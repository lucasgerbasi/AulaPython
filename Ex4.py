import random

def soma_valores():
    vet = []
    for i in range(10):
        n1 = input("Insira um valor: ")
        vet.append(int(n1))

    soma = sum(vet)
    print("A soma dos números é: {}".format(soma))

soma_valores()

def media_pares():
    vet = []
    soma = cont = 0
    for i in range(10):
        n1 = input("Insira um valor: ")
        vet.append(int(n1))
        if int(n1) % 2 == 0:
            soma += int(n1)
            cont += 1

    media = soma / cont

    print("A média dos números pares: {}".format(media))

media_pares()

def media_de_classe():
    notas = []
    soma = cont = 0
    quantAlunos = int(input("Insira a quantidade de alunos: "))
    for i in range(quantAlunos):
        nota = int(input("Insira a nota do aluno {}: ".format(i)))
        notas.append(nota)
        soma += nota
    
    media = soma / quantAlunos
    print("A média da classe é: {}".format(media))
    
media_de_classe()

def vetor_vezes_3():
    vet = []
    for i in range(10):
        n1 = random.randint(1, 10)
        vet.append(int(n1))

    print("Vetor: {}".format(vet))

    for i in range(len(vet)):
        vet[i] = vet[i] * 3

    print("Vetor vezes 3: {}".format(vet))

vetor_vezes_3()

def soma_entre_vetores():
    vet = []
    vet2 = []
    for i in range(50):
        n1 = random.randint(1, 10)
        vet.append(int(n1))

    print("Vetor 1: {}".format(vet))

    for i in range(50):
        n1 = random.randint(1, 10)
        vet2.append(int(n1))

    print("Vetor 2: {}".format(vet2))

    soma = 0

    for i in range(len(vet)):
        soma += vet[i] + vet2[i]

    print("A soma entre os vetores é: {}".format(soma))

soma_entre_vetores()

def preencher_vetor_binario():
    vet = []
    for i in range(100):
        if i % 2 == 0:
            vet.append(1)
        else:
            vet.append(0)

    print("Vetor binário: {}".format(vet))

preencher_vetor_binario()

def preencher_vetor_fibonacci():
    vet = []
    n = int(input("Insira o tamanho do vetor: "))
    for i in range(n):
        if i == 0:
            vet.append(1)
        elif i == 1:
            vet.append(1)
        else:
            vet.append(vet[i - 1] + vet[i - 2])

    print("Vetor fibonacci: {}".format(vet))

preencher_vetor_fibonacci()
