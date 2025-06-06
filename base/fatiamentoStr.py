'''
fatiamento [i:f:p] [::]
i = inicio f = final p = passo

ex :. 
012345678
ola mundo

função len() ---> retorna a qtd de caracteres de uma str

'''

ex = 'ola mundo'
print(ex[4:9]) # pode-se omitir o final tbm, q ela ja reconhece q é para ir ate o
               #final, ---> [4:]
print(ex[0:3]) # pode-se omitir o inicio tbm, q ela ja reconhece q é para começar
               # no inicio ---> [:3]
print(ex[0:9:2])# passo, vai de dois em dois

print(ex[::-1]) #inverte uma str
