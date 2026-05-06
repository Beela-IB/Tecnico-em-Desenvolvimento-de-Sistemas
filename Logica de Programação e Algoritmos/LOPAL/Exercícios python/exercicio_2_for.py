num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
soma = 0

for i in range(num1,num2+1):
    if(i%2 == 0):
        soma = soma + i
print("A soma de todos os números pares é: ", soma)