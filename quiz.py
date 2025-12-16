import time
#Lista com dicionários para organização de questão, alternativas e resposta.
questions = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': 'C',
    },

    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': 'A',
    },

    {
        'Pergunta': 'Quanto é 10/2',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': 'B',
    },

    {
        'Pergunta': 'Quanto é 100+22',
        'Opções': ['122', '123', '240', '121'],
        'Resposta': 'A',
    }
]
#Variavel para mostrar letras as questões // Contagem de perguntas corretas
words = ['A', 'B', 'C', 'D']
question_right = 0

#Bloco para mostrar a pergunta
for question_for_user in questions:
    print(question_for_user['Pergunta'])

    #Bloco para mostrar as opções
    for i, option_for_user in enumerate(question_for_user['Opções']):
        print(f'({words[i]}) {option_for_user}')
        
    #Bloco de resposta do usuario para verificar se a opção escolhida está certa ou incorreta
    response_user = input('Digite a sua alternativa: ').upper()
    if response_user == question_for_user['Resposta']:
        print('Você acertou!')
        question_right += 1
        time.sleep(2)
    else:
        print('Você errou!')
        time.sleep(2)

print(f'Parabéns, seu resultado: 3/{question_right}')
    

    
