# usando len(), retorna um inteiro
 
usuario = input("Digite seu usuario: ")
qtd_caracter = len(usuario)

if qtd_caracter < 6:
  print("voce precisa digitar 6 caracteres")
else:
  print("cadastrado com sucesso")
