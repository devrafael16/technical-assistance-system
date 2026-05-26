from datetime import datetime

class OS:
    def __init__(self, numero_os):  
        self.numero_os = f'OS{numero_os:03d}'
        self.cliente = ''
        self.aparelho = ''
        self.marca_modelo = ''
        self.senha_aparelho = ''
        self.defeito = ''
        self.status = 'Em análise'
        self.valor = 0
        self.observacoes = ''
        self.data_entrada = datetime.now().strftime('%d/%m/%Y %H:%M')

    def abrir_os(self):
        self.cliente = input('Nome do cliente: ')
        self.aparelho = input('Aparelho: ')
        self.marca_modelo = input('Marca e modelo: ')
        self.senha = input('Senha do aparelho: ')
        self.defeito = input('Defeito relatado: ')
        self.observacoes = input('Observações: ')
        print()


