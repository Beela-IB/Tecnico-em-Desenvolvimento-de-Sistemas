numero = []

for i in range(6):
    numero.append(int(input("Digite números: ")))

for i in range(6):
    if numero[i] < 0:
        print("Negativos: ", numero[i])
        numero[i] = 0
print(numero)