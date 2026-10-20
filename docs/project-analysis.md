# Proje Analiz Raporu

## 1. Proje Adı

İstatistiksel Modeller ve Büyük Dil Modelleri ile Kredi Kartı Harcamalarının Analizi ve Tahmini

## 2. Projenin Amacı

Bu projenin amacı, kredi kartı harcama verilerini istatistiksel yöntemler ve büyük dil modelleri (LLM) kullanarak analiz eden bir sistem geliştirmektir.

Sistem, kullanıcıların harcama alışkanlıklarını incelemeyi, harcamaları kategori ve aylara göre karşılaştırmayı, gelecekteki harcamaları tahmin etmeyi ve analiz sonuçlarını doğal dilde açıklamayı amaçlamaktadır.

## 3. Projenin Kapsamı

Proje kapsamında aşağıdaki işlemler gerçekleştirilecektir:

- Kredi kartı harcama verilerinin sisteme aktarılması ve kontrol edilmesi.
- Harcamaların toplam, ortalama ve kategori bazında analiz edilmesi.
- Aylık harcamaların karşılaştırılması ve grafiklerle gösterilmesi.
- Doğrusal regresyon yöntemiyle gelecekteki harcamaların tahmin edilmesi.
- Doğrusal regresyon modelinin, önceki ayın harcamasını temel alan basit tahmin yöntemiyle karşılaştırılması.
- ChatGPT gibi büyük dil modelleri aracılığıyla analiz sonuçlarının açıklanması.
- Kullanıcılara bütçe yönetimi konusunda veriye dayalı öneriler sunulması.

## 4. Hedef Kullanıcılar

Sistemin hedef kullanıcıları, kredi kartı harcamalarını takip etmek, harcama alışkanlıklarını anlamak ve bütçelerini daha bilinçli yönetmek isteyen bireylerdir.

## 5. Kullanılacak Yöntemler ve Teknolojiler

### İstatistiksel Analiz

Harcamaların toplamı, ortalaması ve kategorilere göre dağılımı hesaplanacaktır.

### Doğrusal Regresyon

Geçmiş harcama verileri kullanılarak gelecek döneme ilişkin tahminler oluşturulacaktır.

### Basit Tahmin Yöntemi

Bir sonraki dönemin harcaması, karşılaştırma amacıyla önceki dönemin harcamasına eşit kabul edilecektir.

### Büyük Dil Modeli (LLM)

Analiz sonuçları doğal dilde açıklanacak ve bütçe yönetimine yönelik öneriler üretilecektir. LLM tarafından oluşturulan açıklamalar, hesaplanan verilerle tutarlılık açısından değerlendirilecektir.

### Kullanılacak Teknolojiler

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- ChatGPT veya uygun bir büyük dil modeli

## 6. Projenin Beklenen Çıktıları

- Harcama analiz sonuçları ve grafikler.
- Gelecek döneme ilişkin harcama tahminleri.
- Tahmin yöntemlerinin karşılaştırılması.
- LLM tarafından oluşturulan açıklamalar ve bütçe önerileri.
- Sistem gereksinimleri, test senaryoları ve proje dokümantasyonu.

## 7. Projenin Sınırlamaları

Sistemin tahmin başarısı kullanılan veri setinin kalitesine ve geçmiş verilerin yeterliliğine bağlıdır. Tahmin sonuçları kesin finansal sonuçlar olarak değerlendirilmemelidir.

LLM tarafından üretilen öneriler bilgilendirme amacı taşır ve hesaplanan verilerle tutarlılık açısından kontrol edilmelidir. Projede gerçek kişilere ait hassas finansal veriler yerine uygun açık veya sentetik veriler kullanılacaktır.

## 8. Başarı Ölçütleri

- Harcama istatistiklerinin doğru hesaplanması.
- Harcamaların kategori ve dönem bazında görüntülenebilmesi.
- Tahmin modellerinin aynı test verileri üzerinde karşılaştırılması.
- Tahmin hatasının MAE metriğiyle değerlendirilmesi.
- LLM açıklamalarının analiz sonuçlarıyla tutarlı olması.

## 9. Sonuç

Bu proje, istatistiksel analiz yöntemlerini ve büyük dil modellerini bir araya getirerek kredi kartı harcamalarının daha anlaşılır hâle getirilmesini ve gelecekteki harcamaların tahmin edilmesini amaçlamaktadır.
