'''

variaveis q nao vao mudar devem ser escritas em caps lock (bom habito)

muitas condiçoes no mesmo if(ruim)
.... <- contagem de complexidade(ruim)

'''

velocidade = 61
localCarro = 100

#constantes
RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidadeCarroEstrada = velocidade > RADAR_1

localCarroEstrada = localCarro >= (LOCAL_1 - RADAR_RANGE) and \
       localCarro <= (LOCAL_1 + RADAR_RANGE)


if velocidadeCarroEstrada :

    print("Vc passou no radar 1!")

    if localCarroEstrada:

        print("vc foi multado")

    else: 
        print('vc passou tranquilo!')

else :
    print('vc passou tranquilo!')
