
import pandas as pd
import matplotlib.pyplot as plt
# Temizlenmiş kredi kartı verilerini okuyoruz
df = pd.read_csv("harcamalar_temiz.csv", parse_dates=["Tarih"])

# Genel istatistikleri hesaplıyoruz
toplam_harcama = df["Tutar"].sum()
ortalama_harcama = df["Tutar"].mean()
islem_sayisi = len(df)

# Sonuçları ekrana yazdırıyoruz
print("KREDİ KARTI HARCAMA ANALİZİ")
print("---------------------------")
print(f"Toplam Harcama: {toplam_harcama:,.2f} TL")
print(f"Ortalama İşlem Tutarı: {ortalama_harcama:,.2f} TL")
print(f"Toplam İşlem Sayısı: {islem_sayisi}")

# Kategorilere göre toplam harcamaları hesaplıyoruz
kategori_harcamalari = df.groupby("Kategori")["Tutar"].sum()
kategori_harcamalari = kategori_harcamalari.sort_values(ascending=False)

print("\nKATEGORİLERE GÖRE HARCAMALAR")
print("---------------------------")
print(kategori_harcamalari.round(2))

# Tarih sütununu tarih formatına dönüştürüyoruz
df["Tarih"] = pd.to_datetime(df["Tarih"])

# Harcamaları aylara göre grupluyoruz
aylik_harcamalar = df.groupby(
    df["Tarih"].dt.to_period("M")
)["Tutar"].sum()

print("\nAYLIK HARCAMA ANALİZİ")
print("---------------------------")
print(aylik_harcamalar.round(2))
# Aylık harcamaların grafiğini oluşturuyoruz
plt.figure(figsize=(12, 6))

plt.plot(
    aylik_harcamalar.index.astype(str),
    aylik_harcamalar.values,
    marker="o",
    color="blue"
)

plt.title("2023-2025 Aylık Kredi Kartı Harcamaları")
plt.xlabel("Aylar")
plt.ylabel("Toplam Harcama (TL)")

plt.xticks(rotation=90)
plt.grid(True)
plt.tight_layout()

plt.show()
# Kategorilere göre harcama grafiği
plt.figure(figsize=(10, 6))

kategori_harcamalari.plot(kind="bar", color="skyblue")

plt.title("Kategorilere Göre Kredi Kartı Harcamaları")
plt.xlabel("Kategoriler")
plt.ylabel("Toplam Harcama (TL)")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()