from collections import deque

# Questão 1:
array = [10, 20, 30, 40, 50]

array.remove(10)

array.remove(50)

print(array)

#-------------------------------

pilha = []

pilha.append(10)
pilha.append(20)
pilha.append(30)
pilha.append(40)
pilha.append(50)

pilha.pop()
pilha.remove(pilha[0])

print(pilha)

#Questão 2:
pilha = []

pilha.append(100)
pilha.append(200)
pilha.append(300)
pilha.append(400)
pilha.append(500)

pilha.pop()
pilha.pop()

print(pilha)

#--------------------------------
array = [100, 200, 300, 400, 500]

array.remove(array[-1])
array.remove(array[-1])

print(array)

#Questão 3:
fila = deque(["A", "B", "C", "D", "E"])
fila.remove(fila[0])

fila.append("F")
print(fila)

#-----------------------------------------------
pilha1 = []

pilha1.append("A")
pilha1.append("B")
pilha1.append("C")
pilha1.append("D")
pilha1.append("E")

pilha1.remove(pilha1[0])
pilha1.append("F")
print(pilha1)


#Questão 4:
class Node:  # Define a classe Node, que representa cada nó individual na lista ligada.
    def __init__(self, data):  # Método inicializador para a classe Node.
        self.data = data  # Armazena o valor do nó, passado como argumento no momento da criação.
        self.next = None  # Inicializa o próximo nó como None, pois este nó não está ligado a outro ainda.

class LinkedList:  # Define a classe LinkedList, que representa a lista ligada em si.
    def __init__(self):  # Método inicializador para a classe LinkedList.
        self.head = None  # Define o atributo head, que representa o primeiro nó da lista. Inicia como None, indicando uma lista vazia.

    def append(self, data):  # Método para adicionar um novo nó ao final da lista.
        new_node = Node(data)  # Cria uma nova instância da classe Node com o valor passado.
        if not self.head:  # Verifica se a lista está vazia (head é None).
            self.head = new_node  # Se estiver vazia, head aponta para o new_node, que é agora o primeiro nó.
            return  # Sai do método, pois o novo nó foi adicionado como head.

        last = self.head  # Cria uma referência ao primeiro nó (head) para começar a busca pelo final da lista.
        while last.next:  # Loop para encontrar o último nó, onde last.next será None.
            last = last.next  # Move para o próximo nó até encontrar o último (onde last.next é None).

        last.next = new_node  # Define o atributo next do último nó como o novo nó, conectando-o ao final da lista.

    def display(self):  # Método para exibir os elementos da lista.
        node = self.head  # Começa no primeiro nó da lista.
        while node:  # Loop enquanto houver um nó (node não é None).
            print(node.data, end=" -> ")  # Imprime o valor do nó atual seguido de " -> " para indicar a ligação.
            node = node.next  # Move para o próximo nó.
        print("None")  # Indica o final da lista com "None".

    def remove(self, data):  # Método para remover um nó com um valor específico.
            # Caso especial: o nó a ser removido está no início (é o head).
            if self.head and self.head.data == data:  # Verifica se a lista não está vazia e se o head contém o valor.
                self.head = self.head.next  # Atualiza o head para o próximo nó, removendo o primeiro nó.
                return  # Sai do método pois a remoção foi concluída.

            current = self.head  # Começa no primeiro nó para procurar o valor a ser removido.
            previous = None  # 'previous' é o nó que precede o 'current' e será usado para ajustar a ligação ao remover.

            # Loop para encontrar o nó com o valor especificado
            while current and current.data != data:  # Continua enquanto current não é None e o valor não é encontrado.
                previous = current  # Atualiza o previous para o current.
                current = current.next  # Move current para o próximo nó.

            # Se o nó foi encontrado (current não é None)
            if current:  # Verifica se o nó com o valor foi encontrado.
                previous.next = current.next  # 'Pula' o nó atual, ligando o nó anterior ao próximo do atual.
            else:
                print("Valor não encontrado na lista.")  # Exibe uma mensagem se o valor não estiver na lista.

# Exemplo de uso
ll = LinkedList()  
ll.append(11)  
ll.append(22)  
ll.append(33)  
ll.append(44)  
ll.append(55) 

ll.remove(11)
ll.remove(55)
ll.display()

#-----------------------------
pilha2 = []

pilha2.append(11)
pilha2.append(22)
pilha2.append(32)
pilha2.append(44)
pilha2.append(55)

pilha2.pop()
pilha2.remove(pilha2[0])

print(pilha2)