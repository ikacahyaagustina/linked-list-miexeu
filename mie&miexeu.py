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
