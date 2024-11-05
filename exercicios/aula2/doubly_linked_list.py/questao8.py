class SinglyNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = SinglyNode(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        node = self.head
        while node:
            print(node.data, end=" -> ")
            node = node.next
        print("None")

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

    def display(self):
        node = self.head
        while node:
            print(node.data, end=" <-> ")
            node = node.next
        print("None")

    def to_singly_linked(self):
        singly_linked_list = SinglyLinkedList()
        node = self.head
        while node:
            singly_linked_list.append(node.data)  # Adiciona o dado à nova lista
            node = node.next  # Move para o próximo nó na lista duplamente encadeada
        return singly_linked_list

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)

print("Lista duplamente encadeada:")
dll.display()  # Saída esperada: 1 <-> 2 <-> 3 <-> None

sll = dll.to_singly_linked()

print("Lista simplesmente encadeada:")
sll.display()  # Saída esperada: 1 -> 2 -> 3 -> None
