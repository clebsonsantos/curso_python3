# Formatação de strings

nome = "clebson"
idade = 26 # int
altura = 1.79 # float
maior_de_idade = idade > 18
peso = 89
imc = peso / (altura ** 2)

print(f"{nome} tem {idade} de idade e seu imc é {imc:.2f}") # .2(duas casas)f(flutuantes)
print("{} tem {} anos de idade e seu imc é {:.2f}".format(nome, idade, imc))

# atribuindo posições
print("{0} tem {1} anos e seu imc é {2}. idade: {1} e nome: {0}".format(nome, idade, imc))

# atribuindo paremetros nomeados
print("{n} tem {i} anos de idade e seu imc é {im}".format(n=nome, i=idade, im=imc))
