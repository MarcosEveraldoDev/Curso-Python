print('-------Calculadora-------')
numero_1 = input('Digite o primeiro numero : ')
numero_2 = input('Digite o segundo numero : ')
operador = input('Digite o operador que irá utilizar ( + - / *) : ')

novo_numero_1 = float(numero_1)
novo_numero_2 = float(numero_2)

while operador == '+':
  print(novo_numero_1 + novo_numero_2)
  
  break
while operador == '-':
  print(novo_numero_1 - novo_numero_2)
  break

while operador == '*':
  print(novo_numero_1 * novo_numero_2)
  break

while operador == '/':
  print(novo_numero_1 / novo_numero_2)
  break
  
reutilizar = input('Deseja utilizar a caulculadora novamente s/n ?')

while reutilizar == 's':
  print('-------------------------------------------')
  print('-------Calculadora-------')

  numero_1 = input('Digite o primeiro numero : ')
  numero_2 = input('Digite o segundo numero : ')
  operador = input('Digite o operador que irá utilizar ( + - / *)  : ')

  novo_numero_1 = float(numero_1)
  novo_numero_2 = float(numero_2)
  
  while operador == '+':
      print(novo_numero_1 + novo_numero_2)
  
      break
  while operador == '-':
        print(novo_numero_1 - novo_numero_2)
        break

  while operador == '*':
    print(novo_numero_1 * novo_numero_2)
    break

  while operador == '/':
    print(novo_numero_1 / novo_numero_2)
    break
  
  reutilizar = input('Deseja utilizar a caulculadora novamente s/n ?')
  
  
print('-------Acabou-------')