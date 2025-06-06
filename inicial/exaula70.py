
j = 0
frase = input('Digite uma frase desejada:')
letraMaisAtual = ''
quantLetraMaisAtual = 0

while j < len(frase):

    letraAtual = frase[j]

    if letraAtual == ' ':
        j += 1
        continue

    quantLetraAtual = frase.count(frase[j])

    if quantLetraMaisAtual < quantLetraAtual :
        quantLetraMaisAtual = quantLetraAtual
        letraMaisAtual = frase[j]

    j += 1

print('a letra q mais apareceu foi', letraMaisAtual)
print(f'ela apareceu {quantLetraMaisAtual}x')
