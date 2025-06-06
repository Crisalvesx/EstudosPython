while True:
    Num1str = input("Digite um numero: ")
    Num2str = input('Digite o segundo numero: ')
    result = 0

  
    if  Num1str.isdigit() and  Num2str.isdigit():
        
        operadores = ['+','-','*','/'] 
        Num1 = float(Num1str)
        Num2 = float(Num2str)

        escolhaOperador = input('Escolha um operador para a sua operação (adição(+),\
subtração(-), Multiplicação(*) ou divisão(/)): ')

        if escolhaOperador in operadores:
            if escolhaOperador == '+':
                result = Num1 + Num2

            elif escolhaOperador == '-':
                result = Num1 - Num2   

            elif escolhaOperador == '*':
                result = Num1 * Num2
            
            elif escolhaOperador == '/':
                result = Num1 / Num2 

            else:
                print('Algo deu errado. Por favor tente novamente')
                continue
        
        else:
            print("Você digitou um operador invalido. Por favor selecione um operador correto")
            continue
    
    else:
        print("Por favor digite um número.")
        continue

    print("O resultado da sua operação é:", result)
    escolhaContinuidade = input("Você deseja continuar utilizando a Calculadora? (Sim / Não) ").lower()

    escolhasSim = ['sim','si','s']
    escolhasNao = ['nao','não','no','n','nop']

    if escolhaContinuidade in escolhasSim:
        continue
    
    elif escolhaContinuidade in escolhasNao:
        print("Obrigado pelo acesso!")
        break

    else:
        print('Opção errada. Devido a isso encerraremos o software')
        break