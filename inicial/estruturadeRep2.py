'''
laços internos

'''

qtdLinhas = 5
qtdColunas = 5

linha = 1  


while linha <= qtdLinhas :
    coluna = 1
    while coluna <= qtdColunas:
        print(f'{linha = } {coluna = }')
        coluna += 1
    linha += 1
    
print("Fim!")   