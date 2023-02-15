print('----------Loja----------')
print('1- Ver o catalogo da loja.')
print('2- Pesquisar o produto.')
print('3- Telefone para contato.')
print('4- Sair.')

lista_produtos_esportivos = ['Luva de goleiro' , 'Chuteira' , 'Bola de Futebol']
lista_roupas = ['Vestido','Calça'] 
lista_acessorios = ['Brincos', 'Colar']                                                      
sapatos = ['Nike','Adidas','Puma'] 
                                   
opcao =  input('Digite a opção que irá acessar : ')

if opcao == '1':
  print('--------------------------------------')
  print('1- Produtos esportivos')
  print('2- Roupas ')
  print('3- Acessorios')
  print('4- Sapatos')
  opcao_catalogo = input('Digite a opçao que deseja ver: ')
  
  if opcao_catalogo == '1':
    for i,produto in enumerate(lista_produtos_esportivos):
     print('------------------------------')
     print(i,produto)  
     
    produto_selecionado = input('Digite a opçao que voce ira comprar: ')
    if produto_selecionado == '0':
      print('----------------------------')
      print(lista_produtos_esportivos[0])      
      
    elif produto_selecionado == '1':
      print('----------------------------')
      print(lista_produtos_esportivos[1])
      
    elif produto_selecionado == '2':
      print('----------------------------')
      print(lista_produtos_esportivos[2])
  
  
  
  if opcao_catalogo =='2':
    for produto in lista_roupas:
      if produto_selecionado == '1':        
        print('-------------------------')
        print(lista_roupas[0])
        break
      elif produto_selecionado == '2':
        print('-------------------------')
        print(lista_roupas[1])
        break 
  
  if opcao_catalogo == '3':
    for produto in lista_acessorios:
      if produto_selecionado == '1':
        print('-------------------------')
        print(lista_acessorios[0])
        break
      elif produto_selecionado ==  '2':
        print('--------------------------')
        print(lista_acessorios[1])
        break
  
  if opcao_catalogo == '4':
    for produto in sapatos:
      if produto_selecionado == '1':
        print('--------------------------')
        print(sapatos[0])
        break
      elif produto_selecionado == '2':
        print('---------------------------')
        print(sapatos[1])
        break
      elif produto_selecionado == '3':
        print('----------------------------')
        print(sapatos[2])
        break
  
while opcao == '2':
  pesquisa = input('Digite o produto que irá pesquisar: ')  
  if pesquisa in lista_produtos_esportivos or  lista_roupas or lista_acessorios or sapatos:
    print(f'Seu produto é {pesquisa}, ele tem no nosso estoque ')

  else:
    print('Seu produto nao tem no nosso estoque. ')
    

if opcao == '3':
  print('------------------------')
  print('3628-4725')
  print('------------------------')

if opcao == '4':
  print('------------------------')
  print('Volte Sempre')
  print('------------------------')

