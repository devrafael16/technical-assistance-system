from cliente import Cliente
from rich import print
from rich.panel import Panel
from rich.console import Console
from ordem_servico import OS

clientes = []
ordens_servico = []

def main():


    print(f'{"Sistema de assistência técnica":^30}')

    while True:
        print(f'\n{" Menu ":=^30}')
        print('\n1 - Cadastro de cliente')
        print('2 - Listar clientes')
        print('3 - Cadastrar Ordem de Serviço')
        print('4 - Listar Ordem de Serviço')
        print('5 - Buscar Ordem de Serviço')
        print('0 - Sair')

        opcao = input('\nDigite a opção desejada: ')
        print()

        if opcao.isdigit():
            opcao = int(opcao)
            if opcao  == 1:
                cliente = Cliente()
                cliente.cadastro()
                clientes.append(cliente)
                print('[green]Cliente cadastrado com sucesso![/]')

            elif opcao == 2:
                if not clientes:
                    print('Nenhum cliente cadastrado.')
                else:
                    for cliente in clientes:
                        print(f'\n{"CLIENTES CADASTRADOS":=^30}')
                        print(f'\n{"Nome:":<12} {cliente.nome}')
                        print(f'{"CPF:":<12} {cliente.cpf}')
                        print(f'{"Telefone:":<12} {cliente.telefone}')
                        print('-' * 30)

            elif opcao == 3:
                numero_os = len(ordens_servico) + 1
                ordem_servico = OS(numero_os)
                ordem_servico.abrir_os()
                ordens_servico.append(ordem_servico)
                print('[green]Ordem de serviço cadastrada com sucesso![/]')

            elif opcao == 4:
                if not ordens_servico:
                    print('Nenhuma ordem de serviço cadastrada.')
                else:
                    print(f'{"ORDENS DE SERVIÇOS":=^30}')

                    for ordem_servico in ordens_servico:
                        print(f'{ordem_servico.numero_os} | {ordem_servico.cliente} | {ordem_servico.status}')
                    os_escolhida = input('Digite o numero da OS que deseja vizualizar: ')
                    for ordem_servico in ordens_servico:
                        if os_escolhida == ordem_servico.numero_os:
                            print(f'\n{ordem_servico.numero_os:^30}')
                            print(f'\nNumero da OS: {ordem_servico.numero_os}')
                            print(f'Cliente: {ordem_servico.cliente}')
                            print(f'Tipo do aparelho: {ordem_servico.aparelho}')
                            print(f'Marca/modelo: {ordem_servico.marca_modelo}')
                            print(f'Data de entrada: {ordem_servico.data_entrada}')
                            print(f'Defeito: {ordem_servico.defeito}')
                            print(f'Observações: {ordem_servico.observacoes}')
                            print(f'Status: {ordem_servico.status}')
                            print('-' * 30)
                            break

            elif opcao == 5:
                print('1 - Buscar por cliente')
                print('2 - Buscar por número da OS')
                busca = input()
                if busca.isdigit:
                    busca = int(busca)
                    if busca == 1:
                        nome_os = input('Digite o nome: ')
                        if nome_os.lower() in ordem_servico.cliente.lower():
                            ordem_servico.mostrar_os()
                            break
                        else:
                            print('OS não encontrada.')
                            break
                    elif busca == 2:
                        numero = input('Digite o número: ')
                        if numero in ordem_servico.numero_os:
                            ordem_servico.mostrar_os
                            break
                        else:
                            print('OS não encontrada.')
                            break
                    else:
                        print('[red]Opção inválida![/] Digite uma opção válida.')
                        continue
                            

                else:
                    print('[red]Opção inválida![/] Digite uma das opções a cima.')
                    continue

            elif opcao == 0:
                print('Saindo do sistema...')
                break

            else:
                print('[red]Opção inválida![/]')
                continue

        else:
            print('[red]Opção inválida![/] Escolha uma das opções do menu.')
        

if __name__ == '__main__':
    main()

