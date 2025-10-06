vet = []
for i in range (10):
    vet.append(int(input(f"Digite o {i+1}º número: ")))
def mediaElem(vet):
    elementos = 0
    media = 0
    for i in vet:
        elementos += i
    media = elementos/len(vet)
    print(f'A média dos números do vetor é {media}')

mediaElem(vet)
