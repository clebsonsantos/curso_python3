# Criar um programa que peça ao usuario para digitar um numero inteiro, 
# informe se ese numero é par ou impar. Caso o usuario não digite um numero inteiro, 
# informe que nao é um numero inteiro

numero_1 = input("Digite um numero inteiro: ")

if not numero_1.isdigit():
  print("informaçao inválida")
elif numero_1.isdigit():
  numero_1 = int(numero_1)
  print("informação válida")

try: 
  e_par = (int(numero_1)%2 == 0)
  if e_par:
    print(' é par')
  else: 
    print("é impar")
except:
  print("informe apenas numero inteiros")
