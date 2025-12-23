#Pegar variaveis de outros arquivos
from garage import courtyard
from employees import employees
#---------
#Variaveis

#---------
#Bloco de acesso do usuário de acordo com sua escolha
while True:
    #Escolha do usuário para o que vai acessar
    choose_login = input("""
    Bem-vindo ao sistema concessionária em python!
    (C) - Clientes
    (F) - Funcionários
    (A) - Administrador
""").upper()
    
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
        #Bloco de decisão de compra do cliente
        if option_exit_or_buy == 'Y':
            print('Selecione o vendedor com o seu índice que realizou essa venda: ')
            print()
            #Bloco de decisão de qual vendedor realizou a venda
            for x, employees_info in enumerate(employees):
                print(f'{x} - {employees_info['Nome']}')
                choose_seller = int(input('Digite o vendedor que realizou esta venda: '))
        elif option_exit_or_buy == 'E':
            print('Saindo do painel do cliente...')
            continue
