
try:
    horario = input("Digite o horario de agora: ")
    horarioInt = int(horario)
    
    if horarioInt >= 0 and horarioInt <= 11:
        print("Bom dia!")

    elif horarioInt >= 12 and horarioInt <=17:
        print('Boa tarde!')

    elif horarioInt >= 18 and horarioInt <= 23:
        print('Boa noite!')
    
    else :
        print('O número digitado está fora do fuso-horário!')

except:
    print("Você não digitou um número válido!")

