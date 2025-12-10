
# PROGRAM STRUKTUR DATA PYTHON

from collections import deque

# 1. ARRAY

class ArrayDemo:
    def _init_(self):
        self.arr = []

    def add(self, data):
        self.arr.append(data)

    def remove(self, index):
        if 0 <= index < len(self.arr):
            del self.arr[index]

    def search(self, data):
        if data in self.arr:
            return self.arr.index(data)
        return -1

    def show(self):
        print("Array :", self.arr)


# 2. STACK (LIFO)

class StackDemo:
    def _init_(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None

    def show(self):
        print("Stack :", self.stack)


# 3. QUEUE (FIFO)

class QueueDemo:
    def _init_(self):
        self.queue = deque()

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def peek(self):
        if self.queue:
            return self.queue[0]
        return None

    def show(self):
        print("Queue :", list(self.queue))


# 4. LINKED LIST

class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

class LinkedListDemo:
    def _init_(self):
        self.head = None

    def add_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_back(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def remove(self, data):
        cur = self.head
        prev = None
        while cur:
            if cur.data == data:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                return True
            prev = cur
            cur = cur.next
        return False

    def count(self):
        cur = self.head
        total = 0
        while cur:
            total += 1
            cur = cur.next
        return total

    def show(self):
        cur = self.head
        print("Linked List :", end=" ")
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")


# 5. DICTIONARY (HASH MAP)

class DictDemo:
    def _init_(self):
        self.map = {}

    def add(self, key, value):
        self.map[key] = value

    def update(self, key, value):
        if key in self.map:
            self.map[key] = value

    def remove(self, key):
        if key in self.map:
            del self.map[key]

    def show(self):
        print("Dictionary :", self.map)


# 6. SET

class SetDemo:
    def _init_(self):
        self.s = set()

    def add(self, data):
        self.s.add(data)

    def remove(self, data):
        if data in self.s:
            self.s.remove(data)

    def exists(self, data):
        return data in self.s

    def show(self):
        print("Set :", self.s)


# MENU UTAMA

def main():
    array = ArrayDemo()
    stack = StackDemo()
    queue = QueueDemo()
    linked = LinkedListDemo()
    diction = DictDemo()
    sset = SetDemo()

    while True:
        print("""

      PROGRAM STRUKTUR DATA
1. Array
2. Stack
3. Queue
4. Linked List
5. Dictionary
6. Set
7. Keluar
        """)

        pilihan = input("Pilih menu (1-7): ")

        # ARRAY
        
        if pilihan == "1":
            print("\n--- ARRAY ---")
            print("t=Tambah | h=Hapus | c=Cari | l=Lihat")
            pilih = input("Menu: ")

            if pilih == "t":
                array.add(input("Data: "))
            elif pilih == "h":
                array.remove(int(input("Index: ")))
            elif pilih == "c":
                data = input("Cari data: ")
                pos = array.search(data)
                print("Ditemukan di index:", pos if pos != -1 else "Tidak ada")
            
            array.show()

        # STACK
        
        elif pilihan == "2":
            print("\n--- STACK ---")
            print("p=Push | o=Pop | k=Peek | l=Lihat")
            pilih = input("Menu: ")

            if pilih == "p":
                stack.push(input("Data: "))
            elif pilih == "o":
                print("Pop:", stack.pop())
            elif pilih == "k":
                print("Elemen teratas:", stack.peek())

            stack.show()

        # QUEUE
        
        elif pilihan == "3":
            print("\n--- QUEUE ---")
            print("e=Enqueue | d=Dequeue | p=Peek | l=Lihat")
            pilih = input("Menu: ")

            if pilih == "e":
                queue.enqueue(input("Data: "))
            elif pilih == "d":
                print("Dequeue:", queue.dequeue())
            elif pilih == "p":
                print("Elemen depan:", queue.peek())

            queue.show()

        # LINKED LIST
        
        elif pilihan == "4":
            print("\n--- LINKED LIST ---")
            print("d=Tambah Depan | b=Tambah Belakang | h=Hapus | j=Jumlah | l=Lihat")
            pilih = input("Menu: ")

            if pilih == "d":
                linked.add_front(input("Data: "))
            elif pilih == "b":
                linked.add_back(input("Data: "))
            elif pilih == "h":
                linked.remove(input("Data dihapus: "))
            elif pilih == "j":
                print("Jumlah node:", linked.count())

            linked.show()

        # DICTIONARY
        
        elif pilihan == "5":
            print("\n--- DICTIONARY ---")
            print("t=Tambah | u=Update | h=Hapus | l=Lihat")
            pilih = input("Menu: ")

            if pilih == "t":
                diction.add(input("Key: "), input("Value: "))
            elif pilih == "u":
                diction.update(input("Key: "), input("Value baru: "))
            elif pilih == "h":
                diction.remove(input("Key dihapus: "))

            diction.show()

        # SET
        
        elif pilihan == "6":
            print("\n--- SET ---")
            print("t=Tambah | h=Hapus | c=Cek | l=Lihat")
            pilih = input("Menu: ")

            if pilih == "t":
                sset.add(input("Data: "))
            elif pilih == "h":
                sset.remove(input("Data dihapus: "))
            elif pilih == "c":
                data = input("Cek data: ")
                print("Ada" if sset.exists(data) else "Tidak ada")

            sset.show()

        # KELUAR
        elif pilihan == "7":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!\n")


# Jalankan program
main()