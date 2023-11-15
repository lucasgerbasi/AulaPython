# Nome: Lucas Henrique Passos Gerbasi
# Código: 24732

# Exercício 1

def LeituraValor():
    ValorPrest = int(input("Digite o valor da prestação: "))
    NumDias = int(input("Digite o número de dias em atraso: "))
    return ValorPrest, NumDias

def valorPagamento():
    ValorPrest = -1
    resultado = []
    while ValorPrest != 0:
        ValorPrest, NumDias = LeituraValor()

        if NumDias == 0:
            resultado.append(ValorPrest)
    
        elif NumDias > 1:
            resultado.append(ValorPrest * (1 + 0.03 * (NumDias - 0.1)))

        print("Valor a ser pago: ", resultado[len(resultado) - 1])

    return resultado
        

valorPagamento()



# Exercício 2
def modaVetor():
    lista = []
    for i in range(5):
        lista.append(int(input("Digite um valor: ")))

    moda = []
    maiorQuantNum = 0

    for num in lista:
        cont = 0
        for outro_num in lista:
            if num == outro_num:
                cont += 1
        
        if cont > maiorQuantNum:
            maiorQuantNum = cont
            moda = [num]
        elif cont == maiorQuantNum and num not in moda:
            moda.append(num)

    if maiorQuantNum == 1:
        print("Não existe moda.")
        return None
    else:
        print("Moda:", moda)
        return moda

modaVetor()


# Exercício 3

import random

def adivinharPalavra():
    palavras = ["abacaxi", "banana", "manga", "morango", "abacate", "pera", "uva", "laranja", "melancia", "kiwi"]
    palavra = palavras[random.randint(0, len(palavras) - 1)]
    tentativas = random.randint(6, 11)
    letras_corretas = []
    jogo = "_" * len(palavra)

    print("Tente adivinhar palavra. Voce tem {} tentativas.".format(tentativas))

    while tentativas > 0:
        print("Palavra: " + jogo)
        letra = input("Digite uma letra: ")
        
        if letra in letras_corretas:
            print("-------------------")
            print("Letra repetida. Tente novamente.")
            continue

        if letra in palavra:
            print("-------------------")
            print("Letra correta. Tentativas restantes: ", tentativas)
            letras_corretas.append(letra)
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    jogo = jogo[:i] + letra + jogo[i+1:]
        else:
            print("-------------------")
            tentativas -= 1
            print("Letra errada. Tente novamente. Tentativas restantes: ", tentativas)

        if len(letras_corretas) == len(set(palavra)):
            print("-------------------")
            print("Parabens! Voce acertou a palavra.")
            print("A palavra era: ", palavra)
            break

        if tentativas == 0:
            print("-------------------")
            print("Voce perdeu. A palavra era: ", palavra)
            break


adivinharPalavra()