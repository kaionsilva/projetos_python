
while True:
    print('Bem vindo á calculadora feita em PYTHON.')
    escolha_usuario = input('Qual forma de calculo deseja? [A]dição, [S]ubtração, [D]ivisão ou [E]xit para sair.: ').lower()

    if escolha_usuario == 'a':
        print('Você selecionou o cálculo de ADIÇÃO')
        a = int(input('Digite o primeiro valor: '))
        b = int(input('Digite o segundo valor: '))
        resultado = a + b
        print(f'Resultado: {resultado}')
        continue
    elif escolha_usuario == 's':
        print('Você selecionou o cálculo de SUBTRAÇÃO')
        a = float(input('Digite o primeiro valor: '))
        b = float(input('Digite o segundo valor: '))
        resultado = a - b
        print(f'Resultado: {resultado:.2f}')
        continue
    elif escolha_usuario == 'd':
        print('Você selecionou o cálculo de DIVISÃO')
        a = float(input('Digite o primeiro valor: '))
        b = float(input('Digite o segundo valor: '))
        resultado = a / b
        print(f'Resultado: {resultado:.2f}')
        continue
    else:
        if escolha_usuario == 'e':
            print('Você saiu da calculadora feita em PYTHON')
            break
        else:
            print('Você não selecionou nenhuma das opções, tente novamente.')
            continue