#Revisão vetores - 1
#Solicitar ao usuário a quantidade de números
#Preencher o vetor
#Percorrer o vetor e calcular a soma dos números
#Exibir a soma
#------------------------------------------------

#Passo 1) Criar as variáveis

qtd = int(input("Digite a quantidade de números "))
numeros = []
soma = 0

#Passo 2) Preencher o vetor
for i in range(qtd):
    numeros.append(int(input("Digite um número: ")))

#Passo 3) Percorrer o vetor
for numero in numeros:
    soma = soma + numero

print("A soma é ", soma)