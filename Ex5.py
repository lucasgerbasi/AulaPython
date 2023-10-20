def maior_e_menor_num():
    vet = []
    maiornum = menornum = 0
    for i in range(20):
        num = int(input("Digite um número: "))
        vet.append(num)
        if num > maiornum:
            maiornum = num
        elif num < menornum:
            menornum = num
        
    print("O maior número é: {}".format(maiornum))
    print("O menor número é: {}".format(menornum))

maior_e_menor_num()

# def dobro_e_triplo_vet():
#     vet = []
#     vetDobro = []
#     vetTriplo = []
#     for i in range(5):
#         num = int(input("Digite um número: "))
#         vet.append(num)
    
#     for i in range(5):
#         vetDobro.append(vet[i] * 2)
#         vetTriplo.append(vet[i] * 3)
    
#     print("O dobro do vetor é: {}".format(vetDobro))
#     print("O triplo do vetor é: {}".format(vetTriplo))

# dobro_e_triplo_vet()

# def vetor_invertido():
#     vet = []
#     for i in range(30):
#         num = int(input("Digite um número: "))
#         vet.append(num)
#     vet.reverse()
#     print(vet)

# vetor_invertido()

# def vetor_invertido_sem_funcao():
#     vet = []
#     vetInvertido = []
#     for i in range(30):
#         num = int(input("Digite um número: "))
#         vet.append(num)
#     for i in range(30):
#         vetInvertido.append(vet[29 - i])

#     print(vetInvertido)

# vetor_invertido_sem_funcao()

# def dividir_vetor_par_impar():
#     vet = []
#     vetPar = []
#     vetImpar = []

#     for i in range(20):
#         num = int(input("Digite um número: "))
#         vet.append(num)
#         if num % 2 == 0:
#             vetPar.append(num)
#         else:
#             vetImpar.append(num)
    
#     print("Vetor par: {}".format(vetPar))
#     print("Vetor impar: {}".format(vetImpar))

# dividir_vetor_par_impar()

# def notas_media():
#     vet = []
#     cont = soma = media = contAcima = contAbaixo = 0
#     for i in range(10):
#         num = int(input("Digite uma nota: "))
#         vet.append(num)
#         soma += num
#         cont += 1
    
#     media = soma / cont
#     dez_porcento = media * 0.1
#     print("Média: {}".format(media))
#     print("10 por cento da média: {}".format(dez_porcento))

#     for i in range(10):
#         if vet[i] >= media + dez_porcento:
#             contAcima += 1

#         if vet[i] <= media - dez_porcento:
#             contAbaixo += 1

#     print("Quantidade de notas 10 por cento acima da média: {}".format(contAcima))
#     print("Quantidade de notas 10 por cento abaixo da média: {}".format(contAbaixo))

# notas_media()

