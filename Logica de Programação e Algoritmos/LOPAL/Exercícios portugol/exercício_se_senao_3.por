programa {
  funcao inicio() {
    inteiro numero

    escreva ("Digite um número: ")
    leia (numero)

    se (numero==1){
      escreva ("Domingo")
    }
    senao se (numero==2){
      escreva ("Segunda-Feira")
    }
    senao se (numero==3){
      escreva ("Terça-Feira")
    }
    senao se (numero==4){
      escreva ("Quarta-Feira")
    }
    senao se (numero==5){
      escreva ("Quinta-Feira")
    }
    senao se (numero==6){
      escreva ("Sexta-Feira")
    }
    senao se (numero==7){
      escreva ("Sábado")
    }
    senao {
      escreva ("Dia inválido")
    }
  }
}
