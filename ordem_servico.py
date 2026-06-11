from datetime import datetime

class OS:
    def __init__(self):  
        self.numero_os = ''
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
        self.senha_aparelho = input('Senha do aparelho: ')
        self.defeito = input('Defeito relatado: ')
        self.observacoes = input('Observações: ')
        print()

    def mostrar_os(self):
        print(f'\nNumero da OS: {self.numero_os}')
        print(f'Cliente: {self.cliente}')
        print(f'Tipo do aparelho: {self.aparelho}')
        print(f'Marca/modelo: {self.marca_modelo}')
        print(f'Data de entrada: {self.data_entrada}')
        print(f'Defeito: {self.defeito}')
        print(f'Observações: {self.observacoes}')
        print(f'Status: {self.status}')
        print('-' * 30)

    @staticmethod
    def mostrar_os_banco(ordem):
        print(f'-' * 40)
        print(f'\nID: {ordem[0]}')
        print(f'Número da OS: {ordem[1]}')
        print(f'Cliente: {ordem[2]}')
        print(f'Aparelho: {ordem[3]}')
        print(f'Marca/Modelo: {ordem[4]}')
        print(f'Senha do aparelho: {ordem[5]}')
        print(f'Defeito: {ordem[6]}')
        print(f'Status: {ordem[7]}')
        print(f'Valor: {ordem[8]}')
        print(f'Observações: {ordem[9]}')
        print(f'Data de entrada: {ordem[10]}')
        print('-' * 40)
