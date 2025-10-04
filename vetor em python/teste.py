soma = 0
qtdPar = 0
for num in range(1, 11, 1):
        numeroDigitado= int(input(f"Digite o {num}º número: "))

        if numeroDigitado % 2 == 0:
         print(f"O número {numeroDigitado} é par e vai ser adicionado na média! ")
         soma += numeroDigitado
         qtdPar += 1
        else:
            print(f'O número {numeroDigitado} é ímpar e será ignorado')
if qtdPar > 0:
    media = soma / qtdPar
    print(f'\nA média aritmética dos números pares digitados é: {media:.2f}')
else:
    print("\nNenhum número par foi digitado.")