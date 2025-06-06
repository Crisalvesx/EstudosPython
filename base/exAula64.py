nome = input("Digite um nome: ")

i = 0

print('O nome digitado foi:', nome)
print('O nome modificado eh:', end=' ')
while True:

    print('*' + nome[i], end='')
    i += 1

    if i == len(nome):
        break

print('')

    

