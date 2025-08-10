# Akıllı Kontratlar (Smart Contracts)

---

## Akıllı Kontrat Nedir?

Akıllı kontratlar, blok zincir üzerinde çalışan, belirli koşullar sağlandığında otomatik olarak işlem yapan dijital sözleşmelerdir. İnsan müdahalesi olmadan, önceden programlanmış kurallar doğrultusunda çalışan kod parçacıklarıdır.

> “Akıllı kontratlar, aracılara olan ihtiyacı ortadan kaldırarak işlemleri hızlı, güvenli ve şeffaf hale getirir.”

---

## Akıllı Kontratların Temel Özellikleri

- **Otomasyon:** Koşullar sağlandığında otomatik tetiklenir.  
- **Değiştirilemezlik:** Blok zincire eklendikten sonra kodu değiştirmek mümkün değildir.  
- **Şeffaflık:** Ağdaki tüm kullanıcılar kontrat kodunu görebilir.  
- **Güvenlik:** Kriptografik yapılar sayesinde güvenli ve doğrulanabilir.  

---

## Akıllı Kontratların Çalışma Prensibi

1. **Kodlama:** Solidity gibi diller kullanılarak kontrat yazılır.  
2. **Dağıtım (Deploy):** Ethereum gibi bir blok zincirine yüklenir.  
3. **İşletim:** Koşullar sağlandığında kontrat içerisindeki fonksiyonlar otomatik çalışır.  
4. **Kayıt:** İşlemler blok zincirine kaydedilir ve herkes tarafından doğrulanabilir.  

---

## Akıllı Kontratların Kullanım Alanları

- **Finansal Hizmetler (DeFi):** Kredi verme, borçlanma, sigorta, varlık yönetimi.  
- **Tedarik Zinciri:** Ürün takibi ve doğrulama süreçleri.  
- **Oylama Sistemleri:** Şeffaf ve güvenli dijital oy kullanma.  
- **Gayrimenkul:** Otomatik tapu transferleri ve kiralama sözleşmeleri.  
- **Oyunlar ve NFT:** Dijital varlıkların yönetimi ve ticareti.  

---

## Örnek Solidity Akıllı Kontratı

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleStorage {
    uint256 private data;

    // Veri kaydetme fonksiyonu
    function set(uint256 _data) public {
        data = _data;
    }

    // Veri okuma fonksiyonu
    function get() public view returns (uint256) {
        return data;
    }
}
```

---

## Akıllı Kontratların Avantajları ve Dezavantajları

| Avantajları                      | Dezavantajları                      |
| -------------------------------- | ----------------------------------- |
| Merkeziyetsiz, güvenli ve şeffaf | Kod hataları düzeltilmesi zor       |
| Otomatik, hızlı ve maliyet etkin | Yüksek işlem (gas) ücretleri        |
| Aracı gerektirmez                | Karmaşık iş mantığı zor uygulanır   |
| Herkes tarafından doğrulanabilir | Blok zincir üzerindeki sınırlamalar |

---

## Popüler Akıllı Kontrat Programlama Dilleri

- **Solidity:** Ethereum ekosisteminde en yaygın kullanılan dil.  
- **Vyper:** Güvenlik ve basitliğe odaklanmış Python benzeri dil.  
- **Rust:** Solana ve Polkadot gibi zincirlerde tercih edilir.  
- **JavaScript, Go, C++:** Bazı platformlarda desteklenen diğer diller.  

