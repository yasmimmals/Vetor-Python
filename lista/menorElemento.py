numeros = [1 , 3 ,4, 5]
menores = []
for n in numeros:
    if n < 4:
        menores.append(n)
        print(n)


#ou assim:
menores2 = [n for n in numeros if n<4]
print(menores2)