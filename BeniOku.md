### YouTube Playlist Transcript Downloader

Bu proje, YouTube oynatma listelerinden video transkriptlerini indirir ve bunları yapılandırılmış bir klasör sistemi içinde düzenler. Her oynatma listesi ayrı bir klasör olarak kaydedilir ve her videonun transkripti `.txt` dosyası olarak saklanır. Transkriptler zaman damgalarını içermez ve video başlığı ile yüklenme tarihine göre adlandırılır.

---

## Özellikler

1. **YouTube Oynatma Listesi İşleme**:
   - Her oynatma listesinden video bilgilerini (başlık, ID, yükleme tarihi) çıkarır.
   - `youtube_lists.txt` dosyasında listelenen birden fazla oynatma listesini destekler.

2. **Klasör Organizasyonu**:
   - Her oynatma listesi için oynatma listesi adıyla bir klasör oluşturur.
   - İlgili oynatma listesi klasörünün içine, her videonun transkriptini ayrı bir `.txt` dosyası olarak kaydeder.

3. **Transkript Yönetimi**:
   - YouTube'un yerleşik transkript API'sini kullanarak transkriptleri çeker.
   - Sorunu günlüğe kaydederek özel veya kullanılamayan videoları sorunsuz bir şekilde işler.

4. **Dosya Adlandırma ve Klasör Yapısı**:
   - Uzun başlıkları, dosya sistemi hatalarını önlemek için kısaltır ve sonuna `_` ekler.
   - Windows dosya sistemi kurallarıyla uyumluluğu sağlar (geçersiz karakterleri kaldırır).

---

## Kurulum

### Ön Gereksinimler
- Python 3.7 veya daha yüksek sürüm
- Bir YouTube Data API v3 anahtarı

### Adımlar

1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/fkucuker
   cd YouTube_Project
   ```
