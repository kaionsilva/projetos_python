#Coletar dados do usuário e transformar informação em INT e tirar erros de digitação do usuário
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

#Função para calculo do primeiro e segundo digito
def calc_digits(z):
    multiplier = z
    sum_total_digits = 0
    for digit in cpf_user:
        sum_total_digits = (digit * multiplier) + sum_total_digits
        multiplier -= 1
        total_first_calc = sum_total_digits % 11

    return 0 if total_first_calc <= 1 else 11 - total_first_calc

first_digit_calc = calc_digits(10)
#Adicionar a lista cpf_user o primeiro digito para segundo calculo
cpf_user.append(last_digit_cpf[0])
second_digit_calc = calc_digits(11)

if first_digit_calc == last_digit_cpf[0] and second_digit_calc == last_digit_cpf[1]:
    print('CPF válido.')
else:
    print('CPF Inválido.')
