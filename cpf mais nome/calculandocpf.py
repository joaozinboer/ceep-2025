#Main
TAM_CPF = 14
cpf = input("Por favor insira o cpf: ")
flag = True

if(len(cpf) != TAM_CPF):
    flag = False
elif((cpf[3] != ".") or (cpf[7] != ".") or (cpf[-3] != "-")):
    flag = False
else:
    for i in range(TAM_CPF):
        if((i != 3) and (i != 7) and (i != 11)):
            c = cpf[i]
            if(not c.isdigit()):
                flag = False

if(flag):
    print("Formato de CPF Válido.")
else:
    print("O CPF informado não tem um formato válido.")