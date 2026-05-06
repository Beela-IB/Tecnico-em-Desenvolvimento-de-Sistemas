programa {
  funcao inicio() {
    inteiro num1, num2

    escreva ("Digite o primeiro número; ")
    leia (num1)

    escreva (" Digite o segundo número: ")
    leia (num2)

    se(num1>num2){
        escreva(num1, " é maior que ",num2)
    }
    senao se (num1<num2){
      escreva (num1," é menor que ",num2)
    }
    senao se (num1==num2){
      escreva ("Os números ",num1, " e ",num2, " são iguais.")
    }
  }
}
