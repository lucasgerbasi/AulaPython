def par_ou_impar():
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        print("Esse número é par.")
    else:
        print("Esse número é ímpar.")

par_ou_impar()

def ordem_decrescente():
    n = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))

    numeros = [n, n2]
    numeros.sort(reverse=True)

    print("{}, {}".format(numeros[0], numeros[1]))


ordem_decrescente()

def triangulo_formado():
    n = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    n3 = int(input("Digite mais um número: "))
    if n + n2 > n3 and n + n3 > n2 and n2 + n3 > n:
        print("Os lados formam um triângulo.")
        if n == n2 == n3:
            print("O triângulo é equilátero.")
        elif n == n2 != n3 or n == n3 != n2 or n2 == n3 != n:
            print("O triângulo é isósceles.")
        else:
            print("O triângulo é escaleno.")
    else:
        print("Os lados não formam um triângulo.")

triangulo_formado()

def peso_ideal():
    altura = int(input("Digite sua altura: "))
    sexo = input("Digite seu sexo: (H/M) ").upper()

    if sexo == "H":
        peso_ideal = (72.7 * altura) - 58
        print("Seu peso ideal é: {}".format(peso_ideal))
    
    elif sexo == "M":
        peso_ideal = (62.1 * altura) - 44.7
        print("Seu peso ideal é: {}".format(peso_ideal))

    else:
        print("Sexo inválido.")

peso_ideal()

def ordem_decrescente_3():
    n = int(input("Digite um número: "))
    n2 = int(input("Digite outro número: "))
    n3 = int(input("Digite mais um número: "))

    numeros = [n, n2, n3]
    numeros.sort(reverse=True)

    print("{}, {}, {}".format(numeros[0], numeros[1], numeros[2]))

ordem_decrescente_3()

def calcular_preco():
    # álcool: até 20 litros, desconto de 3% por litro
    # acima de 20 litros, desconto de 5% por litro
    # Gasolina: até 20 litros, desconto de 4% por litro
    # acima de 2 litros, desconto de 6% por litro
    # Gasolina = R$ 3,30 por litro, alcool = R$ 2,10

    Litros = int(input("Digite a quantidade de litros: "))
    Tipo = input("Digite o tipo de combustível: (A/G)  ").upper()

    if Tipo == "A":
        if Litros <= 20:
            preco = (Litros * 2.10) - (0.03 * Litros)

        else:
            preco = (Litros * 2.10) - (0.05 * Litros)

    elif Tipo == "G":
        if Litros <= 20:
            preco = (Litros * 3.30) - (0.04 * Litros)

        else:
            preco = (Litros * 3.30) - (0.06 * Litros)
    
    else:
        print("Tipo de combustível inválido.")

    print("O preço total é: R${}".format(preco))

calcular_preco()