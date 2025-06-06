'''

while condição:
    ...
break -> interrompe o while mais próximos
continue -> executa tudo antes do continue normalmente, ao ver o continue ele 
volta para o inicio do laço

ex.:(break)

while :
...
break

'''

contador = 0

while True  :
     print('hello')
     break
     print(' kkk') #nao sera executado 

print('executou isso')# sera executado por estar fora do while interrompido

while True:
     
     contador += 1 

     if contador == 3:
          continue #nao executa nada abaixo
          print('rsrs') # nao executa

     print(contador) # nao mostrara o 3

     if contador == 5:
          break

else :
     print("o else foi executado") # esse else é executado ao fim do while