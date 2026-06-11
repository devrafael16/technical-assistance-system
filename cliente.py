class Cliente:
    def __init__(self):
        self.nome = ''
        self.cpf = ''
        self.telefone = ''
        self.endereco = ''

    def cadastro(self):
        self.nome = input('Nome: ').strip()
        while True:
            cpf = input('CPF (somente números): ').strip().replace('.', '').replace('-', '')
            if cpf.isdigit() and len(cpf) == 11:
                self.cpf = cpf
                break
        print('CPF inválido. Digite 11 dígitos.')

        while True:
            tel = input('Telefone: ').strip()
            if tel.replace(' ', '').replace('-', '').isdigit():
                self.telefone = tel
                break
            print('Telefone inválido')

        self.endereco = input('Endereço: ')
        print()
        


    