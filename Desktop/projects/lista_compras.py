lista = []
while True:
    escolha_usuario = input('Deseja [A]dicionar, [L]istar, [E]xcluir ou [S]air: ').lower()

    if escolha_usuario == 'a':
        lista.append(input('O que deseja adicionar? '))
        print('Produto:',lista[-1],'Adicionado á lista.')
    
    if escolha_usuario == 'l':
        indice = range(len(lista))
        for indices in indice:
            print(indices,'-',lista[indices])
    
    if escolha_usuario == 'e':
        print('Qual item deseja excluir? Use os números para excluir o item.')
        indice = range(len(lista))
        for indices in indice:
            print(indices,'-',lista[indices])
        opcao_usuario = int(input('Qual item deseja remover? '))
        lista.pop(opcao_usuario)

    if escolha_usuario == 's':
        print('Você saiu da sua lista.')
        break