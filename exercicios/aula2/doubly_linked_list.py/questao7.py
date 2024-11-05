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

    def swap(self, data1, data2):
        if data1 == data2:  # Se os dados são iguais, não é necessário trocar
            return

        # Encontra o primeiro nó que contém data1
        node1 = self.head
        while node1 and node1.data != data1:
            node1 = node1.next

        node2 = self.head
        while node2 and node2.data != data2:
            node2 = node2.next

        if not node1 or not node2:
            return  # Se qualquer um dos nós não for encontrado, não faz nada

        if node1.prev:
            node1.prev.next = node2
        else:
            self.head = node2  # Se node1 era o head, atualiza o head para node2

        if node1.next:
            node1.next.prev = node2

        if node2.prev:
            node2.prev.next = node1
        else:
            self.head = node1  # Se node2 era o head, atualiza o head para node1

        if node2.next:
            node2.next.prev = node1

        node1.next, node2.next = node2.next, node1.next
        node1.prev, node2.prev = node2.prev, node1.prev

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)

print("Lista original:")
dll.display()  # Saída esperada: 1 <-> 2 <-> 3 <-> 4 <-> None

dll.swap(2, 4)

print("Lista após swap(2, 4):")
dll.display()  # Saída esperada: 1 <-> 4 <-> 3 <-> 2 <-> None
