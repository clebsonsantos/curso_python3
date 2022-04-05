# Faça um programa que pergunte as horas e baseado nisso exiba a suadação apropriada. 
# Ex: Bom dia 0-11, Boa tarde 12-17, Boa noite 18-23.

horas = input('Que horas são? ')

try:
  horas = int(horas)

  manha = horas > 0 and horas < 12
  tarde = horas > 11 and horas < 17
  noite = horas > 17 and horas < 24
  if manha:
    print("Bom dia")
  elif tarde:
    print("Boa tarde")
  elif noite:
    print("Boa noite") 
except:
  print("Informação inválida")