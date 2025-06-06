nome = input("Escreva o seu nome:")
idade = input("Digite a sua idade:")

if nome and idade : # nome e idade = true (foram digitados)
    
    print(f"Seu nome é {nome}")
    print(f'Seu nome invertido é', nome[::-1])
    
    if ' ' in nome:
        print("seu nome possui espaços")
    
    else:
        print('Seu nome não possui espaços')

    print('Seu nome tem', len(nome), 'letras')
    print('A primeira letra do seu nome é', nome[0])
    print('A ultima letra do seu nome é', nome[-1]) 


else : # nome ou idade = false (pelo menos um dos dois n foi digitado)
    
    print("desculpe, vc deixou campos vazios")