import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        """
        Blok yapısı:
        - index: blok sırası
        - timestamp: oluşturulma zamanı
        - data: blok içeriği (işlemler vs.)
        - previous_hash: önceki bloğun hash değeri
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Blok hash'i hesaplama fonksiyonu.
        Blok içeriğinin SHA-256 hash'ini oluşturur.
        """
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        """
        Blockchain başlatma:
        - zincire genesis (ilk) bloğu ekler
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Genesis bloğu oluşturur.
        Genellikle index=0, önceki hash "0" olur.
        """
        return Block(0, time.time(), "Genesis Block", "0")

    def get_latest_block(self):
        """
        Zincirin en son bloğunu döner.
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Yeni blok ekleme:
        - önceki bloğun hash'ini yeni bloğa atar
        - bloğun hash'ini tekrar hesaplar
        - zincire ekler
        """
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        """
        Zincir doğrulama:
        - her blok için
            - hash doğru mu?
            - önceki blok hash'i eşleşiyor mu?
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            if current.hash != current.calculate_hash():
                print(f"Blok {i} hash'i geçersiz!")
                return False

            if current.previous_hash != previous.hash:
                print(f"Blok {i} önceki hash ile eşleşmiyor!")
                return False

        return True


# Örnek kullanım
if __name__ == "__main__":
    my_blockchain = Blockchain()

    # Yeni bloklar ekleyelim
    my_blockchain.add_block(Block(1, time.time(), {"amount": 4}, ""))
    my_blockchain.add_block(Block(2, time.time(), {"amount": 10}, ""))

    # Zinciri kontrol edelim
    print("Blockchain geçerli mi?", my_blockchain.is_chain_valid())

    # Zinciri yazdıralım
    for block in my_blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print("-" * 30)
