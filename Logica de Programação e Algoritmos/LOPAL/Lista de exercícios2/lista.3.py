dados_clientes = {}

dados_clientes["Nome do Pet"] = input("Digite o nome do pet: ")
dados_clientes["Espécie"] = input("Digite a espécie: ")
dados_clientes["Idade do Pet"] = int(input("Digite a idade do pet: "))
dados_clientes["Nome do Dono"] = input("Digite o nome do dono: ")

print("\n -----Dados do cliente -----")
print(dados_clientes["Nome do Pet"])
print(dados_clientes["Espécie"])
print(dados_clientes["Idade do Pet"])
print(dados_clientes["Nome do Dono"])
