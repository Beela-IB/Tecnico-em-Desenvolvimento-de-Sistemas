#Leia 5 n ́umeros e exiba o maior valor.

maior = -99999999999999999999999999999999999999999

for i in range(5):
    num = int(input("Digite um número: "))
    if(num > maior):
        maior = num
print("Maior: ",maior)