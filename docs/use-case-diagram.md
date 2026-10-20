# Use Case Diyagramı

## 1. Amaç

Bu diyagram, kredi kartı harcamalarının analizi sisteminde kullanıcının gerçekleştirebileceği temel işlemleri göstermektedir.

## 2. Aktör

**Kullanıcı:** Harcama verilerini yükleyen, analiz sonuçlarını inceleyen ve bütçe önerilerini görüntüleyen kişidir.

## 3. Kullanım Senaryoları

- UC-01: Harcama verilerini CSV dosyasından yükleme
- UC-02: Toplam ve ortalama harcamaları görüntüleme
- UC-03: Kategori bazında harcamaları inceleme
- UC-04: Aylık harcamaları karşılaştırma
- UC-05: Analiz grafiklerini görüntüleme
- UC-06: Gelecek dönem harcama tahminlerini görüntüleme
- UC-07: Tahmin yöntemlerini karşılaştırma
- UC-08: LLM tarafından oluşturulan analiz açıklamalarını görüntüleme
- UC-09: Bütçe önerilerini görüntüleme

## 4. Diyagram

Aşağıdaki diyagram, kullanıcının sistem üzerinden gerçekleştirebileceği temel işlemleri göstermektedir.


```mermaid
flowchart LR
    U["Kullanıcı"]

    subgraph S["Kredi Kartı Harcama Analiz Sistemi"]
        UC1(["CSV verilerini yükle"])
        UC2(["Toplam ve ortalama harcamaları görüntüle"])
        UC3(["Kategori bazında harcamaları incele"])
        UC4(["Aylık harcamaları karşılaştır"])
        UC5(["Grafikleri görüntüle"])
        UC6(["Harcama tahminlerini görüntüle"])
        UC7(["Tahmin yöntemlerini karşılaştır"])
        UC8(["LLM açıklamalarını görüntüle"])
        UC9(["Bütçe önerilerini görüntüle"])
    end

    U --- UC1
    U --- UC2
    U --- UC3
    U --- UC4
    U --- UC5
    U --- UC6
    U --- UC7
    U --- UC8
    U --- UC9
```
