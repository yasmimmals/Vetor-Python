def validacao1(cpf):
    soma =0
    peso=10 

    for i in range(9):
        soma = soma+ int(cpf[i])*peso
        peso = peso-1
    
    resto = soma%11

    if resto < 2:
        digito1= 0
    
    else:
        digito1 =11- resto

    soma =0
    peso=11

    for i in range(9):
        soma = soma+ int(cpf[i]) *peso
        peso = peso -1
    
    soma = soma + digito1*2
    resto = soma %11

    if resto<2:
        digito2 =0 
    
    else:
        digito2 = 11- resto 

    return digito1, digito2

def main():
    cpf= input("digite o cpf ")
    if len(cpf) != 11:
        print("cpf invalido")
        return
   
    digito1, digito2 = validacao1(cpf)

    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        print("cpf valido")
    
    else:
        print("cpf invalido")

main()