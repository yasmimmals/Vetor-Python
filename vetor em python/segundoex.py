vet = []
soma = 0
qtdPares = 0
media = 0

for i in range(5):
    vet.append(int(input('Informe um valor: '))) # adiciona um item no vetor
    

for i in range(5):
    if vet[i] % 2 == 0:
        soma += vet[i]
        qtdPares += 1
        media = soma / qtdPares
print('\nVetor')
print(f'A média dos números pares é: {media}')