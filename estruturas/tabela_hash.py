#Inserção na lista:
hash_list = [None] * 11

def aula_hash(key):
    index = key % 11
    hash_list[index] = key
    
aula_hash(16)
aula_hash(15)
aula_hash(14)
aula_hash(13)
aula_hash(12)
aula_hash(11)

print(hash_list)


# Método de Folding:
def foldig(key):
    key_string = str(key)
    
    return