'''
Flag - marcar um local(ver se entrou em um if, for ....)
is e is not = é ou não é (tipo, valor , identidade)
id = identidade

'''

v1 = 'a'
v2 = 'b'
v3 = 'b'#devido a otimização ele ja aponta para o mesmo local de v2 automaticamente

print(id(v1))
print(id(v2))
print(id(v3))