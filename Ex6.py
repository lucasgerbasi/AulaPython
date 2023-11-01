# Fazer um programa que possui um menu com as seguintes opções para executar diferentes funções, até que o usuário digite -1 e termine o programa:
# ◦ Escrever a tabuada de um número ou uma mensagem de erro caso o número não esteja entre 1 e 9. O número deve ser passado como parâmetro e a validação feita na função.
# ◦ Calcular o Índice de Massa Corporal (IMC): a fórmula é IMC = peso / altura2. Passar o peso e altura como parâmetros e retornar o IMC.
# ◦ Calcular o fatorial de um número. O número deve ser passado como parâmetro e retornar o resultado.


def tabuada(num):
    for i in range(1, 10):
        print("{} x {} = {}".format(num, i, num * i))
    
def imc(peso, altura):
    imc = peso / (altura ** 2)
    print("Seu IMC é: {}".format(imc))

def fatorial(num):
    fat = 1
    for i in range(1, num + 1):
        fat *= i
    print("O fatorial de {} é {}".format(num, fat))

def programa_menu():
    
    escolha = 0
    while escolha != -1:
        print("1 - Tabuada de um número entre 1 e 9")
        print("2 - Calcular IMC")
        print("3 - Calcular Fatorial")
        print("-1 - Terminar Programa")
        escolha = int(input("Escolha uma das opções: "))

        if escolha == 1:
            num = int(input("Insira um número: "))
            tabuada(num)
        elif escolha == 2:
            peso = float(input("Insira seu peso: "))
            altura = float(input("Insira sua altura: "))
            imc(peso, altura)
        elif escolha == 3:
            num = int(input("Insira um número: "))
            fatorial(num)
        elif escolha == -1:
            print("Programa encerrado")
        else:
            print("Opção inválida")

programa_menu()

#  Fazer uma função que receba o valor de N como parâmetro, calcular e retorne o valor do somatório S:

N = int(input("Insira um número: "))

def somatoria(N):
    S = 0
    for i in range(N):
        S += i
    return S

resultado = somatoria(N)
print(resultado)

# Fazer uma função que verifique se o número de um CPF é válido.

def cpf_valido():
    cpf = input("Insira seu CPF: ")

    soma = 0
    for i, digito in enumerate(cpf[:9]):
        soma += int(digito) * (10 - i)

    resto = soma % 11
    primeiro_digito_verificador = 0 if resto < 2 else 11 - resto

    soma = 0
    for i, digito in enumerate(cpf[:10]):
        soma += int(digito) * (11 - i)

    resto = soma % 11
    segundo_digito_verificador = 0 if resto < 2 else 11 - resto

    if cpf[9] == str(primeiro_digito_verificador) and cpf[10] == str(segundo_digito_verificador):
        print("{} é um CPF válido.".format(cpf))
    else:
        print("{} é um CPF inválido.".format(cpf))

cpf_valido()

# Fazer uma função que verifica se uma palavra, frase ou número é um palíndromo.

def palindromo():
    palavra = input("Insira uma palavra, frase ou número: ")
    invertida = palavra[::-1]
    if palavra == invertida:
        print("{} é um palíndromo.".format(palavra))
    else:
        print("{} não é um palíndromo.".format(palavra))

palindromo()