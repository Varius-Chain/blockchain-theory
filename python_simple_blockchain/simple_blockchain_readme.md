# Simple Blockchain - Basit Blok Zinciri

Bu proje, Python ile temel blok zinciri (blockchain) yapısının nasıl oluşturulacağını gösteren basit bir örnektir. 

## Özellikler

- Blok yapısı (index, zaman damgası, veri, önceki blok hash’i)
- SHA-256 ile blok hash’lerinin hesaplanması
- Zincire yeni blok ekleme
- Zincirin geçerliliğinin kontrol edilmesi (hash doğrulaması ve önceki hash eşleşmesi)

## Dosyalar

- `simple_blockchain.py`: Basit blockchain implementasyonu ve örnek kullanım.

## Nasıl Kullanılır?

1. Python 3 kurulu olduğundan emin olun.
2. Terminal ya da komut istemcisinde dosyanın olduğu klasöre gidin.
3. Aşağıdaki komutla çalıştırın:

```bash
python simple_blockchain.py
```

## Örnek Çıktı

```
Blockchain geçerli mi? True
Index: 0
Timestamp: 1691678509.123456
Data: Genesis Block
Previous Hash: 0
Hash: 1a2b3c4d5e6f...

------------------------------
Index: 1
Timestamp: 1691678515.654321
Data: {'amount': 4}
Previous Hash: 1a2b3c4d5e6f...
Hash: 7f8e9d0c1b2a...

------------------------------
Index: 2
Timestamp: 1691678520.987654
Data: {'amount': 10}
Previous Hash: 7f8e9d0c1b2a...
Hash: 3d4e5f6a7b8c...

------------------------------
```

## Geliştirme İpuçları

- Proof-of-Work (iş kanıtı) mekanizması eklenebilir.  
- Bloklarda işlem listesi tutularak gerçek bir blockchain simülasyonu yapılabilir.  
- Ağ üzerinden düğümler arası iletişim eklenebilir.  

---