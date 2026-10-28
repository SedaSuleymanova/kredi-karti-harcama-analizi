# Kredi kartı harcama verisinin temizlenmesi
# Girdi: harcamalar_ham.csv
# Çıktı: harcamalar_temiz.csv
#
# Farklı dosya adlarıyla çalıştırmak için:
#   python veri_temizleme.py girdi.csv cikti.csv

import sys

import numpy as np
import pandas as pd

GEREKLI_SUTUNLAR = ["Tarih", "Tutar", "Kategori"]
KATEGORILER = ["Market", "Restoran", "Ulaşım", "Fatura", "Giyim", "Eğlence", "Sağlık"]
TARIH_FORMATLARI = ["%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y"]


def veriyi_oku(dosya):
    # Önce her şeyi metin olarak okuyoruz, türleri aşağıda kendimiz çeviriyoruz
    df = pd.read_csv(dosya, dtype=str, encoding="utf-8")
    df.columns = df.columns.str.strip()

    eksik = [s for s in GEREKLI_SUTUNLAR if s not in df.columns]
    if eksik:
        raise ValueError("Gerekli sütunlar bulunamadı: " + ", ".join(eksik))
    return df[GEREKLI_SUTUNLAR].copy()


def tarih_cevir(deger):
    if pd.isna(deger):
        return pd.NaT
    deger = str(deger).strip()
    for bicim in TARIH_FORMATLARI:
        try:
            return pd.to_datetime(deger, format=bicim)
        except ValueError:
            pass
    return pd.NaT  # hiçbir formata uymadıysa geçersiz


def tutar_cevir(deger):
    # "1286,46 TL", "1286,46" ve "1286.46" gibi yazımları sayıya çevirir
    if pd.isna(deger):
        return np.nan
    metin = str(deger).upper().replace("TL", "").replace(" ", "").strip()
    if "," in metin and "." in metin:   # 1.286,46 gibi
        metin = metin.replace(".", "").replace(",", ".")
    elif "," in metin:                  # 1286,46 gibi
        metin = metin.replace(",", ".")
    try:
        return round(float(metin), 2)
    except ValueError:
        return np.nan


def kucuk_harf(metin):
    # lower() "I" harfini "i" yaptığı için ULAŞIM -> ulaşim oluyordu,
    # o yüzden Türkçe harfleri önce kendimiz çeviriyoruz
    return metin.replace("I", "ı").replace("İ", "i").lower()


def kategori_duzelt(deger):
    if pd.isna(deger) or str(deger).strip() == "":
        return np.nan
    deger = str(deger).strip()
    for kategori in KATEGORILER:
        if kucuk_harf(deger) == kucuk_harf(kategori):
            return kategori
    return deger.title()  # listede yoksa olduğu gibi bırak, raporda görünür


def temizle(df):
    rapor = {"Ham kayıt sayısı": len(df)}
    for s in GEREKLI_SUTUNLAR:
        rapor[f"Eksik {s} (ham)"] = int(df[s].isna().sum())

    df["Tarih"] = df["Tarih"].map(tarih_cevir)
    df["Tutar"] = df["Tutar"].map(tutar_cevir).astype(float)
    df["Kategori"] = df["Kategori"].map(kategori_duzelt)

    # Tarihi ya da tutarı olmayan satırlar siliniyor
    tarih_yok = df["Tarih"].isna()
    tutar_yok = df["Tutar"].isna()
    rapor["Tarihi eksik/geçersiz olduğu için silinen"] = int(tarih_yok.sum())
    rapor["Tutarı eksik/geçersiz olduğu için silinen"] = int((tutar_yok & ~tarih_yok).sum())
    df = df[~(tarih_yok | tutar_yok)].copy()

    # Kategorisi olmayanları silmiyoruz, tutarları toplamda kalsın diye "Diğer" yapıyoruz
    kategori_yok = df["Kategori"].isna()
    rapor["Kategorisi eksik olup 'Diğer' yapılan"] = int(kategori_yok.sum())
    df.loc[kategori_yok, "Kategori"] = "Diğer"

    # Tekrarları formatlar düzeldikten sonra siliyoruz
    once = len(df)
    df = df.drop_duplicates()
    rapor["Silinen tekrar eden kayıt"] = once - len(df)

    gecersiz = df["Tutar"] <= 0
    rapor["Sıfır/negatif tutar nedeniyle silinen"] = int(gecersiz.sum())
    df = df[~gecersiz]

    rapor["Listede olmayan kategori sayısı"] = int((~df["Kategori"].isin(KATEGORILER + ["Diğer"])).sum())

    df = df.sort_values(["Tarih", "Kategori", "Tutar"]).reset_index(drop=True)
    rapor["Temiz kayıt sayısı"] = len(df)
    return df, rapor


def kaydet(df, dosya):
    cikti = df.copy()
    cikti["Tarih"] = cikti["Tarih"].dt.strftime("%Y-%m-%d")
    cikti.to_csv(dosya, index=False, encoding="utf-8", float_format="%.2f")


def rapor_yazdir(df, rapor):
    print("----- Temizleme Raporu -----")
    for k, v in rapor.items():
        print(f"{k:<45}{v:>6}")
    print()
    print("Tarih aralığı:", df["Tarih"].min().date(), "-", df["Tarih"].max().date())
    print("Ay sayısı:", df["Tarih"].dt.to_period("M").nunique())
    print(f"Toplam tutar: {df['Tutar'].sum():,.2f} TL")
    print("\nSütun türleri:")
    print(df.dtypes.to_string())
    print("\nKategorilere göre kayıt sayısı:")
    print(df["Kategori"].value_counts().to_string())
    print("\nKalan eksik değer:", int(df.isna().sum().sum()))
    print("Kalan tekrar eden kayıt:", int(df.duplicated().sum()))


if __name__ == "__main__":
    girdi = sys.argv[1] if len(sys.argv) > 1 else "harcamalar_ham.csv"
    cikti = sys.argv[2] if len(sys.argv) > 2 else "harcamalar_temiz.csv"

    try:
        ham = veriyi_oku(girdi)
    except (FileNotFoundError, ValueError) as hata:
        print("HATA:", hata)
        sys.exit(1)

    temiz, rapor = temizle(ham)
    kaydet(temiz, cikti)
    rapor_yazdir(temiz, rapor)
    print("\nTemiz veri kaydedildi:", cikti)
