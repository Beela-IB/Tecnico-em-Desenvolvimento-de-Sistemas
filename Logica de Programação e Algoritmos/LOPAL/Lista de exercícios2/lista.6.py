def gerar_resumo(nome, tipo, valor):
    print("\n--- Resumo da Compra ---")
    print(f"Cliente: {nome}")
    print(f"Tipo de ingresso: {tipo}")
    print(f"Valor do ingresso: R$ {valor:.2f}")

nome = input("Digite o nome do cliente: ")
tipo = int(input("Digite o tipo de ingresso (1-Normal, 2-Estudante, 3-Idoso): "))

match tipo:
    case 1:
        tipo_ingresso = "Normal"
        valor = 30.00
    case 2:
        tipo_ingresso = "Estudante"
        valor = 15.00
    case 3:
        tipo_ingresso = "Idoso"
        valor = 10.00
    case _:
        tipo_ingresso = "Inválido"
        valor = 0

gerar_resumo(nome, tipo_ingresso, valor)