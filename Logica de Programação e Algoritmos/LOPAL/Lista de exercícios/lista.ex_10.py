#Leia 6 n ́umeros e exiba apenas os n ́umeros pares.

for i in range(6):
    num = int(input("Digite um número: "))
    if(num%2 == 0):
        print(num)