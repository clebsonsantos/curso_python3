# while em python
# realiza repetiçõese enquanto for verdadeira
# 
condicao = True
while condicao: 
  nome = input("Qual o seu nome?  ")
  print(f'Olá {nome}')
  condicao = False

print("Encerrou")

# Somando valores
x = 0

while x <= 10:
  if x == 3:
    x += 1
    continue 

  print(x)
  x += 1

y = 0

while y <= 5:
  if y == 3:
    y += 1
    break 

  print(y)
  y += 1