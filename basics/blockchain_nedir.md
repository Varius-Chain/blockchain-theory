# Blockchain Nedir?

- Blockchain, verilerin **merkezi olmayan (decentralized)** bir ağ üzerinde, **şifrelenmiş bloklar** halinde saklandığı, değiştirilemez (immutable) bir dijital kayıt teknolojisidir. 

- En çok **Bitcoin** gibi kripto paralarla tanınsa da, finans, sağlık, tedarik zinciri, oy verme sistemleri gibi pek çok alanda kullanılmaktadır.

---

## 📌 Temel Özellikleri

1. **Blok Yapısı**  
   - Veriler bloklar halinde saklanır.  
   - Her blok, bir önceki bloğun **hash** değerini içerir. Zincir (chain) oluşur. 
   - Bu zincirleme yapı sayesinde veriler **değiştirilemez**.
   - Eğer bir bloktaki veri değiştirilirse hash değeri değişir ve zincir bozulur. Bu da verinin değiştirilmesini neredeyse imkânsız hâle getirir.

2. **Blockchain’in Yapısı**
   - **Blok (Block)** → İçinde veri (örneğin işlem bilgileri), kendi hash’i ve önceki bloğun hash’i bulunur.

   - **Hash** → Bloğun içeriğinin dijital imzası gibi çalışan, SHA-256 gibi algoritmalarla üretilen benzersiz karakter dizisidir.

   - **Zincir (Chain)**→ Blokların birbirine hash’lerle bağlanmasıyla oluşur.

   - **Dağıtık Ağ**(Distributed Network) → Tüm veritabanı tek bir yerde değil, ağdaki tüm katılımcılarda bulunur.

3. **Dağıtık Ağ (Distributed Network)**  
   - Veriler tek bir sunucuda değil, ağdaki **tüm katılımcılarda (node)** tutulur.  
   - Böylece tek bir noktaya saldırı sistemi çökertemez.

4. **Kriptografi ile Güvenlik**  
   - Veriler, **SHA-256** gibi algoritmalar ile şifrelenir.  
   - Yetkisiz değişiklik yapılamaz.

5. **Değiştirilemezlik (Immutability)**  
   - Bir blok eklendikten sonra değiştirmek için **tüm ağın onayı** gerekir.  
   - Bu da sahtecilik ihtimalini minimuma indirir.

---

## 🛠 Blockchain Nasıl Çalışır?

1. **İşlem Oluşturma** → Bir kullanıcı, ağa bir işlem gönderir.(ör. Ali → Ayşe 2 BTC gönderir).
2. **İşlem ağa yayılır** (peer-to-peer ağ).
3. **İşlemin Doğrulanması** → Ağdaki düğümler (nodes), işlemi doğrular.  
4. **Blok Oluşturma** → Doğrulanan işlemler yeni bir blokta toplanır.  
5. **Blok Zincire Eklenir** → Yeni blok, önceki bloğun hash’ini içererek zincire eklenir.  
6. **Güncel Kopya Yayılır** → Güncellenmiş blockchain, tüm düğümlere gönderilir.

---
## 📊 Basit Görsel Anlatım


Her blok bir önceki bloğun hash değerini içerir.  
Bu nedenle ortadaki bir bloğu değiştirirseniz, tüm zincir bozulur.

---

## 📌 Avantajları
- **Şeffaflık** → Herkes işlemleri görebilir.  
- **Güvenlik** → Kriptografi ile korunur.  
- **Merkeziyetsizlik** → Tek bir kontrol noktası yoktur.  
- **Değiştirilemezlik** → Veriler geriye dönük değiştirilemez.

---

## ⚠️ Dezavantajları
- **Enerji Tüketimi** → PoW sistemlerinde yüksek enerji kullanımı.  
- **İşlem Hızı** → Bazı blockchain ağlarında işlemler yavaş olabilir.  
- **Depolama Sorunu** → Zincir büyüdükçe veri boyutu artar.

---
## Kullanım Alanları
- Kripto paralar (Bitcoin, Ethereum)
- Akıllı sözleşmeler (Smart Contracts)
- Tedarik zinciri yönetimi
- Oylama sistemleri
- Dijital kimlik
- Veri güvenliği ve arşivleme

---
Blockchain, “herkesin görebildiği ama kimsenin silemediği bir defter” gibidir.
İşlemler kronolojik olarak eklenir, şifrelenir ve tüm ağda saklanır.
---

