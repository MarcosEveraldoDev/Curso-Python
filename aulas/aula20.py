print('-------LOGIN--------')
print('')
nome_digitado = input('Digite seu nome: ')
senha_digitada = input('Digite sua senha: ')

nome_permitido1 = 'marcos'
nome_permitido2 = 'rodolfo'
senha_permitida = '92425259'

if (nome_digitado == nome_permitido1 or nome_digitado == nome_permitido2) and senha_digitada == senha_permitida:
  print('')
  print('------ACESSO PERMITIDO------')  
  print("")
else: 
  print('')
  print('------ACESSO NEGADO------')
  print('')