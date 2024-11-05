# #Questão 1:

    # Adição de Elementos em Diferentes Posições

    # Modifique o método append ou crie um novo método chamado insert_at_position(data,
    # position) para adicionar um nó em uma posição específica da lista.

        # Exemplo: Se a lista for 1 <-> 2 <-> 3 e chamarmos insert_at_position(5, 2), o resultado deve ser 1
        # <-> 5 <-> 2 <-> 3.


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

    def insert_at_position(self, data, position):
        new_node = Node(data)
        # Inserir no início se a posição for 0
        if position == 0:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
            return

        # Percorrer até a posição desejada ou o final da lista
        current = self.head
        current_position = 0
        while current and current_position < position:
            current_position += 1
            if current_position == position:
                # Inserir no meio da lista
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

        # Caso a posição seja maior que o comprimento, inserir no final
        if not current:
            self.append(data)





