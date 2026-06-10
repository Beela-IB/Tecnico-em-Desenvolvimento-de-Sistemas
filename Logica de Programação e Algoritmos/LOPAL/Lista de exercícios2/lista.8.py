def calcular_estacionamento(horas):
    if horas <= 1:
        return 8.0
    else:
        return 8.0 + (horas - 1) * 3.0

placa = input("Digite a placa do veículo: ")
horas = int(input("Digite a quantidade de horas estacionadas: "))

valor = calcular_estacionamento(horas)

print("\n--- Resumo ---")
print(f"Placa: ", placa)
print(f"Horas estacionadas: ", horas)
print(f"Valor a pagar: R$ ", valor)