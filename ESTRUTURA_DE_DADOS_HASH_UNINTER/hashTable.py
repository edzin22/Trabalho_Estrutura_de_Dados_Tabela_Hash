class Node:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class HashTable:
    def __init__(self):
        self.table = [None] * 10  

    def hash_function(self, sigla):
        if sigla == "EF":
            return 1
        
        if sigla == "DF":
            return 7  
        else:
            return (ord(sigla[0]) + ord(sigla[1])) % 10  

    def insert(self, sigla, nomeEstado):
        index = self.hash_function(sigla)
        nodo = Node(sigla, nomeEstado)
        nodo.proximo = self.table[index]
        self.table[index] = nodo  

    def print_table(self):
        for i in range(len(self.table)):  
            current = self.table[i]
            print(f" {i}:", end=" ")
            while current:
                print(f"{current.sigla} ({current.nomeEstado}) ->", end=" ")
                current = current.proximo
            print("None")

# Criação da tabela hash
hash_table = HashTable()

#Impressão da tabela hash antes de inserir qualquer informação
print("________________________________________________________________________________________________")
print("Tabela Hash Inicial:")

hash_table.print_table()

# Inserção dos estados
estados = [
    ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"), ("BA", "Bahia"),
    ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"), ("GO", "Goiás"),
    ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"), ("MG", "Minas Gerais"),
    ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"), ("PE", "Pernambuco"), ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"), ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"), ("SP", "São Paulo"),
    ("SE", "Sergipe"), ("TO", "Tocantins")
    ]

# Inserção dos estados e Distrito Federal
for sigla, nome in estados:
    hash_table.insert(sigla, nome)  
print("________________________________________________________________________________________________")
#Impressão da tabela hash após inserir os 26 estados e o Distrito Federal - DF
print("\nTabela Hash após inserir os 26 estados e o Distrito Federal:")

hash_table.print_table()


# Inserção do estado fictício
estado_ficticio = ("EF", "Edmilson Ferreira")
hash_table.insert(*estado_ficticio)  
print("________________________________________________________________________________________________")
print("\nTabela Hash após inserir os 26 estados, Distrito Federal e o estado fictício:")

hash_table.print_table()
