# Veri Seti Kaynağı ve Açıklaması

## 1. Veri Setinin Kaynağı

Projede gerçek bir veri seti yerine sentetik (yapay) bir kredi kartı harcama verisi kullandık. Veriyi Python ile yazdığımız `veri_uretimi.py` dosyasıyla oluşturduk.

Kodda rastgele sayı üretimi için sabit bir tohum değeri (42) kullanıldı. Bu yüzden kod her çalıştırıldığında aynı veri tekrar oluşuyor ve grubun diğer üyeleri de aynı veri üzerinde çalışabiliyor.

## 2. Neden Sentetik Veri Kullandık?

Proje analiz raporunda ve gereksinimlerde (NFR-05) gerçek kişilere ait finansal verilerin kullanılmaması gerektiği belirtilmişti. Sentetik veri herhangi bir kişiye ait olmadığı için bu şartı karşılıyor.

Açık kaynaklı kredi kartı veri setlerine de baktık. Ancak bunların çoğu dolandırıcılık tespiti için hazırlanmış ve içlerinde harcama kategorisi ya da birkaç yıla yayılan aylık harcama bilgisi yok. Bizim projemizde hem kategori analizi hem de aylık tahmin yapılacağı için bu veri setleri uygun değildi.

Sentetik verinin bir avantajı da verinin nasıl oluştuğunu bilmemiz. Böylece temizleme ve analiz sonuçlarının doğru olup olmadığını kontrol edebiliyoruz (NFR-02). Ayrıca veriyi 36 ay olarak hazırladığımız için tahmin aşamasında veri eğitim ve test dönemlerine ayrılabilir (FR-06, FR-07).

## 3. Veri Setinin Genel Özellikleri

- Veri tek bir kişinin harcamalarını içeriyor.
- 1 Ocak 2023 ile 31 Aralık 2025 arasındaki 36 ayı kapsıyor.
- Tutarlar Türk Lirası (TL) cinsinden.
- FR-01'de belirtildiği gibi `Tarih`, `Tutar` ve `Kategori` sütunlarından oluşuyor.
- Kategoriler: Market, Restoran, Ulaşım, Fatura, Giyim, Eğlence ve Sağlık. Kategorisi bilinmeyen kayıtlar için ayrıca Diğer kategorisi var.
- Dosya formatı CSV, karakter kodlaması UTF-8.

## 4. Verinin Nasıl Oluşturulduğu

Verinin gerçek bir kişinin harcamalarına benzemesi için birkaç şeye dikkat ettik.

Her kategori için aylık ortalama bir işlem sayısı belirledik. Örneğin markette ayda ortalama 12, giyimde ayda ortalama 2 harcama var. Her ay bu sayı rastgele biraz değişiyor.

Tutarları log-normal dağılımla ürettik. Bu dağılımda küçük harcamalar çok, büyük harcamalar az oluyor. Gerçek kredi kartı ekstrelerinde de durum genelde böyle.

Elektrik, su, doğalgaz ve internet/telefon faturaları her ay belli günlerde ödeniyor. Doğalgaz faturası kışın yüksek, yazın düşük.

Bazı mevsimsel etkiler de ekledik. Aralıkta giyim ve eğlence harcamaları artıyor. Yazın restoran ve eğlence harcamaları, temmuz ve ağustosta ise ulaşım harcamaları yükseliyor.

Son olarak fiyatların zamanla arttığını göstermek için tutarlara her ay %2,5 artış uyguladık. Bu sayede veride zamanla artan bir eğilim oluştu ve regresyon modelinin bu eğilimi yakalaması bekleniyor.

## 5. Ham Verideki Sorunlar

Temizleme adımlarını gösterebilmek için ham veriye (`harcamalar_ham.csv`) bilerek bazı hatalar ekledik. Gerçek hayatta bankalardan ya da farklı uygulamalardan alınan verilerde de benzer sorunlar sık görülüyor.

Tarihlerin çoğu `YYYY-MM-DD` formatında ama 116 kayıt `GG.AA.YYYY`, 115 kayıt da `GG/AA/YYYY` formatında yazıldı.

151 tutarda ondalık ayırıcı olarak virgül kullanıldı (örneğin `1286,46`). Bunların 74'ünün sonunda ayrıca `TL` yazıyor.

123 kayıtta kategori adı farklı yazıldı. Bazıları küçük harfle (`market`), bazıları büyük harfle (`ULAŞIM`), bazıları da başında ve sonunda boşlukla (` Giyim `) yazılmış.

Bunların dışında 6 kayıtta tarih, 13 kayıtta tutar, 15 kayıtta kategori eksik. 29 kayıt da veride iki kez geçiyor. Kayıtlar ayrıca tarih sırasına göre değil, karışık sırada.

## 6. Veri Temizleme Adımları

Temizleme işlemlerini `veri_temizleme.py` dosyasında yaptık. Adımlar şöyle:

1. **Sütun kontrolü:** Önce dosyada `Tarih`, `Tutar` ve `Kategori` sütunlarının olup olmadığına bakılıyor. Eksik sütun varsa program hata mesajı verip duruyor (FR-01).

2. **Tarihlerin düzenlenmesi:** Üç farklı tarih formatı okunup hepsi `YYYY-MM-DD` formatına çevriliyor. Okunamayan tarihler geçersiz sayılıyor.

