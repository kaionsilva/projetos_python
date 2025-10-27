#CPF EXEMPLO: 746.824.890-70

#Variáveis / Listas
cpf = ('746.824.890-70')
cpf_multiplicado = 0
soma_cpf_multiplicado = 0
#---

#Calculo do primeiro digito
digito_cpf = cpf.replace('-', '.').split('.')

#digitos do cpf separados em list
digitos_cpf = [int(digito) for numero in digito_cpf for digito in numero]
ultimos_digitos_cpf = [digitos_cpf[9], digitos_cpf[10]] #Pegar os 2 últimos digitos do CPF
del digitos_cpf[-1] #Exclusão dos dois últimos digitos do CPF
del digitos_cpf[-1]

#Calculo para o primeiro digito do CPF
soma_cpf = 0
multiplicacao_cpf = 10
indice = range(len(digitos_cpf))

for indices in indice:
    cpf_multiplicado = digitos_cpf[indices] * multiplicacao_cpf
    multiplicacao_cpf -= 1
    soma_cpf += cpf_multiplicado

total_primeirodigito = 0
total_primeirodigito = (soma_cpf * 10) % 11

if total_primeirodigito > 9: #Resultado do primeiro digito do CPF
    total_primeirodigito = 0 

#Calculo para o segundo digito do CPF

digitos_cpf.extend([ultimos_digitos_cpf[0]])

soma_cpf = 0
multiplicacao_cpf = 11
indice = range(len(digitos_cpf))

for indices in indice:
    cpf_multiplicado = digitos_cpf[indices] * multiplicacao_cpf
    multiplicacao_cpf -= 1
    soma_cpf += cpf_multiplicado

total_segundodigito = 0
total_segundodigito = (soma_cpf * 10) % 11

if total_segundodigito > 9: #Resultado do segundo digito do CPF
    total_segundodigito = 0 

#Verificação de digitos se batem com o cálculo
if str(total_primeirodigito) in str(ultimos_digitos_cpf) and str(total_segundodigito) in str(ultimos_digitos_cpf):
    print('CPF válido')
else:
    print('CPF inválido')