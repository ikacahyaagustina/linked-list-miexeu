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
