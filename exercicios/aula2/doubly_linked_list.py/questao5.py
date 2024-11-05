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

    def remove_duplicates(self):
        current = self.head
        seen = set()  # Conjunto para armazenar os valores já encontrados
        while current:
            if current.data in seen:
                next_node = current.next  # Armazena o próximo nó
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # Se o nó atual é o head, atualiza o head
                    self.head = current.next
                current = next_node  # Continua com o próximo nó
            else:
                seen.add(current.data)
                current = current.next  # Move para o próximo nó

    def display(self):
        node = self.head
        while node:
            print(node.data, end=" <-> ")
            node = node.next
        print("None")

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(2)
dll.append(3)
dll.append(1)

print("Lista original:")
dll.display()  # Saída esperada: 1 <-> 2 <-> 2 <-> 3 <-> 1 <-> None

dll.remove_duplicates()

print("Lista após remover duplicatas:")
dll.display()  # Saída esperada: 1 <-> 2 <-> 3 <-> None