3. **Tutarların sayıya çevrilmesi:** `TL` yazısı ve boşluklar siliniyor, virgüller noktaya çevriliyor. Sonra tutarlar iki ondalık basamaklı sayıya dönüştürülüyor.

4. **Kategori adlarının düzeltilmesi:** Baştaki ve sondaki boşluklar siliniyor, büyük-küçük harf farkları gideriliyor. Burada Türkçe karakterlerde bir sorunla karşılaştık. Python'un `lower()` fonksiyonu büyük `I` harfini `i` yapıyor, bu yüzden `ULAŞIM` kelimesi `ulaşim` oluyor ve `Ulaşım` ile eşleşmiyordu. Bunu çözmek için önce `I` harfini `ı`, `İ` harfini `i` yapan küçük bir fonksiyon yazdık.

5. **Eksik veriler:** Tarihi veya tutarı eksik olan kayıtları sildik. Tarihi olmayan bir harcamanın hangi aya ait olduğu bilinmiyor. Eksik tutarları ortalama gibi bir değerle doldurmak da toplam harcamayı olduğundan farklı gösterirdi. Kategorisi eksik olan kayıtları ise silmedik, `Diğer` kategorisine aldık. Böylece bu harcamaların tutarları toplamlarda yer almaya devam ediyor.

6. **Tekrar eden kayıtlar:** Tarihi, tutarı ve kategorisi aynı olan kayıtlardan sadece birini bıraktık. Bu kontrolü formatları düzelttikten sonra yaptık. Aksi hâlde örneğin tarihi farklı formatta yazılmış aynı kayıt tekrar olarak görülmeyebilirdi.

7. **Geçersiz tutarlar:** Sıfır veya negatif tutar olup olmadığı kontrol edildi. Bizim verimizde böyle bir kayıt çıkmadı ama kod başka bir veriyle çalıştırıldığında bu kontrol işe yarayabilir.

8. **Kaydetme:** Temizlenen veri tarihe göre sıralanıp `harcamalar_temiz.csv` dosyasına kaydedildi.

## 7. Temizleme Sonuçları

| İşlem | Kayıt Sayısı |
|---|---|
| Ham veri | 1.539 |
| Tarihi eksik olduğu için silinen | 6 |
| Tutarı eksik olduğu için silinen | 13 |
| Kategorisi eksik olup `Diğer` yapılan | 15 |
| Silinen tekrar eden kayıt | 29 |
| Sıfır veya negatif tutar nedeniyle silinen | 0 |
| **Temiz veri** | **1.491** |

Temizlemeden sonra veride eksik değer ya da tekrar eden kayıt kalmadı. Tüm tarihler aynı formatta, tutarlar sayısal ve kategori adları düzgün.

Sonuçların doğru olup olmadığını görmek için temiz veriyi, hatalar eklenmeden önceki orijinal veriyle karşılaştırdık. 1.491 kaydın hepsi tarih ve tutar olarak orijinal veriyle eşleşti. `Diğer` yapılan 15 kayıt dışında kategoriler de doğru çıktı.

## 8. Temiz Veri Setinin Özeti

| Yıl | İşlem Sayısı | Toplam Harcama |
|---|---|---|
| 2023 | 515 | 249.339 TL |
| 2024 | 487 | 297.358 TL |
| 2025 | 489 | 447.768 TL |
| **Toplam** | **1.491** | **994.465 TL** |

Aylık ortalama harcama yaklaşık 27.624 TL. En düşük harcama Şubat 2023'te (yaklaşık 14.610 TL), en yüksek harcama ise Aralık 2025'te (yaklaşık 75.279 TL) yapılmış. Bir işlemin ortalama tutarı 666,98 TL, medyanı ise 498,47 TL.

Aralık 2025'teki harcamanın bu kadar yüksek olmasının sebebi, yılbaşı dönemindeki giyim harcamalarıyla fiyat artışının üst üste gelmesi. Tahmin aşamasında bu ayın diğerlerinden yüksek olduğu göz önünde bulundurulmalı.

## 9. Teslim Edilen Dosyalar

- `harcamalar_ham.csv`: Hatalı ham veri
- `veri_uretimi.py`: Veriyi oluşturan kod
- `veri_temizleme.py`: Temizleme kodu
- `harcamalar_temiz.csv`: Analize hazır temiz veri
- Veri Sözlüğü: Sütunların ve değerlerin açıklaması

Kodları çalıştırmak için:

```
python veri_uretimi.py
python veri_temizleme.py
```

## 10. Sınırlamalar

Veri sentetik olduğu için gerçek bir kişinin harcama alışkanlıklarını tam olarak yansıtmıyor. Kategori ortalamaları, mevsim etkileri ve fiyat artışı bizim yaptığımız varsayımlara dayanıyor. Bu yüzden analiz ve tahmin sonuçları, yöntemlerin doğru çalıştığını göstermek için kullanılmalı, gerçek finansal sonuç gibi yorumlanmamalı.

## 11. Sonuç

Bu bölümde projeye uygun, tek kişiye ait 36 aylık sentetik bir harcama veri seti hazırladık. Ham verideki format farklılıklarını, eksik verileri ve tekrar eden kayıtları temizledik. Sonuçta `Tarih`, `Tutar` ve `Kategori` sütunlarından oluşan, analize hazır bir CSV dosyası elde ettik. Bu dosya sonraki aşamalarda yapılacak analiz, grafik ve tahmin çalışmalarında doğrudan kullanılabilir.
