class Node:
    def __init__(self, menu, harga):
        self.menu = menu
        self.harga = harga
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def masukan_pesanan(self, menu, harga):
        if not self.head:
            self.head = Node(menu, harga)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(menu, harga)

def tampilkan_pesanan(self):
    if not self.head:
        print("keranjang kosong")
        return
    current = self.head
    count = 1
        while current:
        print(f"{count}. {current.menu} {current.harga} rupiah")
        current = current.next
        count += 1

def total_biaya(self):
    total = 0
    current = self.head
    while current:
        total += current.harga
        current = current.next
    return total
menu_miexue = {
    "miexue ice cream": 5000,
    "boba shake": 16000,
    "mi sundae": 14000,
    "mi ganas": 11000,
    "creamy mango boba": 22000
}
keranjang = LinkedList()

while True:
    print("\nMenu:")
    print("1. Tambah pesanan ke keranjang")
    print("2. Tambah pesanan yang sudah")
    print("3. Jumlah Harga yang dibayarkan")
    print("4. Keluar")
    pilihan = input("pilihan menu: ")


