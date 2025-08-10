# Solidity Eğitimi – Başlangıçtan İleri Seviyeye

---

## 1. Giriş

Solidity, Ethereum ve diğer EVM uyumlu blok zincirlerinde akıllı kontratlar geliştirmek için kullanılan en popüler programlama dilidir. JavaScript, C++ ve Python’a benzer sözdizimi sayesinde öğrenmesi görece kolaydır.

---

## 2. Temel Kavramlar ve Sürüm Belirtme

```solidity
// SPDX Lisansı ve Sürüm Belirtme
// Bu satırlar, kodun lisansını ve Solidity sürümünü belirtir (MIT, GPL, vb)
// pragma: Derleyiciye hangi sürümle uyumlu olduğunu söyler
// ^ işareti: belirtilen sürüm ve sonrası için geçerli
pragma solidity ^0.8.17;
```

---

## 3. Kontrat Oluşturma

```solidity
// Basit bir kontrat örneği
contract MerhabaDunya {
    // Değişken ve fonksiyonlar buraya yazılır
}
```

---

## 4. Veri Tipleri ve Değişkenler

- **Temel Tipler:**  
  - `uint` / `uint256`: İşaretsiz tam sayı (0 ve pozitif tam sayılar)  
  - `int` / `int256`: İşaretli tam sayı (pozitif ve negatif)  
  - `bool`: Boolean (true/false)  
  - `address`: Ethereum adresi  
  - `string`: Metin dizisi  
  - `bytes`: Bayt dizisi  

- **Değişken Tanımlama Örnekleri:**

```solidity
uint256 public sayi = 10;
bool public aktifMi = true;
address public sahibi;
string public mesaj = "Merhaba, Solidity!";
```

---

## 5. Fonksiyonlar

### 5.1 Fonksiyon Tanımı ve Çağrılması

```solidity
function setSayi(uint256 _sayi) public {
    sayi = _sayi;
}

function getSayi() public view returns (uint256) {
    return sayi;
}
```

- `public`: Fonksiyon herkes tarafından çağrılabilir.  
- `view`: Fonksiyon sadece veri okur, blok zincirine yazmaz.

---

## 6. Erişim Belirleyiciler

| Belirleyici | Açıklama                                  |
|-------------|-------------------------------------------|
| `public`    | Herkese açık                              |
| `private`   | Sadece kontrat içinde erişilebilir        |
| `internal`  | Kontrat ve kalıtım alan kontratlardan erişilebilir |
| `external`  | Sadece kontrat dışından erişilebilir      |

---

## 7. Yapıcı Fonksiyon (Constructor)

Kontrat deploy edildiğinde sadece bir kez çalışır.

```solidity
constructor() {
    sahibi = msg.sender; // Kontratı dağıtan adresi sahibi olarak atar
}
```

---

## 8. Olaylar (Events) ve Loglama

Kontrattan dış dünyaya bilgi göndermek için kullanılır.

```solidity
event SayıDegisti(uint256 yeniSayi);

function setSayi(uint256 _sayi) public {
    sayi = _sayi;
    emit SayıDegisti(_sayi); // Olay tetiklenir
}
```

---

## 9. Koşullar ve Döngüler

### 9.1 If-Else

```solidity
if (sayi > 100) {
    // Kod bloğu
} else {
    // Alternatif kod bloğu
}
```

### 9.2 For Döngüsü

```solidity
for (uint i = 0; i < 10; i++) {
    // Döngü içi kod
}
```

---

## 10. Basit Solidity Kontratı – Sayı Depolama

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract SayıDepo {
    uint256 private sayi;
    address public sahibi;

    event SayıDegisti(uint256 yeniSayi);

    constructor() {
        sahibi = msg.sender;
    }

    modifier sadeceSahibi() {
        require(msg.sender == sahibi, "Yetkiniz yok!");
        _;
    }

    function setSayi(uint256 _sayi) public sadeceSahibi {
        sayi = _sayi;
        emit SayıDegisti(_sayi);
    }

    function getSayi() public view returns (uint256) {
        return sayi;
    }
}
```

---

## 11. İleri Konular

- Miras (Inheritance)  
- Modifiers (Fonksiyon koşulları)  
- Arayüzler (Interfaces)  
- Kütüphaneler (Libraries)  
- Hata Yönetimi ve Geri Dönüşler (Error Handling)  
- Gas ve Optimizasyon  

---

## 12. Geliştirme Araçları

- **Remix IDE:** Tarayıcı tabanlı Solidity geliştirme ortamı (https://remix.ethereum.org)  
- **Truffle:** Akıllı kontrat geliştirme ve test framework’ü  
- **Hardhat:** Modern Ethereum geliştirme ortamı  
- **Ganache:** Yerel blockchain simülatörü  

---

> *Bu eğitim, Solidity’ye yeni başlayanlar ve temel bilgilerini pekiştirmek isteyenler için hazırlanmıştır. İleri seviye konular için resmi dokümanlar ve kaynaklar önerilmektedir.*
