# Pedindo informações do produto

nome_bebida = input("Digite o nome da bebida: ")
valor_bebida = float(input("Digite o preço unitário da bebida: "))
qtd_bebida = int(input("Digite a quantidade de bebidas: "))

calcular_total = (valor_bebida * qtd_bebida)

print("Valor a pagar: ", calcular_total)