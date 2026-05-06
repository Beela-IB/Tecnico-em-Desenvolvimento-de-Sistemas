print("-------------------------")
numeros = []
num_par = 0
for i in range(10):
    num = int(input("Digite um número: "))
    numeros.append(num)

for num in numeros:
    if(num%2 == 0):
        num_par = num_par + 1
print("Os números pares são: ", num_par)

    

