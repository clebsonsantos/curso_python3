# Faça um programa que peça o primeiro nome do usuario. 
# Se o nome tiver 4 letras ou menos, escreva `seu nome é curto` 
# Se tiver entre 5 ou 6, escreva `seu nome é normal` 
# Se tiver maior que 6, escreva `seu nome é muito grande`

nome = input("Digite seu nome: ")

try:
  qtd_caracter = len(nome)

  if qtd_caracter <= 4:
    print("seu nome é muito curto")
  elif qtd_caracter > 4 and qtd_caracter < 7:
    print("Seu nome é normal")
  elif qtd_caracter > 6:
    print("Seu nome é muito grande")
except:
  print("Informe um nome válido")