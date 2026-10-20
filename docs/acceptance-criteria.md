# Kabul Kriterleri

## 1. Amaç

Bu bölüm, kredi kartı harcamalarının analizi sisteminin başarılı kabul edilmesi için karşılanması gereken koşulları açıklamaktadır.

## 2. Kabul Kriterleri

**AC-01 – Veri Aktarımı:** Sistem, `Tarih`, `Tutar` ve `Kategori` sütunlarını içeren geçerli bir CSV dosyasını okuyabilmelidir. Gerekli sütunlar eksik olduğunda sistem hata mesajı vermelidir.

**AC-02 – Toplam Harcama:** Sistem, veri setindeki tüm harcamaların toplamını doğru şekilde hesaplamalıdır.

**AC-03 – Ortalama Harcama:** Sistem, harcamaların ortalama tutarını doğru şekilde hesaplamalıdır.

**AC-04 – Kategori Analizi:** Sistem, her kategori için toplam harcama tutarını hesaplamalı ve sonuçları gösterebilmelidir.

**AC-05 – Aylık Analiz:** Sistem, harcamaları aylara göre gruplandırmalı ve aylık toplamları gösterebilmelidir.

**AC-06 – Grafikler:** Sistem, kategori bazındaki ve aylık harcama sonuçlarını uygun grafiklerle gösterebilmelidir.

**AC-07 – Harcama Tahmini:** Sistem, geçmiş verilere dayanarak doğrusal regresyon yöntemiyle gelecek dönem için harcama tahmini oluşturabilmelidir.

**AC-08 – Tahmin Karşılaştırması:** Sistem, doğrusal regresyon tahminini önceki ayın harcamasını temel alan basit tahmin yöntemiyle karşılaştırabilmelidir.

**AC-09 – Tahmin Hatası:** Sistem, tahmin sonuçlarının MAE değerini hesaplayabilmelidir.

**AC-10 – LLM Açıklaması:** Sistem, istatistiksel analiz sonuçlarını anlaşılır bir dille açıklayabilmelidir. Açıklamalarda kullanılan sayısal bilgiler hesaplanan sonuçlarla tutarlı olmalıdır.

**AC-11 – Bütçe Önerileri:** Sistem, analiz sonuçlarına dayanarak kullanıcıya harcamalarını yönetmesine yardımcı olacak öneriler sunabilmelidir.

**AC-12 – Veri Güvenliği:** Proje kapsamında gerçek kişilere ait hassas finansal veriler yerine açık veya sentetik veriler kullanılmalıdır.

## 3. Genel Kabul Koşulu

Sistem, uygulanması planlanan gereksinimleri karşılamalı ve temel işlevler test verileriyle kontrol edilmelidir. Testlerde bulunan hatalar belirlenmeli ve sonuçlar proje raporunda açıklanmalıdır.
