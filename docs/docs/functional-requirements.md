# Fonksiyonel ve Fonksiyonel Olmayan Gereksinimler

## 1. Fonksiyonel Gereksinimler

Fonksiyonel gereksinimler, sistemin hangi işlemleri yapması gerektiğini belirtir.

**FR-01: Veri Aktarımı**

Sistem, analiz için uygun formatta hazırlanmış harcama verilerini okuyabilmelidir.

**FR-02: Harcamaların Analizi**

Sistem, toplam harcama ve ortalama harcama gibi temel istatistikleri hesaplayabilmelidir.

**FR-03: Kategori Bazında Analiz**

Sistem, harcamaları kategorilere göre gruplandırabilmeli ve karşılaştırabilmelidir.

**FR-04: Aylık Harcama Analizi**

Sistem, aylık harcamaları hesaplayabilmeli ve farklı ayların sonuçlarını karşılaştırabilmelidir.

**FR-05: Grafik Oluşturma**

Sistem, analiz sonuçlarını grafiklerle gösterebilmelidir.

**FR-06: Harcama Tahmini**

Sistem, geçmiş harcama verilerini kullanarak doğrusal regresyon yöntemiyle gelecek döneme ilişkin tahmin oluşturabilmelidir.

**FR-07: Tahmin Yöntemlerinin Karşılaştırılması**

Sistem, doğrusal regresyon sonuçlarını önceki ayın harcamasını temel alan basit tahmin yöntemiyle karşılaştırabilmelidir.

**FR-08: Tahmin Hatasının Hesaplanması**

Sistem, tahmin sonuçlarının hata düzeyini MAE metriğiyle hesaplayabilmelidir.

**FR-09: LLM ile Sonuçların Açıklanması**

Sistem, istatistiksel analiz sonuçlarını büyük dil modeline aktararak anlaşılır açıklamalar oluşturabilmelidir.

**FR-10: Bütçe Önerileri**

Sistem, analiz sonuçlarına dayanarak kullanıcıya bütçe yönetimi konusunda öneriler sunabilmelidir.

## 2. Fonksiyonel Olmayan Gereksinimler

Fonksiyonel olmayan gereksinimler, sistemin nasıl çalışması gerektiğini ve hangi kalite özelliklerine sahip olacağını belirtir.

**NFR-01: Kullanılabilirlik**

Sistem kolay anlaşılır olmalı ve analiz sonuçları kullanıcıya açık bir şekilde sunulmalıdır.

**NFR-02: Doğruluk**

İstatistiksel hesaplamalar ve tahmin hata ölçümleri doğru şekilde yapılmalıdır.

**NFR-03: Performans**

Sistem, kullanılan veri setinin boyutuna uygun bir sürede analiz sonuçlarını üretebilmelidir.

**NFR-04: Veri Güvenliği**

Projede gerçek kişilere ait hassas finansal bilgiler kullanılmamalıdır. Veriler güvenli ve uygun şekilde işlenmelidir.

**NFR-05: Güvenilirlik**

LLM tarafından oluşturulan açıklamalar, sisteme aktarılan analiz sonuçlarıyla tutarlı olmalıdır.

**NFR-06: Bakım Kolaylığı**

Kodlar ve proje dosyaları düzenli hazırlanmalı, gerektiğinde güncellenebilecek şekilde yapılandırılmalıdır.

**NFR-07: Anlaşılabilirlik**

Tahmin sonuçları, grafikler ve analiz açıklamaları kullanıcı tarafından kolayca yorumlanabilmelidir.
