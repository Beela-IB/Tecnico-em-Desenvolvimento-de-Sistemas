#Leia 8 n ́umeros e exiba a soma apenas dos n ́umeros pares.

numeros = []
soma = 0

for i in range(8):
    num = int(input("Digite um número: "))
    numeros.append(num)

for num in numeros:
    if(num %2 == 0):
        soma = soma + num
print("A soma dos números pares é =",soma)