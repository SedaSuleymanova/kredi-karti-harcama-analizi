# Veri Sözlüğü (Data Dictionary)

## 1. Genel Bilgiler

Bu bölümde temiz veri setindeki sütunların ne anlama geldiği, hangi veri türünde olduğu ve hangi değerleri alabileceği açıklanmıştır.

- Dosya adı: `harcamalar_temiz.csv`
- Kayıt sayısı: 1.491
- Sütun sayısı: 3
- Tarih aralığı: 2023-01-01 – 2025-12-31
- Karakter kodlaması: UTF-8
- Sütun ayırıcı: virgül (`,`)
- Ondalık ayırıcı: nokta (`.`)
- Kayıtlar tarihe göre sıralıdır ve her satır bir harcamayı gösterir.

## 2. Sütunlar

| Sütun Adı | Açıklama | Veri Türü | Format | Örnek | Zorunlu |
|---|---|---|---|---|---|
| `Tarih` | Harcamanın yapıldığı gün | Tarih (datetime) | `YYYY-MM-DD` | `2024-03-15` | Evet |
| `Tutar` | Harcama tutarı (TL) | Ondalıklı sayı (float) | İki ondalık basamak | `486.25` | Evet |
| `Kategori` | Harcamanın türü | Metin (string) | Kategori listesindeki ad | `Market` | Evet |

## 3. Sütunların Açıklaması

**Tarih:** Harcamanın yapıldığı günü gösterir, saat bilgisi yoktur. 1 Ocak 2023 ile 31 Aralık 2025 arasındaki tarihleri içerir. Aylık analiz (FR-04) ve tahmin (FR-06) yapılırken harcamalar bu sütuna göre aylara ayrılacaktır.

**Tutar:** Harcamanın TL cinsinden tutarıdır. Tüm değerler sıfırdan büyüktür. En küçük harcama 24,55 TL, en büyük harcama 8.563,06 TL'dir. Toplam ve ortalama harcama (FR-02) bu sütundan hesaplanır.

**Kategori:** Harcamanın hangi türe ait olduğunu gösterir. Kategori bazında analiz (FR-03) bu sütuna göre yapılır. Alabileceği değerler aşağıdaki tabloda verilmiştir.

## 4. Kategori Değerleri

| Kategori | Açıklama | Kayıt Sayısı |
|---|---|---|
| `Market` | Gıda ve günlük ihtiyaç alışverişleri | 447 |
| `Ulaşım` | Yakıt, toplu taşıma, taksi vb. | 358 |
| `Restoran` | Restoran, kafe ve yemek siparişleri | 306 |
| `Fatura` | Elektrik, su, doğalgaz, internet ve telefon faturaları | 141 |
| `Eğlence` | Sinema, konser, etkinlik vb. | 105 |
| `Giyim` | Kıyafet ve ayakkabı alışverişleri | 85 |
| `Sağlık` | Eczane ve sağlık harcamaları | 34 |
| `Diğer` | Ham veride kategorisi eksik olan harcamalar | 15 |

## 5. Ham Veri ve Temiz Veri Karşılaştırması

| Sütun | Ham Veri (`harcamalar_ham.csv`) | Temiz Veri (`harcamalar_temiz.csv`) |
|---|---|---|
| `Tarih` | Metin olarak tutuluyor; üç farklı format var; bazı değerler eksik | Tarih türünde; sadece `YYYY-MM-DD`; eksik değer yok |
| `Tutar` | Metin olarak tutuluyor; nokta veya virgül kullanılmış; bazılarında `TL` eki var; bazı değerler eksik | Sayısal; ondalık ayırıcı nokta; eksik değer yok |
| `Kategori` | Büyük-küçük harf ve boşluk farkları var; bazı değerler eksik | Kategori adları düzeltilmiş; eksikler `Diğer` yapılmış |
| Kayıtlar | 1.539 kayıt; tekrar eden kayıtlar var; sıralama karışık | 1.491 kayıt; tekrar yok; tarihe göre sıralı |

## 6. Kullanırken Dikkat Edilmesi Gerekenler

- Dosya Python'da `pd.read_csv("harcamalar_temiz.csv", parse_dates=["Tarih"])` ile okunursa `Tarih` sütunu doğrudan tarih türünde gelir.
- Aynı gün içinde birden fazla harcama olabilir. Aylık toplamlar için veri aylara göre gruplanmalıdır.
- `Diğer` gerçek bir harcama türü değildir, kategorisi bilinmeyen harcamaları gösterir. Kategori karşılaştırmasında bu durum belirtilmelidir.
- Fiyat artışı nedeniyle tutarlar yıllar içinde yükseliyor. Farklı yıllar karşılaştırılırken bu göz önünde bulundurulmalıdır.
