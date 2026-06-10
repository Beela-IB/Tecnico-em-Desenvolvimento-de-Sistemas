#Criar a função
def aplicarDesconto(nome_peca, valor_original):
    valor_desconto = (valor_original * 0.10)
    valor_pagar = (valor_original - valor_desconto)
    print("O valor com desconto é: ", valor_pagar)

#Chamar a função 
    
nome_peca = input("Digite o nome da peça: ")
valor_original = float(input("Digite o valor original da peça: "))
aplicarDesconto(nome_peca, valor_original)

