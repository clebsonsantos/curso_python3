import random
JOGODAFORCA = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
palavras = 'casa carro dinheiro uva apple xiaomi programa chocolate elefante golfinho motorola escola universidade chiclete honda yamaha lista praia corona '.split()

def buscarpalavraAleat(listapalavras):
    # Esta função retorna uma palavra aleatória.
    palavraAleatoria = random.randint(0, len(listapalavras) - 1)
    return listapalavras[palavraAleatoria]

def displayBoard(JOGODAFORCA, letraIncorreta, letraCorreta, palavraSecreta):
    print(JOGODAFORCA[len(letraIncorreta)])
    print ("")
    fim = " "
    print ('Letras incorretas:', fim)
    for letra in letraIncorreta:
        print (letra, fim)
    print ("")
    espaço = '_' * len(palavraSecreta)
    for i in range(len(palavraSecreta)): # Substitui os espaços em branco por uma letra escrita
        if palavraSecreta[i] in letraCorreta:
            espaço = espaço[:i] + palavraSecreta[i] + espaço[i+1:]
    for letra in espaço: # Mostrará a palavra secreta com espaços entre letras
        print (letra, fim)
    print ("")

def EscolherLetra(algumaLetra):
    # Retorna a letra que o jogador colocou. Este recurso faz com que o jogador insira uma letra e mais nada
    while True:
        print ('Adivinha uma letra: ')
        letra = input()
        letra = letra.lower()
        if len(letra) != 1:
            print ('Introduz uma única letra.') 
        elif letra in algumaLetra:
            print ('Você já escolheu essa letra, que tal tentar outra?')
        elif letra not in 'abcçdefghijklmnopqrstuvwxyz':
            print ('Escolha uma letra.')
        else:
            return letra

def Começar():
    # Esta função retorna True se o jogador quiser jogar novamente, caso contrário ele retorna False
    print ('Quer jogar de novo? (Sim ou Não)')
    return input().lower().startswith('s')

print ('JOGO DA FORCA')
letraIncorreta = ""
letraCorreta = ""
palavraSecreta = buscarpalavraAleat(palavras)
fimJogo = False
while True:
    displayBoard(JOGODAFORCA, letraIncorreta, letraCorreta, palavraSecreta)
    # O usuário escolhe uma letra.
    letra = EscolherLetra(letraIncorreta + letraCorreta)
    if letra in palavraSecreta:
        letraCorreta = letraCorreta + letra
        # É fixo se o jogador ganhar
        letrasEncontradas = True
        for i in range(len(palavraSecreta)):
            if palavraSecreta[i] not in letraCorreta:
                letrasEncontradas = False
                break
        if letrasEncontradas:
            print ('Muito bem! A palavra secreta é "' + palavraSecreta + '" Você Ganhou!')
            fimJogo = True
    else:
        letraIncorreta = letraIncorreta + letra
        # Verifica o número de letras que o jogador inseriu e se ele perdeu
        if len(letraIncorreta) == len(JOGODAFORCA) - 1:
            displayBoard(JOGODAFORCA, letraIncorreta, letraCorreta, palavraSecreta)
            print ('Não tem mais letras\nDepois de ' + str(len(letraIncorreta)) + ' letras erradas e ' + str(len(letraCorreta)) + ' letras corretas, a palavra era "' + palavraSecreta + '"')
            fimJogo = True
    # Pergunte ao jogador se ele quer jogar novamente
    if fimJogo:
        if Começar():
            letraIncorreta = ""
            letraCorreta = ""
            fimJogo = False
            palavraSecreta = buscarpalavraAleat(palavras)
        else:
            break