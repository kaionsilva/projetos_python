
#Lista com dicionários para organização de questão, alternativas e resposta.
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },

    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },

    {
        'Pergunta': 'Quanto é 10/2',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

contador_nota = 0

def exibir_pergunta(z=0):
    print(perguntas[z]['Pergunta'])


def exibir_questoes(i=0):
    for exibir_opcoes in range(len(perguntas[i]['Opções'])):
        print(f'({exibir_opcoes})', perguntas[i]['Opções'][exibir_opcoes])


exibir_pergunta()
exibir_questoes()

try:
    resposta_usuario = int(input('Digite a alternativa: '))
    if resposta_usuario > 3:
        print('Digite apenas as alternativas disponiveis.')
    else:
        if resposta_usuario == 2:
            print('Parabéns, você acertou a questão!')
            contador_nota += 1
        else:
            print('Você errou a questão!')
except ValueError:
    print('Digite apenas as alternativas disponiveis.')

exibir_pergunta(1)
exibir_questoes(1)

try:
    resposta_usuario = int(input('Digite a alternativa: '))
    if resposta_usuario > 3:
        print('Digite apenas as alternativas disponiveis.')
    else:
        if resposta_usuario == 0:
            print('Parabéns, você acertou a questão!')
            contador_nota += 1
        else:
            print('Você errou a questão!')
except ValueError:
    print('Digite apenas as alternativas disponiveis.')

exibir_pergunta(2)
exibir_questoes(2)

try:
    resposta_usuario = int(input('Digite a alternativa: '))
    if resposta_usuario > 3:
        print('Digite apenas as alternativas disponiveis.')
    else:
        if resposta_usuario == 2:
            print('Parabéns, você acertou a questão!')
            contador_nota += 1
        else:
            print('Você errou a questão!')
except ValueError:
    print('Digite apenas as alternativas disponiveis.')

print(f'Resultado: 3/{contador_nota}')
