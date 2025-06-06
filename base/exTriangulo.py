baseStr = input("Digite a base do triangulo retangulo: ")

base = int(baseStr)
i=1

while True:

    triangulo = i * '*'
    print(triangulo)
    i += 1 

    if (i - 1) == base:
        break