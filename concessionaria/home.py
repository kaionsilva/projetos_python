#Pegar variaveis de outros arquivos
from garage import courtyard
from employees import employees

#Escolha do usuário para o que vai acessar
escolha_login = input("""
    Bem-vindo ao sistema concessionária em python!
    (C) - Clientes
    (F) - Funcionários
    (A) - Administrador
""").upper()

#Bloco de acesso do usuário de acordo com sua escolha
if escolha_login == 'C':
    
    name_cliente = input('Bem vindo, digite o seu nome para continuarmos: ') 
    print()
    print(f'Bem-vindo{name_cliente}. Segue abaixo nossos veículos a venda: ')

    for x, car in enumerate(courtyard):
        print(f'{x}', '-', car['Car'])
    option_car = int(input('Digite o veiculo que deseja verificar. (Ex: 2)'))
    print()
    print('-'*10, 'DADOS DO VEICULO', '-'*10)
    for car_description in courtyard[option_car]:
        print(f'{car_description}: {courtyard[option_car][car_description]}')
