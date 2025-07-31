from datetime import datetime

# Solicita ao usuário a data de nascimento no formato dia/mês/ano
data_nascimento_str = input("Digite sua data de nascimento (dd/mm/aaaa): ")

# Converte a string para um objeto de data
data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

# Pega a data atual
data_atual = datetime.today()

# Calcula a idade
idade = data_atual.year - data_nascimento.year

# Ajusta se ainda não fez aniversário este ano
if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
    idade -= 1

# Exibe o resultado
print(f"Você tem {idade} anos.")

if idade > 50:
    print("voce esta perto de se aposentar")