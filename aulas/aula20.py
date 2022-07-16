texto = 'Python'
# utilizando laço for
for letra in texto:
  print(letra)

# utilizando range
for numero in range(20,10,-1):
  print(numero)

print("#######")
for n in range(100):
  if n % 8 == 0:
    print(n)


nova_string = ''

for letra in texto:
  if letra == 't':
    nova_string += letra.upper()
  elif letra == 'h':
    nova_string += letra.upper()
    break
  else: 
    nova_string += letra
    
print(nova_string)