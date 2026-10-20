# Fonksiyonel ve Fonksiyonel Olmayan Gereksinimler

## 1. Fonksiyonel Gereksinimler

Fonksiyonel gereksinimler, sistemin hangi işlemleri yapması gerektiğini belirtir.

**FR-01 – Veri Aktarımı:** Sistem, `Tarih`, `Tutar` ve `Kategori` sütunlarını içeren CSV formatındaki harcama verilerini okuyabilmelidir. Gerekli sütunlar eksik olduğunda kullanıcıya hata mesajı verilmelidir.

**FR-02 – Harcamaların Analizi:** Sistem, toplam harcama ve ortalama harcama gibi temel istatistikleri hesaplayabilmelidir.

**FR-03 – Kategori Bazında Analiz:** Sistem, harcamaları kategorilere göre gruplandırabilmeli ve kategoriler arasındaki harcamaları karşılaştırabilmelidir.

**FR-04 – Aylık Harcama Analizi:** Sistem, aylık harcamaları hesaplayabilmeli ve farklı ayların sonuçlarını karşılaştırabilmelidir.

**FR-05 – Grafik Oluşturma:** Sistem, analiz sonuçlarını grafiklerle gösterebilmelidir.

**FR-06 – Harcama Tahmini:** Sistem, geçmiş harcama verilerini kullanarak doğrusal regresyon yöntemiyle gelecek döneme ilişkin tahmin oluşturabilmelidir.

**FR-07 – Tahmin Yöntemlerinin Karşılaştırılması:** Sistem, doğrusal regresyon sonuçlarını önceki ayın harcamasını temel alan basit bir tahmin yöntemiyle karşılaştırabilmelidir.

**FR-08 – Tahmin Hatasının Hesaplanması:** Sistem, tahmin sonuçlarının hata düzeyini Ortalama Mutlak Hata (MAE) metriğiyle hesaplayabilmelidir.

**FR-09 – LLM ile Sonuçların Açıklanması:** Sistem, istatistiksel analiz sonuçlarını büyük dil modeline aktararak anlaşılır açıklamalar oluşturabilmelidir.

**FR-10 – Bütçe Önerileri:** Sistem, analiz sonuçlarına dayanarak kullanıcıya bütçe yönetimi konusunda öneriler sunabilmelidir.

## 2. Fonksiyonel Olmayan Gereksinimler

Fonksiyonel olmayan gereksinimler, sistemin kalite, performans ve güvenilirlik gibi özelliklerini belirtir.

**NFR-01 – Kullanılabilirlik:** Sistem kolay anlaşılır olmalı ve analiz sonuçları kullanıcıya açık bir şekilde sunulmalıdır.

**NFR-02 – Doğruluk:** İstatistiksel hesaplamalar, önceden belirlenmiş doğru sonuçlara sahip test verileri kullanılarak kontrol edilmelidir. Hesaplanan sonuçlar beklenen sonuçlarla eşleşmelidir.

**NFR-03 – Performans:** Sistem, kullanılan veri setinin boyutuna uygun bir sürede analiz sonuçlarını üretebilmelidir.

**NFR-04 – Analiz Süresi:** Sistem, test ortamında 10.000 satırlık bir harcama veri setinin temel istatistiksel analizini 5 saniye içinde tamamlamayı hedeflemelidir. Bu süre test edilerek değerlendirilecektir.

**NFR-05 – Veri Güvenliği:** Projede gerçek kişilere ait hassas finansal bilgiler yerine açık veya sentetik veriler kullanılmalıdır. Veriler uygun şekilde işlenmelidir.

**NFR-06 – LLM Güvenilirliği:** Büyük dil modeli tarafından oluşturulan açıklamalar, Python ile hesaplanan istatistiksel sonuçlarla tutarlı olmalıdır. Modelin verdiği sayısal bilgiler kontrol edilmeli ve doğrulanamayan sonuçlar kesin bilgi olarak sunulmamalıdır.

**NFR-07 – Bakım Kolaylığı:** Kodlar ve proje dosyaları düzenli hazırlanmalı ve gerektiğinde güncellenebilecek şekilde yapılandırılmalıdır.

**NFR-08 – Anlaşılabilirlik:** Tahmin sonuçları, grafikler ve analiz açıklamaları kullanıcı tarafından kolayca yorumlanabilmelidir.
