from cliente import Cliente
from rich import print
from rich.panel import Panel
from rich.console import Console
from ordem_servico import OS
from database import salvar_cliente, listar_clientes


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
        print('6 - Editar Ordem de Serviço')
        print('0 - Sair')

        opcao = input('\nDigite a opção desejada: ')
        print()

        if opcao.isdigit():
            opcao = int(opcao)
            if opcao  == 1:
                cliente = Cliente()
                cliente.cadastro()
                salvar_cliente(
                    cliente.nome,
                    cliente.cpf,
                    cliente.telefone,
                    cliente.endereco
                )
                print('[green]Cliente cadastrado com sucesso![/]')

            elif opcao == 2:
                clientes_banco = listar_clientes()
                if not clientes_banco:
                    print('Nenhum cliente cadastrado.')
                else:
                    print(f'\n{"CLIENTES CADASTRADOS":=^30}')
                    for cliente in clientes_banco:
                        print(f'\n{"Nome:":<12} {cliente[1]}')
                        print(f'{"CPF:":<12} {cliente[2]}')
                        print(f'{"Telefone:":<12} {cliente[3]}')
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
                    if os_escolha.isdigit():
                        os_escolha = f'OS{int(numero):03d}'
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
                if busca.isdigit():
                    busca = int(busca)
                    if busca == 1:
                        nome_os = input('Digite o nome: ')
                        encontrou = False
                        for ordem_servico in ordens_servico:
                            if nome_os.lower() in ordem_servico.cliente.lower():
                                ordem_servico.mostrar_os()
                                encontrou = True
                                
                        if not encontrou:
                            print('OS não encontrada.')
                                
                    elif busca == 2:
                        numero = input('Digite o número: ')
                        if numero.isdigit():
                            numero = f'OS{int(numero):03d}'
                        encontrou = False
                        for ordem_servico in ordens_servico:
                            if numero == ordem_servico.numero_os:
                                ordem_servico.mostrar_os()
                                encontrou = True
                                
                        if not encontrou:
                            print('OS não encontrada.')
                            

                    else:
                        print('[red]Opção inválida![/] Digite uma opção válida.')
                        continue
                            

                else:
                    print('[red]Opção inválida![/] Digite uma das opções a cima.')
                    continue

            elif opcao == 6:
                print(f'{" EDITAR ORDEM DE SERVIÇO ":=^30}')
                numero = input('\n Digite o número da OS que deseja editar: ')
                if numero.isdigit():
                    numero = f'OS{int(numero):03d}'
                    for ordem_servico in ordens_servico:
                        encontrou = False
                        if numero == ordem_servico.numero_os:
                            ordem_servico.mostrar_os()
                            editar_opcoes = {
                                '1' : 'cliente',
                                '2' : 'aparelho',
                                '3' : 'marca_modelo',
                                '4' : 'senha_aparelho',
                                '5' : 'defeito',
                                '6' : 'status',
                                '7' : 'valor',
                                '8' : 'observacoes'
                            }
                            print('Qual dado gostaria de alterar: ')
                            print()
                            for c,v in editar_opcoes.items():
                                print(f'{c} - {v}')
                            opcao = input('')
                            
                            if opcao in editar_opcoes:
                                atributo = editar_opcoes[opcao]
                                novo_dado = input(f'Novo {atributo}')
                                if atributo == 'valor':
                                    novo_dado = float(novo_dado)
                                ordem_servico.editar_os(atributo, novo_dado)
                                print('Status atualizado com sucesso!')
                                encontrou = True
                            if not encontrou:
                                print('OS não encontrada!')




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

