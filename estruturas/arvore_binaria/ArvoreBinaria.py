class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def __str__(self):
        return str(self.data)
    
# Letra A:
"""Letra A: Define a classe da árvore binária."""
class BinaryTree:
    def __init__(self, data=None, node=None):
        """(Letra A) Inicializa a árvore binária com dado ou nó inicial."""
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # Letra C:
    def node_degree(self, node):
        """(Letra C) Retorna o grau (número de filhos) de um nó específico."""
        degree = 0
        if node.left:
            degree += 1
        if node.right:
            degree += 1
        return degree

    # Letra D:
    def tree_degree(self, node=None):
        """(Letra D) Retorna o grau máximo da árvore, comparando o grau do nó com os graus das subárvores."""
        if node is None:
            node = self.root
        if node is None:
            return 0
        left_degree = self.tree_degree(node.left) if node.left else 0
        right_degree = self.tree_degree(node.right) if node.right else 0
        return max(self.node_degree(node), left_degree, right_degree)

    # Letras E e F:
    def report_node_depth(self, value):
        """(Letras E e F) Exibe a profundidade do nó com o valor informado, utilizando node_depth."""
        depth = self.node_depth(self.root, value)
        print(f"Profundidade do nó '{value}':", depth)

    # Letra G:
    def detailed_node_info(self, value):
        """(Letra G) Exibe informações detalhadas do nó: mostra nó pai, irmãos, tios e se é filho esquerdo ou direito."""
        node, parent = self._search_with_parent(self.root, value)
        if node is None:
            print(f"Nó com valor {value} não encontrado.")
            return
        info = {}
        info["nó"] = node.data
        if parent:
            info["nó pai"] = parent.data
            if parent.left == node:
                info["posição"] = "filho esquerdo"
            elif parent.right == node:
                info["posição"] = "filho direito"
            siblings = []
            if parent.left and parent.left != node:
                siblings.append(parent.left.data)
            if parent.right and parent.right != node:
                siblings.append(parent.right.data)
            info["irmãos"] = siblings
            gp = self._search_with_parent(self.root, parent.data)[1]
            uncles = []
            if gp:
                if gp.left and gp.left != parent:
                    uncles.append(gp.left.data)
                if gp.right and gp.right != parent:
                    uncles.append(gp.right.data)
            info["tios"] = uncles
        else:
            info["nó pai"] = None
            info["posição"] = None
            info["irmãos"] = []
            info["tios"] = []
        print(info)

    def _search_with_parent(self, node, value, parent=None):
        """Função auxiliar que busca um nó pelo valor e retorna uma tupla (nó, pai)."""
        if node is None:
            return None, None
        if node.data == value:
            return node, parent
        left_result = self._search_with_parent(node.left, value, node)
        if left_result[0] is not None:
            return left_result
        return self._search_with_parent(node.right, value, node)

    # Letra H:
    def node_height(self, node):
        """(Letra H) Calcula a altura do nó, definida como a maior distância até uma folha."""
        if node is None:
            return 0
        hleft = self.node_height(node.left)
        hright = self.node_height(node.right)
        return max(hleft, hright) + 1  # Retorna o maior valor entre a esquerda e a direita e soma mais 1

    # Letra I:
    def tree_height(self, node=None):
        """(Letra I) Retorna a altura da árvore a partir de um nó, considerando o caminho até a folha mais distante."""
        if node is None:
            node = self.root
        hleft = -1
        hright = -1
        if node.left:
            hleft = self.tree_height(node.left)
        if node.right:
            hright = self.tree_height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1

    # Letra J:
    def node_level(self, raiz, node, nivel=0):
        """(Letra J) Retorna o nível (profundidade) de um nó a partir da raiz fornecida."""
        if raiz is None:
            return -1
        if raiz == node:
            return nivel
        l_left = self.node_level(raiz.left, node, nivel + 1)
        if l_left != -1:
            return l_left
        l_right = self.node_level(raiz.right, node, nivel + 1)
        return l_right

    # Letra K:
    def tree_level(self, node=None):
        """(Letra K) Retorna o nível máximo da árvore, calculando os níveis dos sub-nós."""
        if node is None:
            node = self.root
        l_left = -1
        l_right = -1
        if node.left:
            l_left = self.tree_level(node.left)
        if node.right:
            l_right = self.tree_level(node.right)
        if l_right > l_left:
            return l_right + 1
        return l_left + 1

    # Letra M:
    def print_hierarchical(self, node=None, indent="", last=True):
        """(Letra M) Imprime a árvore em formato hierárquico, usando caracteres gráficos para definir a estrutura."""
        if node is None:
            node = self.root
        print(indent, end="")
        if last:
            print("└─", end="")
            indent += "  "
        else:
            print("├─", end="")
            indent += "│ "
        print(node.data)
        children = []
        if node.left:
            children.append(node.left)
        if node.right:
            children.append(node.right)
        for i, child in enumerate(children):
            is_last = (i == len(children) - 1)
            self.print_hierarchical(child, indent, is_last)

    # Letra L:
    def leaf_nodes(self, node=None):
        """(Letra L) Retorna uma lista com os dados dos nós folha (sem filhos) da árvore."""
        if node is None:
            node = self.root
        if node is None:
            return []
        leaves = []
        if not node.left and not node.right:
            leaves.append(node.data)
        else:
            if node.left:
                leaves.extend(self.leaf_nodes(node.left))
            if node.right:
                leaves.extend(self.leaf_nodes(node.right))
        return leaves

    # Letra N:
    def preorder(self, node=None):
        """(Letra N) Realiza a travessia em pré-ordem, imprimindo os dados dos nós."""
        if node is None:
            node = self.root
        print(node, end=' ')
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)

    # Letra O:
    def postorder_traversal(self, node=None):
        """(Letra O) Realiza a travessia em pós-ordem, imprimindo os dados dos nós."""
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)

    # Letra P:
    def inorder(self, node=None):
        """(Letra P) Realiza a travessia em ordem (inorder), imprimindo os dados dos nós."""
        if node is None:
            node = self.root
        if node.left:
            print('(', end='') 
            self.inorder(node.left)
        print(node, end='')
        if node.right:
            self.inorder(node.right)
            print(')', end='')

    def node_sheet(self, node):
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        left = self.node_sheet(node.left)
        right = self.node_sheet(node.right)

        return left + right

    def tree_depth(self, root):
        if root is None:
            return 0

        left_depth = self.tree_depth(root.left)
        right_depth = self.tree_depth(root.right)

        return max(left_depth, right_depth) + 1
    
    def node_depth(self, root, value):
        def search(node, value, depth):
            if node is None:
                return -1  
            if node.data == value:
                return depth
            return max(search(node.left, value, depth + 1), 
                       search(node.right, value, depth + 1))
        
        return search(root, value, 0)


if __name__ == "__main__":
    # LETRA B:
    # Criando os nós da árvore binária
    tree = BinaryTree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')

    # Construindo a árvore binária
    tree.root = n2
    n2.left = n1
    n2.right = n3
    n3.left = n4
    n3.right = n5
    n5.left = n6
    n5.right = n7

