import re

cpf = '850.806.780-11'.replace('.', '').replace('-', '')

cpf = re.sub(r'[^0-9]', '', cpf)


nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0

for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0


dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_1 = 11

resultado_digito_2 = 0

for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'

if cpf == novo_cpf:
    print(f'{cpf} é válido')
else:
    print(f'{cpf} é inválido')
