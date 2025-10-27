lista = []
while True:
    escolha_usuario = input('Deseja [A]dicionar, [L]istar, [E]xcluir ou [S]air: ').lower()

    if escolha_usuario == 'a':
        lista.append(input('O que deseja adicionar? '))
        print('Produto:',lista[-1],'Adicionado á lista.')
    
    elif escolha_usuario == 'l':
        indice = range(len(lista))
        for indices in indice:
            print(indices,'-',lista[indices])
    
    elif escolha_usuario == 'e':
        print('Qual item deseja excluir? Use os números para excluir o item.')
        indice = range(len(lista))
        for indices in indice:
            print(indices,'-',lista[indices])
        try:
            opcao_usuario = int(input('Qual item deseja remover? '))
            lista.pop(opcao_usuario)
        except ValueError:
            print('Digite um número inteiro.')
        except IndexError:
            print('Digite um número que esteja na lista.')

    elif escolha_usuario == 's':
        print('Você saiu da sua lista.')
        break