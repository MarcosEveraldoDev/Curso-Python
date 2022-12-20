senha = input('Digite sua senha : ') 

senha_permitida = '123456'

if not senha:
  print('Senha nao digitada')
elif senha == senha_permitida:
  print('Senha correta !')
else:
  print('Senha incorreta !')
