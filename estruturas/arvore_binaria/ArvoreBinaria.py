class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def __str__(self):
        return str(self.data)
    

class BinaryTree:
    def __init__(self, data=None, node=None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None


    # Percurso em ordem simétrica (o correto é "inorder" em inglês)
    def inorder(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='') 
            self.inorder(node.left)
        print(node, end='')
        if node.right:
            self.inorder(node.right)
            print(')', end='')

    
    def postorder_traversal(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)
        


    def height(self, node=None):
        if node is None:
            node = self.root
        hleft = 0
        hright = 0
        if node.left:
            hleft = self.height(node.left)
        if node.right:
            hright = self.height(node.right)
        if hright > hleft:
            return hright + 1
        return hleft + 1
    

if __name__ == "__main__":
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

    tree.inorder()
    print()