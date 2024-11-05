# ----------------- Questões 1 e 2 -------------------

pares = {2, 4, 6, 8, 10}
impares = {1, 3, 5, 7, 9}

print("----------------- Questões 1 e 2 -------------------")
print("\nPares: ", pares)
print("Impares: ", impares)

uniao = pares | impares
print("Uniao: ", uniao)


print("O conjunto final é a união dos dois conjuntos criados anteriormente.")
print("Resultado da operação: Uniao: ", uniao, "\n")

# ----------------- Questões 3 e 4 -------------------

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

interseccao = A & B

print("----------------- Questões 3 e 4 -------------------")


print("\nInterseção: ", interseccao)

diferenca_A_B = A - B
diferenca_B_A = B - A
print("Diferença (A - B): ", diferenca_A_B)
print("Diferença (B - A): ", diferenca_B_A)

print("\nA ordem dos conjuntos funciona da seguinte forma.")
print("O conjunto que vem primeiro como A em (A - B) é o conjunto principal da operação.")
print("O resultado será a impressão de todos os itens do conjunto A com exceção dos itens em comum com o conjunto subsequente, neste caso o conjunto B.")

uniao_AB = A | B
print("Uniao: ", uniao_AB)
print("\nO conjunto final é a união dos dois conjuntos criados anteriormente.")
print("Resultado da operação: Uniao: ", uniao_AB)

# ----------------- Questão 5 -------------------

lista_com_duplicatas = [1, 2, 2, 3, 4, 4, 5]
conjunto_sem_duplicatas = set(lista_com_duplicatas)

print("----------------- Questão 5 -------------------")

print("\nLista com duplicatas:", lista_com_duplicatas)
print("Conjunto sem duplicatas:", conjunto_sem_duplicatas)
lista_sem_duplicatas = list(conjunto_sem_duplicatas)
print("Lista convertida de volta sem duplicatas:", lista_sem_duplicatas, "\n")

# ----------------- Questão 6 -------------------


conjunto_imutavel = frozenset({1, 2, 3, 4})

print("----------------- Questão 6 -------------------")

print("\nConjunto imutável (frozenset):", conjunto_imutavel)
print("Tentar adicionar ou remover elementos de um frozenset gera um erro, pois ele é imutável.\n")

# ----------------- Questão 7 -------------------

print("----------------- Questão 7 -------------------\n")

frase = "Eu amo muito o meu cachorro Obi. O nome dele é Obi porque eu amo muito Star Wars."
palavras_unicas = set(frase.lower().replace(".", "").replace(",", "").split())

print("\nConjunto de palavras únicas:", palavras_unicas)

# ----------------- Questão 8 -------------------


cores = {"vermelho", "verde", "azul"}

print("----------------- Questão 8 -------------------")

print("\n'amarlelo' está no conjunto?", "amarelo" in cores)

cores.add("amarelo")
print("'amarelo' foi adicionado ao conjunto:", cores)
