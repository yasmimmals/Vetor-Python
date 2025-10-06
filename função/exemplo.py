def exemplo(a, b):
    if(a > b):
        print(f'O menor valor é o segundo: {b}')
    elif (a == b):
        print("Os valores são iguais")
    else:
        print(f'O menor valor é o primeiro: {a}')


a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
exemplo(a, b)
 