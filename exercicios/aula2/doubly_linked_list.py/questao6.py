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

    def prepend(self, data):
        new_node = Node(data)  # Cria um novo nó com o dado fornecido
        if self.head:  # Se a lista não está vazia
            new_node.next = self.head  # O próximo do novo nó será o atual head
            self.head.prev = new_node  # O anterior do head atual será o novo nó
        self.head = new_node  # Atualiza o head para o novo nó

    def display(self):
        node = self.head
        while node:
            print(node.data, end=" <-> ")
            node = node.next
        print("None")

dll = DoublyLinkedList()
dll.append(2)
dll.append(3)

print("Lista original:")
dll.display()  # Saída esperada: 2 <-> 3 <-> None

dll.prepend(1)

print("Lista após inserção no início:")
dll.display()  # Saída esperada: 1 <-> 2 <-> 3 <-> None
