'''
try - tenta executar o codigo
except - ocorreu algum erro ao tentar executar

'''

num = input('vou dobrar o seguinte num:')

try: #testa o codigo para ve se possui algum erro
     numFloat = float(num)
     print(f"o dobro de {num} é {numFloat*2}")
except: # exibe a mensagem se ocorrer algum erro no try
     print("oq vc digitou n é um num")