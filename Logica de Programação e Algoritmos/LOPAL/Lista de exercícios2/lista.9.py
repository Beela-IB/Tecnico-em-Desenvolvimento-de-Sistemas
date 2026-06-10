dados_pizza = {}

dados_pizza["Sabor"] = input("Digite o sabor da pizza: ")
dados_pizza["Tamanho"] = input("Digite o tamanho da pizza: \n P - Pequena \n M - Média \n G - Grande \n")

print("\n -----Dados da pizza -----")
print(dados_pizza["Sabor"])
print(dados_pizza["Tamanho"])

match dados_pizza["Tamanho"]:
    case "P":
        print("Preço = 29.90")
    case "M":
        print("Preço = 59.90")
    case "G":
        print("Preço 79.90")