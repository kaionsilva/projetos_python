#Pegar variaveis de outros arquivos
import time
from garage import courtyard
from employees import employees
#---------
#Variaveis

#---------
#Bloco de acesso do usuário de acordo com sua escolha
while True:
    #Escolha do usuário para o que vai acessar
    try:
        choose_login = input("""
        Bem-vindo ao sistema concessionária em python!
        (C) - Clientes
        (F) - Funcionário
        (A) - Administrador
    """).upper()
    except ValueError, IndexError:
        print('Por favor, digite apenas as opções disponíveis.')
        
    #Bloco de decisão para qual ferramenta o usuário escolheu
    if choose_login == 'C':
        name_client = input('Bem vindo, digite o seu nome para continuarmos: ')
        balance_client = float(input('Digite o seu saldo: '))
        print()
        print(f'Bem-vindo{name_client}. Segue abaixo nossos veículos a venda: ')

        #Bloco opções de veículos para o cliente
        for x, car in enumerate(courtyard):
            print(f'{x}', '-', car['Carro'])
        option_car = int(input('Digite o veiculo que deseja verificar. (Ex: 2)'))
        print()

        #Bloco para cliente visualizar descrições do veículo selecionado
        print('-'*10, 'DADOS DO VEICULO', '-'*10)
        for car_description in courtyard[option_car]:
            print(f'{car_description}: {courtyard[option_car][car_description]}')
        print('-'*40)

        #Bloco para cliente comprar ou sair da página cliente
        option_exit_or_buy = input("""
        (Y) - Comprar Veículo
        (E) - Sair do painel de cliente
                            """).upper()
        
        #Bloco para verificar de saldo do cliente é compativel com o valor do carro.
        if balance_client < courtyard[option_car]['Valor']:
            print('Não há saldo suficiente para realizar a compra.')
            print('Saindo do painel do cliente...')
            time.sleep(3)
            continue
        
        #Bloco de decisão se cliente quer comprar veículo
        if option_exit_or_buy == 'Y':
            print('Selecione o vendedor com o seu índice que realizou essa venda: ')
            print()

            #Bloco para mostrar nome e índice dos vendedores
            for x, employees_info in enumerate(employees):
                print(f'{x} - {employees_info['Nome']}')
            
            #Bloco para seleção de funcionário na qual vai receber comissão, vendas realizadas e o nome do veículo que vendeu
            try:
                choose_seller = int(input('Digite o vendedor que realizou esta venda: '))
                vendor = employees[choose_seller]
                vendor['Vendas Realizadas'] += 1
                vendor['Carros Vendidos'].append(courtyard[option_car]['Carro'])
                vendor['Comissão'] += courtyard[option_car]['Valor'] * 0.10
                print('Venda confirmada!')
                print()

                #Bloco de loop para mostrar informações do funcionário que realizou a venda
                for info_seller in employees[choose_seller]:
                    print(f'{info_seller}: {employees[choose_seller][info_seller]}')
            

            except ValueError, IndexError:
                print('Por favor, escolha o índice do vendedor que realizou a venda.')
                print('Voltando para o menu principal... COMPRA CANCELADA')
                time.sleep(3)

        #Bloco de saída para retornar ao LOOP principal
        elif option_exit_or_buy == 'E':
            print('Saindo do painel do cliente...')
            time.sleep(3)
            continue
    
    #Bloco de funcionário
    elif choose_login == 'F':
        
        #Bloco de loop para mostrar os funcionários
        for x, employees_info in enumerate(employees):
                print(f'{x} - {employees_info['Nome']}')

        #Bloco de decisão para qual vai acessar o sistema
        choose_employees = int(input('Digite qual login deseja acessar: '))
        if choose_employees == 0:
            print('Oi')