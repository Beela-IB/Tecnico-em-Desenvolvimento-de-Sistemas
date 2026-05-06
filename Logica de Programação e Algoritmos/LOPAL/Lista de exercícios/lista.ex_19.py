#Leia 4 n ́umeros e ordene-os em ordem crescente.

numeros = []

for i in range(4):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

numeros.sort()

print("Números em ordem crescente:", numeros)
