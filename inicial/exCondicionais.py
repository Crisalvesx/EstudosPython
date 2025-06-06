primeiro_valor = input("qual o primeiro valor?: ")
segundo_valor = input("qual o segundo valor?: ")

if primeiro_valor > segundo_valor :
    print(f"O {primeiro_valor =} é maior que o {segundo_valor =}")

elif primeiro_valor < segundo_valor :
    print(f"O {segundo_valor =} é maior que o {primeiro_valor =}")

elif primeiro_valor == segundo_valor:
    print(f"Os valores são iguais")

else :
    print("Algo deu errado")