pessoa = {}

chave = 'nome'

pessoa[chave] = 'Marcos'
pessoa['sobrenome'] = 'Everaldo'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome'):
  print('Existe')
else:
  print('Terminou')