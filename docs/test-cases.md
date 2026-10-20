# Test Senaryoları

## 1. Amaç

Bu doküman, kredi kartı harcamalarının analizi sisteminin temel işlevlerini test etmek için hazırlanmıştır.

## 2. Test Senaryoları

### TC-01 – Geçerli CSV Dosyasını Yükleme

**Amaç:** Sistemin doğru formatta hazırlanmış bir CSV dosyasını okuyabildiğini kontrol etmek.

- **Ön Koşul:** Gerekli sütunları içeren bir CSV dosyası hazırlanmıştır.
- **Test Verisi:** Tarih, Tutar ve Kategori sütunları bulunan geçerli bir dosya.
- **Beklenen Sonuç:** Sistem dosyayı okumalı ve analiz için hazır hale getirmelidir.

### TC-02 – Eksik Sütun Kontrolü

**Amaç:** Gerekli sütunlardan biri eksik olduğunda sistemin hata verip vermediğini kontrol etmek.

- **Ön Koşul:** Bir CSV dosyası hazırlanmıştır.
- **Test Verisi:** Kategori sütunu bulunmayan bir dosya.
- **Beklenen Sonuç:** Sistem dosyayı geçerli kabul etmemeli ve eksik sütun hakkında hata mesajı vermelidir.

### TC-03 – Toplam Harcama Hesaplama

**Amaç:** Toplam harcamanın doğru hesaplandığını kontrol etmek.

- **Test Verisi:** 100 TL, 200 TL ve 300 TL tutarında üç harcama.
- **Beklenen Sonuç:** Toplam harcama 600 TL olmalıdır.

### TC-04 – Ortalama Harcama Hesaplama

**Amaç:** Ortalama harcamanın doğru hesaplandığını kontrol etmek.

- **Test Verisi:** 100 TL, 200 TL ve 300 TL tutarında üç harcama.
- **Beklenen Sonuç:** Ortalama harcama 200 TL olmalıdır.

### TC-05 – Kategori Bazında Harcama Analizi

**Amaç:** Harcamaların kategorilere göre doğru gruplandırıldığını kontrol etmek.

- **Test Verisi:**
  - Market: 100 TL ve 200 TL
  - Ulaşım: 50 TL
- **Beklenen Sonuç:**
  - Market toplamı: 300 TL
  - Ulaşım toplamı: 50 TL

### TC-06 – Aylık Harcama Analizi

**Amaç:** Harcamaların aylara göre doğru gruplandırıldığını kontrol etmek.

- **Test Verisi:**
  - Ocak: 300 TL
  - Şubat: 500 TL
- **Beklenen Sonuç:** Sistem Ocak ayı için 300 TL, Şubat ayı için 500 TL toplam harcama göstermelidir.

### TC-07 – Grafik Oluşturma

**Amaç:** Analiz sonuçlarının grafiklerle gösterildiğini kontrol etmek.

- **Ön Koşul:** Kategori veya aylık analiz tamamlanmıştır.
- **Beklenen Sonuç:** İlgili analiz sonuçlarını gösteren grafik oluşturulmalıdır.

### TC-08 – Harcama Tahmini

**Amaç:** Doğrusal regresyon yönteminin tahmin üretebildiğini kontrol etmek.

- **Ön Koşul:** Tahmin için yeterli geçmiş dönem verisi bulunmaktadır.
- **Beklenen Sonuç:** Sistem gelecek dönem için sayısal bir harcama tahmini üretmelidir.

### TC-09 – Tahmin Yöntemlerini Karşılaştırma

**Amaç:** İki farklı tahmin yönteminin sonuçlarını karşılaştırmak.

- **Ön Koşul:** Doğrusal regresyon ve önceki ayı temel alan tahmin yöntemi uygulanmıştır.
- **Beklenen Sonuç:** Her iki yöntemin tahmin sonuçları ve MAE değerleri karşılaştırılabilmelidir.

### TC-10 – LLM Açıklamalarını Kontrol Etme

**Amaç:** LLM tarafından oluşturulan açıklamaların analiz sonuçlarıyla tutarlı olduğunu kontrol etmek.

- **Test Verisi:** Python tarafından hesaplanan toplam harcama 600 TL'dir.
- **Beklenen Sonuç:** Açıklamada belirtilen toplam harcama 600 TL olmalıdır. Farklı bir tutar verilirse sonuç tutarsız olarak değerlendirilmelidir.

### TC-11 – Bütçe Önerileri Oluşturma

**Amaç:** Sistemin analiz sonuçlarına dayanarak bütçe önerileri sunabildiğini kontrol etmek.

- **Ön Koşul:** Harcama analizi tamamlanmıştır.
- **Beklenen Sonuç:** Sistem, analiz sonuçlarıyla ilişkili anlaşılır bütçe önerileri sunmalıdır.

## 3. Test Sonuçlarının Kaydedilmesi

Her test uygulandığında aşağıdaki bilgiler kaydedilmelidir:

- Test numarası
- Gerçekleşen sonuç
- Beklenen sonuç
- Test durumu: Başarılı veya Başarısız

Testler henüz çalıştırılmadığı için sonuçları önceden başarılı olarak işaretlememek gerekir.
