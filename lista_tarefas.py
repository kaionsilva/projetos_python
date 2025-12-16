import time
task_user = []
count_task = 0


while True:
    print('='*35)
    print(' '*1,'--LISTA DE TAREFAS EM PYTHON--')
    print('='*35)

    for x in range(len(task_user)):
        print(f'{x} - {task_user[x]}')

    print('='*35)
    print('(A) Adicionar tarefa\n(C) Marcar tarefa como concluída\n(R) Remover tarefa')
    choose_user = input('Digite uma opção: ').lower()

    #Bloco para adicionar tarefas á lista
    if choose_user == 'a':
        add_task = input('Adicionar tarefa: ').title()
        task_user.append(add_task)
        print('Tarefa adicionada com sucesso!')
        time.sleep(2)

    #Bloco para concluir uma tarefa
    elif choose_user == 'c':
        print()
        for x in range(len(task_user)):
            print(f'{x} - {task_user[x]}')
        print()
        try:
            done_task = int(input('Digite a tarefa que deseja concluir. (Ex: 2) '))
            task_user.pop(done_task)
            print('Terefa concluída, parabéns! ✅')
            count_task += 1
            print(f'Tarefas concluídas: {count_task}')
            time.sleep(2)
        except IndexError:
            print('Desculpa, mas não existe essa tarefa na sua lista. ✘')
            time.sleep(2)
        except ValueError:
            print('Desculpe, mas digite apenas os índices das tarefas. (Ex: 3)')
            time.sleep(2)

    #Bloco para remover uma tarefa
    elif choose_user == 'r': 
        print()
        for x in range(len(task_user)):
            print(f'{x} - {task_user[x]}')
        print()
        try:
            remove_task = int(input('Digite a tarefa que deseja remover. (Ex: 3)'))
            task_user.pop(remove_task)
            print('Tarefa removida')
        except IndexError:
            print('Desculpe, mas não existe essa tarefa na sua lista. ✘')
            time.sleep(2)
        except ValueError:
            print('Desculpe, mas digite apenas os índices das tarefas. (Ex: 3)')
            time.sleep(2)




