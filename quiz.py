#Lista com dicionários para organização de questão, alternativas e resposta.
questions = [
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
#Variavel para aparecer letras as questões // Contagem de perguntas corretas
words = ['A', 'B', 'C', 'D']
question_right = 0

#Bloco para mostrar a pergunta
for question_for_user in questions:
    print(question_for_user['Pergunta'])

    #Bloco para mostrar as opções
    for i, option_for_user in enumerate(question_for_user['Opções']):
        print(f'({words[i]}) {option_for_user}')
        
    #Bloco de resposta do usuario para verificar se a opção escolhida está certa ou incorreta
    response_user = input('Digite a alternativa: ').upper()
    if response_user == questions[0]['Resposta']:
