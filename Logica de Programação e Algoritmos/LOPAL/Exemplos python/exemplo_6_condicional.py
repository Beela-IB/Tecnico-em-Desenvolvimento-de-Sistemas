valorcompra = float(input("Digite o valor da compra: "))
cupomdesconto = input("Possui cupom de desconto? ")

if(valorcompra >= 200 or cupomdesconto == "Sim"):
    print("Você ganhou 15% de desconto!")
else:
    print("Você não tem direito a descontos no momento!")