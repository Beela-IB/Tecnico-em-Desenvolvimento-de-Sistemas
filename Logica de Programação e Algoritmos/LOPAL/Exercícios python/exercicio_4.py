posicao_inicial = float(input("Posição inicial: "))
posicao_final = float(input("Posição final: "))
tempo_inicial = float(input("Tempo inicial: "))
tempo_final = float(input("Tempo final: "))

velocidade_media = (posicao_final-posicao_inicial)/(tempo_final-tempo_inicial)
print("Velocidade média: ", velocidade_media)