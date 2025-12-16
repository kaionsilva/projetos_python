#Coletar dados do usuário e transformar informação em INT e tirar erros de digitação
cpf = input('Digite o seu CPF: ')
cpf = cpf.replace("-", "").replace(".", "").replace(" ", "")
cpf_usuario = list(cpf)
cpf_usuario = [int(x) for x in cpf]

#Pegando os dois últimos digitos do CPF para cálculo
ultimos_digitos_cpf = cpf_usuario[-2], cpf_usuario[-1]
ultimos_digitos_cpf = list(ultimos_digitos_cpf)
#Removendo 2 últimos digitos do CPF
for i in range(1, 3):
    cpf_usuario.pop()

#Calculo multiplicação dos 9 primeiros digitos
for x in len(cpf_usuario):
    multiplicador = 10
    resultado_multiplicacao = cpf_usuario[x] * multiplicador
    multiplicador -= 1
    soma_total = soma_total + resultado_multiplicacao
    total = soma_total % 11



