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

    def reverse(self):
        current = self.head
        prev_node = None

        while current:
            # Troca de next e prev para o nó atual
            next_node = current.next
            current.next = prev_node
            current.prev = next_node
            
            # Move os ponteiros prev_node e current para frente
            prev_node = current
            current = next_node
        
        # Define o novo head da lista
        self.head = prev_node

    def display(self):
        node = self.head
        while node:
            print(node.data, end=" <-> ")
            node = node.next
        print("None")

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
print("Lista original:")
dll.display()  # Saída esperada: 1 <-> 2 <-> 3 <-> None

dll.reverse()
print("Lista após a inversão:")
dll.display()  # Saída esperada: 3 <-> 2 <-> 1 <-> None
