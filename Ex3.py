renas = ["Dasher", "Dancer", "Prancer", "Vixen", "Comet", "Cupid", "Donner", "Blitzen", "Rudolph"]
maiorQuantBolas = -1
for i in range(len(renas)):
    bolas = int(input("Digite a quantidade de bolas na rodada {}: ".format(i)))
    maiorQuantBolas = bolas
    if bolas > maiorQuantBolas:
        maiorQuantBolas = bolas

print(maiorQuantBolas)
RenaVencedor = renas[maiorQuantBolas - 1]
print("A maior quantidade de bolas foi: {}, a rena vencedora é {}".format(maiorQuantBolas, RenaVencedor))



def fibonacci(n):
    a, b = 1, 1
    while b < n:
        a, b = b, a + b
    return b == n

def achar_fibonot(k):
    count = 0
    num = 1
    while count < k:
        num += 1
        if not fibonacci(num):
            count += 1
    return num

k = int(input("Digite um número: "))
fibonot = achar_fibonot(k)
print(fibonot)

nums = []
cont = 0
soma = 0

for i in range(0, 10, 1):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        nums.append(num)
        soma = soma + num
        cont = cont + 1

media = soma / cont

print("A média dos números pares é: {}".format(media))

nums = []
cont = 0
soma = 0

while (num != 0):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        nums.append(num)
        soma = soma + num
        cont = cont + 1

media = soma / cont

print("A média dos números pares é: {}".format(media))

import random

num = random.randint(1, 10)

chute = 0
while (chute != num):
    chute = int(input("Tente adivinhar o número: "))
    if chute > num:
        print("O chute foi alto.")
    elif chute < num:
        print("O chute foi baixo.")
    else:
        print("Parabéns, você acertou.")


def Estoque_vinho():
    total = totalTinto = TotalBranco = TotalRose = 0
    tipo = ''
    while tipo != 'F':
        tipo = input('Qual o tipo de vinho? (T - Tinto, B - Branco, R - Rosé, F - Finalizar) ').upper()
        if tipo == 'T':
            totalTinto = totalTinto + 1
            total = total + 1
        elif tipo == 'B':
            TotalBranco = TotalBranco + 1
            total = total + 1
        elif tipo == 'R':
            TotalRose = TotalRose + 1
            total = total + 1
        if tipo == 'F':
            break
        else:
            print('Tipo inválido.')

    print('Total de vinhos: {}'.format(total))
    print('Porcentagem de vinho tinto: {}%'.format(totalTinto * 100 / total))
    print('Porcentagem de vinho branco: {}%'.format(TotalBranco * 100 / total))
    print('Porcentagem de vinho rosé: {}%'.format(TotalRose * 100 / total))

Estoque_vinho()

def tabuada5():
    for i in range(1, 11):
        print("{} x 5 = {}".format(i, i * 5))

    j = 1
    while j != 11:
        print("{} x 5 = {}".format(j, j * 5))
        j += 1

tabuada5()  

def tabuada():
    num = int(input("Digite um número: "))
    while num != -1:
        for i in range(1, 11):
           print("{} x {} = {}".format(i, num, i * 5))

        while i != 11:
            print("{} x {} = {}".format(i, num, i * 5))
            i += 1
    
tabuada()
