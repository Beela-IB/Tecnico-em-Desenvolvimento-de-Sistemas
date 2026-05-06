programa {
  funcao inicio() {
    inteiro num1, num2, soma_pares = 0

    escreva ("Digite um número:")
    leia (num1)

    escreva ("Digite um número: ")
    leia (num2)

    para (inteiro i=num1;i<=num2;i++){
      se(i%2 == 0){
        soma_pares = soma_pares + i
      }
    }
    escreva ("A soma dos pares é: ", soma_pares)
  }
}
