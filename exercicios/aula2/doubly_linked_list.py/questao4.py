class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def count(self, data):
        current = self.head
        count = 0
        while current:
            if current.data == data:
                count += 1
            current = current.next
        return count

    def display(self):
        node = self.head
        while node:
            print(node.data, end=" <-> ")
            node = node.next
        print("None")

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(1)
dll.append(3)
dll.append(1)

print("Lista:")
dll.display()  # Saída esperada: 1 <-> 2 <-> 1 <-> 3 <-> 1 <-> None

count_1 = dll.count(1)
print("O valor 1 aparece:", count_1, "vezes")  # Saída esperada: O valor 1 aparece: 3 vezes
