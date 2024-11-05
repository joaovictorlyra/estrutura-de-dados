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

    def remove_last(self):
        if not self.head:  # Lista está vazia
            print("A lista já está vazia.")
            return
        if not self.head.next:  # Apenas um elemento na lista
            self.head = None
            return
        # Percorrer até o último nó
        last = self.head
        while last.next:
            last = last.next
        # Remover o último nó
        last.prev.next = None

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
dll.display()  

dll.remove_last()
print("Lista após remover o último elemento:")
dll.display() 

dll.remove_last()
print("Lista após remover o último elemento novamente:")
dll.display()  

dll.remove_last()
print("Lista após remover o último elemento de uma lista com um único elemento:")
dll.display()  

dll.remove_last()  
