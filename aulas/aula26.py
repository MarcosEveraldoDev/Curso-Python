nome = input('Digite seu nome : ')

idade = input('Digite sua idade : ')

if nome == '' or idade == ''  :
  print('voce deixou campos em brancos')
else:
  print('Seu nome é : ' , nome)
  print('Seu nome invertido é ', nome [::-1] )
  print('Sua idade é de : ' , idade)
  if ' ' in nome:
   print('Seu nome contem espacos')
  else:
    print('Seu nome nao contem espaços') 
  print(f'Seu nome tem {len(nome)} letras')
  print('A primeira letra do seu nome é :', nome[0])
  print('A ultima letra do seu nome é :', nome[-1])

  
 


