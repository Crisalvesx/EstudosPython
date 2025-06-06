nome = input('Digite o seu nome:')

tamanhoNome = len(nome)

if tamanhoNome > 0 and tamanhoNome <= 4:
    print('Seu nome é curto!')

elif tamanhoNome == 5 or tamanhoNome == 6 :
    print('Seu nome é normal!')

else:
    print ("Seu nome é grande!")