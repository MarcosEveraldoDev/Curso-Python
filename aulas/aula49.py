import os

lista = []

while True:
  print('Selecione uma opção:')
  opcao = input('[i]nserir, [a]pagar, [l]istar: ')
  
  if opcao == 'i':
   os.system('cls')
   valor = input('Valor: ')
   lista.append(valor)
   
  elif opcao == 'a':
   os.system('cls')
   for i,valor in enumerate(lista):
     print(i,valor)
   indice_str =input('Digite o indice que voce deseja apagar: ')
   
   try:
     indice = int(indice_str)
     del lista[indice]
   
   except ValueError:
     print('Por favor digite um numero inteiro !')
   except TypeError:
     print('Indice nao existente na lista !')
   
  elif opcao == 'l':
   os.system('cls')
   if len(lista) == 0:
     print('Nao ha nada para listar')
     
   for i,valor in enumerate(lista):
     print(i,valor) 
        
  else:
    print('Por favor digite i,a ou l')



  
