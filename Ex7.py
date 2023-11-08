def prog():
    nomes = []
    idades = []
    nomesAbaixoMedia = []
    contPessoasAcimaMedia = 0
    soma = 0
    for i in range(3):
        nome = input("Insira o nome: ")
        idade = int(input("Insira a idade: "))
        soma += idade
        nomes.append(nome)
        idades.append(idade)
    
    media = soma / 3
    print("A media das idades é: {}".format(media))
    
    maior = idades[0]
    menor = idades[0]
    for i in range(3):
        if idades[i] > media:
            contPessoasAcimaMedia += 1
        if idades[i] < media:
            nomesAbaixoMedia.append(nomes[i])
        if idades[i] > maior:
            maior = idades[i]
        if idades[i] < menor:
            menor = idades[i]

    print("Quantidade de pessoas com idades acima da média: {}".format(contPessoasAcimaMedia))
    print("Nome das pessoas com idades abaixo da média: {}".format(nomesAbaixoMedia))
    print("Maior idade: {}".format(maior))
    print("Menor idade: {}".format(menor))

    for i in idades:
        fatorial = 1 
        for j in range(1, i+1):
            if i % j == 0:
                fatorial *= j
        print("Idade: {} | Fatorial: {}".format(i, fatorial))


prog()