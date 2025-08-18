def validar_cnpj(cnpj):
    cnpj = ''.join(filter(str.isdigit, cnpj))
    if len(cnpj) != 14 or cnpj == cnpj[0] * 14:
        return False

    def calc_digito(cnpj, pesos):
        return (11 - sum(int(cnpj[i]) * pesos[i] for i in range(len(pesos))) % 11) % 10

    pesos_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    digito_1 = calc_digito(cnpj, pesos_1)
    digito_2 = calc_digito(cnpj, pesos_2)

    return cnpj[12] == str(digito_1) and cnpj[13] == str(digito_2)

# Teste
cnpj_test = "12.345.678/0001-95"
print(f"CNPJ {cnpj_test} é {'válido' if validar_cnpj(cnpj_test) else 'inválido'}")
