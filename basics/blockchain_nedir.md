# Blockchain Nedir?

Blockchain, verilerin **merkezi olmayan (decentralized)** bir ağ üzerinde, **şifrelenmiş bloklar** halinde saklandığı, değiştirilemez (immutable) bir dijital kayıt teknolojisidir.  
En çok **Bitcoin** gibi kripto paralarla tanınsa da, finans, sağlık, tedarik zinciri, oy verme sistemleri gibi pek çok alanda kullanılmaktadır.

---

## 📌 Temel Özellikleri

1. **Blok Yapısı**  
   - Veriler bloklar halinde saklanır.  
   - Her blok, bir önceki bloğun **hash** değerini içerir.  
   - Bu zincirleme yapı sayesinde veriler **değiştirilemez**.

2. **Dağıtık Ağ (Distributed Network)**  
   - Veriler tek bir sunucuda değil, ağdaki **tüm katılımcılarda (node)** tutulur.  
   - Böylece tek bir noktaya saldırı sistemi çökertemez.

3. **Kriptografi ile Güvenlik**  
   - Veriler, **SHA-256** gibi algoritmalar ile şifrelenir.  
   - Yetkisiz değişiklik yapılamaz.

4. **Değiştirilemezlik (Immutability)**  
   - Bir blok eklendikten sonra değiştirmek için **tüm ağın onayı** gerekir.  
   - Bu da sahtecilik ihtimalini minimuma indirir.

---

## 🛠 Blockchain Nasıl Çalışır?

1. **İşlem Oluşturma** → Bir kullanıcı, ağa bir işlem gönderir.  
2. **İşlemin Doğrulanması** → Ağdaki düğümler (nodes), işlemi doğrular.  
3. **Blok Oluşturma** → Doğrulanan işlemler yeni bir blokta toplanır.  
4. **Blok Zincire Eklenir** → Yeni blok, önceki bloğun hash’ini içererek zincire eklenir.  
5. **Güncel Kopya Yayılır** → Güncellenmiş blockchain, tüm düğümlere gönderilir.

---

## 📊 Basit Görsel Anlatım

<img width="675" height="723" alt="image" src="https://github.com/user-attachments/assets/8df1dd99-1fab-41b5-8ae9-b1a207f814d2" />
