programa {
  funcao inicio() {
    inteiro lado1, lado2, lado3

    escreva (" Digite lado 1: ")
    leia (lado1)

    escreva ("Digite lado 2: ")
    leia (lado2)

    escreva ("Digite lado 3: ")
    leia (lado3)

    se (lado1==lado2 e lado1==lado3 e lado2==lado3){
    escreva ("Triângulo equilátero")
    }

    senao se (lado1==lado2 ou lado1==lado3 e lado2==lado3){
      escreva ("Triângulo isósceles")
    }
    senao se (lado1!=lado2 e lado2!=lado3 e lado1!=lado3){
      escreva ("Triângulo escaleno")
    }
  }
}
