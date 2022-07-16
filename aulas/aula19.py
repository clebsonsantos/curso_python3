frase = 'o rato roeu a roupa do rei de roma' # iterável
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_do_user = input("Qual letra deseja colocar maiúscula: ")

# iteração <- iterar
while contador < tamanho_frase:
  letra = frase[contador]
  if letra == input_do_user:
    nova_string += input_do_user.upper()
  else: 
    nova_string += letra
  contador += 1
print(nova_string)