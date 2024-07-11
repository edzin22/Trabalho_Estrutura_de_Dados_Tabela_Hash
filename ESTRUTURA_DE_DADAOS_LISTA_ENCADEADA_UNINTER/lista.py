class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if self.head is None:
            self.head = nodo
        elif self.head.cor == 'V':
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo is not None and atual.proximo.cor == 'A':
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):
        cor = obter_entrada_string("Digite a cor do cartão (A/V): ").upper()
        while cor not in ['A', 'V']:
            print("Entrada inválida. Por favor, digite 'A'/'V'.")
            cor = obter_entrada_string("Digite a cor do cartão (A/V): ").upper()
            
        numero = obter_entrada_inteiro("Digite o número do cartão: ")
        
        nodo = Nodo(numero, cor)
        
        if self.head is None:
            self.head = nodo
        elif cor == 'V':
            self.inserirSemPrioridade(nodo)
        else:
            self.inserirComPrioridade(nodo)

    def imprimirListaEspera(self):
        atual = self.head
        while atual is not None:
            print(f"Cartão -> [{atual.cor},{atual.numero}]")
            atual = atual.proximo

    def atenderPaciente(self):
        if self.head is None:
            print("Nenhum paciente na fila.")
        else:
            print(f"Atendendo paciente cartão cor {self.head.cor} e número {self.head.numero}")
            self.head = self.head.proximo

def obter_entrada_string(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isalpha():
            return entrada
        else:
            print("Entrada inválida. Por favor, digite apenas letras.")

def obter_entrada_inteiro(mensagem):
    while True:
        try:
            entrada = int(input(mensagem))
            return entrada
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def listaMenu():
    lista = ListaEncadeada()
    while True:
        print("\nMenu:")
        print("1 - Adicionar paciente à fila")
        print("2 - Mostrar pacientes na fila")
        print("3 - Chamar paciente")
        print("4 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            lista.inserir()
        elif opcao == '2':
            lista.imprimirListaEspera()
        elif opcao == '3':
            lista.atenderPaciente()
        elif opcao == '4':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    listaMenu()
