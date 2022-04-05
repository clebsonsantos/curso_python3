# Operadores lógicos

# and
# or
# not
# in
# not in

a = 2
b = 3
c = 2
nome = 'clebson'

usando_and = ( a == b and a == c) # verifica se as suas são verdadeiras
usando_or = ( a == b or a == c) # retorna true para algumas das condições
usando_not = ( not b > a ) # inverte o valor retornado 

print(usando_and)
print(usando_or)
print(usando_not)

# verifica se existe um determinado carater em uma string
if 'l' in nome: 
  print("existe esta letra no seu nome")

# verifica se não existe um determinado carater em uma string
if 'abc' not in nome: 
  print("não existe em seu nome")