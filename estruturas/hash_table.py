# Implementação de uma tabela de dispersão (hash table) simples
class HashTable:
    def __init__(self, size=10):
        """
        Inicializa a tabela de dispersão com um tamanho definido.

        Parâmetros:
        size (int): Tamanho inicial da tabela de dispersão.
        Vocês podem alterar o valor padrão para o tamanho da tabela.
        """
        self.size = size  # Define o tamanho da tabela.
        self.table = [None] * self.size  # Cria uma lista vazia para armazenar pares chave-valor.
        """
        Obs: [None] * self.size cria uma lista com self.size elementos None.
        Ou seja, a tabela começa vazia com o tamanho do "size".
        """

    def hash_function(self, key):
        """
        Função hash simples que converte a chave em um índice válido.

        Parâmetros:
        key: Chave que será usada para calcular o índice.

        Retorna:
        int: Índice da tabela calculado usando o hash da chave.
        """
        return hash(key) % self.size  # Calcula o índice usando a função hash e o tamanho da tabela.

    def put(self, key, value):
        """
        Insere ou atualiza um valor na tabela com base em uma chave.

        Parâmetros:
        key: Chave associada ao valor.
        value: Valor a ser armazenado.
        """
        index = self.hash_function(key)  # Calcula o índice para a chave.
        while self.table[index] is not None:  # Trata colisões com sondagem linear.
            if self.table[index][0] == key: # Se a chave já existir, atualiza o valor associado.
                self.table[index] = (key, value)
                return
            # Sondagem linear: tenta o próximo índice.
            index = (index + 1) % self.size
        # Insere o novo par chave-valor na posição calculada.
        self.table[index] = (key, value)

    def get(self, key):
        """
        Recupera um valor associado à chave fornecida.

        Parâmetros:
        key: Chave para a qual o valor será recuperado.

        Retorna:
        O valor associado à chave ou None se a chave não existir.
        """
        index = self.hash_function(key)  # Calcula o índice inicial.
        while self.table[index] is not None:  # Continua enquanto houver elementos no índice.
            if self.table[index][0] == key:
                return self.table[index][1]  # Retorna o valor associado.
            index = (index + 1) % self.size  # Continua sondagem linear.
        return None  # Retorna None se a chave não for encontrada.

    def delete(self, key):
        """
        Remove um item da tabela pela chave fornecida.

        Parâmetros:
        key: Chave associada ao item a ser removido.
        """
        index = self.hash_function(key)  # Calcula o índice inicial.
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None  # Remove o par chave-valor.
                return
            index = (index + 1) % self.size  # Continua sondagem linear.

# Testando a implementação básica
hash_table = HashTable()
hash_table.put("chave1", "valor1")
hash_table.put("chave2", "valor2")
hash_table.put("chave3", "valor3")

print("Valor para 'chave1':", hash_table.get("chave1"))
print("Valor para 'chave2':", hash_table.get("chave2"))

hash_table.delete("chave1")
print("Após remover 'chave1':", hash_table.get("chave1"))

# Adicionando rehashing dinâmico à tabela de dispersão
"""
Rehashing Dinâmico: Quando a taxa de carga ultrapassa 70%,
a tabela dobra de tamanho e todos os elementos são redistribuídos.
"""
class HashTableWithRehashing(HashTable):
    def __init__(self, size=10):
        """
        Inicializa uma tabela de dispersão com suporte a rehashing dinâmico.

        Parâmetros:
        size (int): Tamanho inicial da tabela.
        """
        super().__init__(size)  # Chama o construtor da classe base.
        self.count = 0  # Mantém o número de elementos armazenados.

    def put(self, key, value):
        """
        Insere ou atualiza um valor e redimensiona a tabela se necessário.

        Parâmetros:
        key: Chave associada ao valor.
        value: Valor a ser armazenado.
        """
        if self.count / self.size > 0.7:  # Verifica a taxa de carga (70% de ocupação).
            self._rehash()  # Redimensiona e redistribui os elementos.
        super().put(key, value)  # Insere o valor usando a implementação base.
        self.count += 1  # Incrementa o contador de elementos.

    def _rehash(self):
        """
        Duplica o tamanho da tabela e redistribui os elementos existentes.
        """
        old_table = self.table  # Armazena a tabela antiga.
        self.size *= 2  # Dobra o tamanho da tabela.
        self.table = [None] * self.size  # Cria uma nova tabela vazia.
        self.count = 0  # Reinicia o contador de elementos.

        for item in old_table:  # Reinsere todos os elementos da tabela antiga.
            if item is not None:
                self.put(item[0], item[1])  # Reinsere chave e valor.

# Teste de rehashing
hash_table_rehash = HashTableWithRehashing(size=5)  # Cria uma tabela com tamanho inicial 5.
for i in range(8):  # Insere 8 elementos para acionar o rehashing.
    hash_table_rehash.put(f"chave{i}", f"valor{i}")

# Exibe a tabela após rehashing.
print("Tabela após rehashing:", hash_table_rehash.table)