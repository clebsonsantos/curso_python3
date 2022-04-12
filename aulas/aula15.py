# Formatando valores com modificadores 
# :s - strings
# :f - numeros de ponto flutuante
# :d inteiros
# :.(numero)f casas decimais 
# :(caracteres)(> ou < ou ^) (quantidade)(tipo -s, d ou f)

# > esquerda
# < direita
# ^ centro

number_1 = 10
number_2 = 350
number_3 = 1
divisao = number_1 / number_2

print('{:.2f}'.format(divisao))

print(f'{number_3:0>10}')

print(f'{number_2:0>10}')

print(f'{number_2:.2f}')