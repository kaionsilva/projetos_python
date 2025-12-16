#Coletar dados do usuário e transformar informação em INT e tirar erros de digitação
cpf = input('Digite o seu CPF: ')
cpf = cpf.replace("-", "").replace(".", "").replace(" ", "")
cpf_user = list(cpf)
cpf_user = [int(x) for x in cpf]

#Pegando os dois últimos digitos do CPF para cálculo
last_digit_cpf = cpf_user[-2], cpf_user[-1]
last_digit_cpf = list(last_digit_cpf)
#Removendo 2 últimos digitos do CPF
for i in range(1, 3):
    cpf_user.pop()

#Calculo multiplicação dos 9 primeiros digitos
for x in len(cpf_user):
    multiplier = 10
    result_multiplier = cpf_user[x] * multiplier
    multiplier -= 1
    sum_total = sum_total + result_multiplier
    total = sum_total % 11



