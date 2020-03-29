import random





def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    letras_faltando = str(letras_acertadas.count('_'))
    print( 'Ainda faltam acertar {} letras'.format(letras_faltando))

    while(not enforcou and not acertou):

        chute = pede_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(len(palavra_secreta) - erros))

        enforcou = (erros == len(palavra_secreta))
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor()





def imprime_mensagem_perdedor():
    print("Você perdeu!")

def imprime_mensagem_vencedor():
    print("Você ganhou!")

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def  imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo =  open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha =  linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

# for letra in palavra_secreta:
#    letras_acertadas.append("_")

if(__name__ == "__main__"):
    jogar()
