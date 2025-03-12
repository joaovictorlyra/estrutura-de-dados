class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.filhos = []

    def adicionar_filho(self, nodo):
        self.filhos.append(nodo)

class ArvoreSimples:
    def __init__(self, raiz):
        self.raiz = Nodo(raiz)
    
    def imprimir(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz
        print("  " * nivel + str(nodo.valor))
        for filho in nodo.filhos:
            self.imprimir(filho, nivel + 1)

# Exemplo de uso
arvore = ArvoreSimples("Raiz")

nodo_a = Nodo("A")
nodo_b = Nodo("B")
nodo_c = Nodo("C")
nodo_d = Nodo("D")
nodo_e = Nodo("E")

arvore.raiz.adicionar_filho(nodo_a)
arvore.raiz.adicionar_filho(nodo_b)
nodo_a.adicionar_filho(nodo_c)
nodo_a.adicionar_filho(nodo_d)
nodo_b.adicionar_filho(nodo_e)

arvore.imprimir()
