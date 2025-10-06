vet = []
for i in range (10):
    vet.append(int(input(f"Digite o {i+1}º número: ")))
def mediaPar(vet):
    pares = 0
    cont = 0
    media = 0
    for i in vet:
        if i % 2 == 0:
            pares += i
            cont += 1
    media = pares/cont
    print(f'A média dos números do vetor é {media}')

mediaPar(vet)
