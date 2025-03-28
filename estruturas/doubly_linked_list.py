# Implementação de uma lista duplamente encadeada

# Definição de um nó individual da lista
class Node:
    def __init__(self, data):
        # Cada nó contém um dado, um ponteiro para o nó anterior e um para o próximo
        self.data = data  # Armazena o dado do nó
        self.prev = None  # Aponta para o nó anterior (inicialmente None)
        self.next = None  # Aponta para o próximo nó (inicialmente None)

# Definição da lista duplamente encadeada
class DoublyLinkedList:
    def __init__(self):
        # Inicializa a lista com o head (cabeça) vazio
        self.head = None  # Head aponta para o primeiro nó da lista

    # Método para adicionar um novo nó ao final da lista
    def append(self, data):
        new_node = Node(data)  # Cria um novo nó com o dado fornecido
        if not self.head:
            # Se a lista estiver vazia, define o novo nó como o head
            self.head = new_node
            return
        # Caso a lista já tenha nós, percorre até o final
        last = self.head
        while last.next:
            last = last.next  # Move para o próximo nó até encontrar o último
        # Atualiza o último nó para apontar para o novo nó
        last.next = new_node
        # Configura o novo nó para apontar de volta para o último
        new_node.prev = last

    # Método para remover o primeiro nó com um valor específico
    def remove(self, data):
        # Começa a busca pelo head (cabeça) da lista
        node = self.head
        while node:
            if node.data == data:
                # Quando encontra o nó com o dado a ser removido
                if node.prev:
                    # Se não for o head, desconecta o nó anterior
                    node.prev.next = node.next
                else:
                    # Se for o head, atualiza o head para o próximo nó
                    self.head = node.next
                if node.next:
                    # Se houver um próximo nó, desconecta o nó atual do próximo
                    node.next.prev = node.prev
                return  # Sai do método após remover o nó
            node = node.next  # Move para o próximo nó na lista

    # Método para buscar um nó com um valor específico
    def search(self, data):
        # Começa a busca pelo head (cabeça) da lista
        node = self.head
        while node:
            if node.data == data:
                # Retorna o nó se encontrar o dado
                return node
            node = node.next  # Move para o próximo nó na lista
        return None  # Retorna None se não encontrar o valor

    # Método para exibir todos os elementos da lista
    def display(self):
        # Começa do head da lista
        node = self.head
        while node:
            # Exibe o dado do nó atual
            print(node.data, end=" <-> ")
            node = node.next  # Move para o próximo nó na lista
        print("None")  # Finaliza a exibição com None para indicar o final da lista

# Exemplo de uso da lista duplamente encadeada
dll = DoublyLinkedList()  # Cria uma nova lista duplamente encadeada
dll.append(1)  # Adiciona o valor 1 à lista
dll.append(2)  # Adiciona o valor 2 à lista
dll.append(3)  # Adiciona o valor 3 à lista

# Exibe a lista
dll.display()  # Esperado: 1 <-> 2 <-> 3 <-> None

# Remove o elemento 2 da lista
dll.remove(2)

# Exibe a lista após a remoção
dll.display()  # Esperado: 1 <-> 3 <-> None

# Busca pelo valor 3 na lista
result = dll.search(3)
if result:
    print("Elemento encontrado:", result.data)  # Esperado: Elemento encontrado: 3
else:
    print("Elemento não encontrado.")


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)

print(dll.head.data)
print(dll.head.next.data)
print(dll.head.next.next.data)
