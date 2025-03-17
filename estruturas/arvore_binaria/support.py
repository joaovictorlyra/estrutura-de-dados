from ArvoreBinaria import ArvoreBinaria, Node

if __name__ == "__main__":
    tree = ArvoreBinaria(7)
    tree.root.left = Node(18)
    tree.root.right = Node(14)

    print(tree.root)
    print