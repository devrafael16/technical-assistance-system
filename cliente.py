class Cliente:
    def __init__(self):
        self.nome = ''
        self.cpf = ''
        self.telefone = ''
        self.endereco = ''

    def cadastro(self):
        self.nome = input('Nome do cliente: ')
        self.cpf = input('CPF do cliente:  ')
        self.telefone = input('Telefone para contato: ')
        self.endereco = input('Endereço: ')
        print()
        


    