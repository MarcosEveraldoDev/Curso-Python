print('-------LOGIN--------')
print('')
nome_digitado = input('Digite seu nome: ')
senha_digitada = input('Digite sua senha: ')

nome_permitido = 'marcos'
senha_permitida = '92425259'

if nome_digitado == nome_permitido and senha_digitada == senha_permitida:
  print('')
  print('------ACESSO PERMITIDO------')
  print("")
else: 
  print('')
  print('------ACESSO NEGADO------')
  print('')