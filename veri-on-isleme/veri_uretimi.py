# Sentetik kredi kartı harcama verisi oluşturma
# Tek kişi, 36 ay (Ocak 2023 - Aralık 2025), tutarlar TL
# Temizleme adımlarını gösterebilmek için veriye bilerek hatalar ekleniyor
# Çıktı: harcamalar_ham.csv

import numpy as np
import pandas as pd

RASTGELE_TOHUM = 42          # her çalıştırmada aynı veri çıksın diye
BASLANGIC = "2023-01-01"
AY_SAYISI = 36
AYLIK_ARTIS = 0.025          # fiyat artışı için aylık %2,5

rng = np.random.default_rng(RASTGELE_TOHUM)

# kategori: (aylık ortalama işlem sayısı, ortalama tutar TL, sigma)
KATEGORILER = {
    "Market":   (12, 450, 0.55),
    "Restoran": (8, 350, 0.50),
    "Ulaşım":   (10, 200, 0.60),
    "Giyim":    (2, 1200, 0.60),
    "Eğlence":  (3, 500, 0.60),
    "Sağlık":   (1, 600, 0.70),
}

# faturalar: (adı, ortalama tutar TL, ödeme günü)
FATURALAR = [
    ("Elektrik", 450, 12),
    ("Su", 200, 15),
    ("Doğalgaz", 500, 18),
    ("İnternet ve Telefon", 400, 22),
]


def mevsim_carpani(kategori, ay):
    # (işlem sayısı çarpanı, tutar çarpanı)
    if kategori in ("Giyim", "Eğlence") and ay == 12:
        return 1.8, 1.2                      # yılbaşı
    if kategori in ("Restoran", "Eğlence") and ay in (6, 7, 8):
        return 1.3, 1.0                      # yaz
    if kategori == "Ulaşım" and ay in (7, 8):
        return 1.2, 1.3                      # tatil
    return 1.0, 1.0


def dogalgaz_carpani(ay):
    # kışın yüksek, yazın düşük
    return {1: 2.6, 2: 2.3, 3: 1.7, 4: 1.0, 5: 0.5, 6: 0.3, 7: 0.3,
            8: 0.3, 9: 0.4, 10: 0.8, 11: 1.6, 12: 2.3}[ay]


def temiz_veri_uret():
    kayitlar = []
    aylar = pd.date_range(BASLANGIC, periods=AY_SAYISI, freq="MS")

    for i, ay_basi in enumerate(aylar):
        fiyat_endeksi = (1 + AYLIK_ARTIS) ** i
        gun_sayisi = ay_basi.days_in_month

        for kategori, (ort_adet, ort_tutar, sigma) in KATEGORILER.items():
            adet_c, tutar_c = mevsim_carpani(kategori, ay_basi.month)
            adet = rng.poisson(ort_adet * adet_c)
            for _ in range(adet):
                gun = int(rng.integers(1, gun_sayisi + 1))
                # log-normal: küçük harcamalar çok, büyükler az
                mu = np.log(ort_tutar * tutar_c * fiyat_endeksi) - sigma**2 / 2
                tutar = rng.lognormal(mu, sigma)
                kayitlar.append((ay_basi.replace(day=gun), round(tutar, 2), kategori))

        for fatura, ort_tutar, odeme_gunu in FATURALAR:
            carpan = dogalgaz_carpani(ay_basi.month) if fatura == "Doğalgaz" else 1.0
            tutar = ort_tutar * carpan * fiyat_endeksi * rng.normal(1, 0.08)
            kayitlar.append((ay_basi.replace(day=odeme_gunu), round(tutar, 2), "Fatura"))

    df = pd.DataFrame(kayitlar, columns=["Tarih", "Tutar", "Kategori"])
    df = df.drop_duplicates().sort_values("Tarih").reset_index(drop=True)
    return df


def hatalari_ekle(df):
    # temizleme kodunu göstermek için bilerek hata ekliyoruz
    ham = df.copy()
    ham["Tarih"] = ham["Tarih"].dt.strftime("%Y-%m-%d")
    ham["Tutar"] = ham["Tutar"].map(lambda x: f"{x:.2f}")
    n = len(ham)

    # farklı tarih formatları (~%15)
    idx = rng.choice(n, size=int(n * 0.15), replace=False)
    for j, k in enumerate(idx):
        t = pd.Timestamp(ham.at[k, "Tarih"])
        ham.at[k, "Tarih"] = t.strftime("%d.%m.%Y") if j % 2 == 0 else t.strftime("%d/%m/%Y")

    # virgüllü tutarlar ve "TL" eki (~%10)
    idx = rng.choice(n, size=int(n * 0.10), replace=False)
    for j, k in enumerate(idx):
        deger = ham.at[k, "Tutar"].replace(".", ",")
        ham.at[k, "Tutar"] = f"{deger} TL" if j % 2 == 0 else deger

    # kategori adlarında harf/boşluk farkları (~%8)
    idx = rng.choice(n, size=int(n * 0.08), replace=False)
    for j, k in enumerate(idx):
        kat = ham.at[k, "Kategori"]
        ham.at[k, "Kategori"] = [kat.lower(), kat.upper(), f" {kat} "][j % 3]

    # eksik değerler
    for sutun, adet in (("Tarih", 6), ("Tutar", 12), ("Kategori", 15)):
        idx = rng.choice(n, size=adet, replace=False)
        ham.loc[idx, sutun] = np.nan

    # tekrar eden kayıtlar (~%2)
    tekrar = ham.sample(n=int(n * 0.02), random_state=RASTGELE_TOHUM)
    ham = pd.concat([ham, tekrar], ignore_index=True)

    # sırayı karıştır
    return ham.sample(frac=1, random_state=RASTGELE_TOHUM).reset_index(drop=True)


if __name__ == "__main__":
    temiz = temiz_veri_uret()
    ham = hatalari_ekle(temiz)
    ham.to_csv("harcamalar_ham.csv", index=False, encoding="utf-8")
    print("Hatasız kayıt sayısı:", len(temiz))
    print("Ham dosyadaki kayıt sayısı:", len(ham))
