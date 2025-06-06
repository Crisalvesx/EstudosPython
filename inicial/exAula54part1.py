
try:
    numero = input("Digite um numero inteiro: ")
    numeroInt = int(numero)
    
    if type(numeroInt) == int:

        if numeroInt % 2 == 0:
            print("Seu numero é par")
    
        else:
            print("Seu numero é impar")

except:
    print("O dado digitado esta incorreto")


