medicamentos = []

for i in range(4):
    print(f"\nCadastro do medicamento {i + 1}")

    nome = input("Nome: ")
    fabricante = input("Fabricante: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: R$ "))

    medicamento = {
        "nome": nome,
        "fabricante": fabricante,
        "quantidade": quantidade,
        "preco": preco
    }

    medicamentos.append(medicamento)

print("\nMedicamentos com quantidade menor que 10:\n")

for med in medicamentos:
    if med["quantidade"] < 10:
        print("Nome: ", nome)
        print("Fabricante: ", fabricante)
        print("Quantidade: ", quantidade)
        print("Preço: ", preco)
        print("\n")