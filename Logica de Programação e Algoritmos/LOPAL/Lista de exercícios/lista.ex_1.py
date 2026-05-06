#Leia dois n ́umeros inteiros e exiba a soma, subtra ̧c ̃ao, multiplica ̧c ̃ao e divis ̃ao entre eles.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

soma = num1+num2
sub = num1-num2
div = num1/num2
mult = num1*num2

print(num1,"+",num2,"=",soma)
print(num1,"-",num2,"=",sub)
print(num1,"/",num2,"=",div)
print(num1,"x",num2,"=",mult)