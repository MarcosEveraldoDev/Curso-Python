palavra_secreta = 'futebol'
letras_acertadas = ''
contador = 0
print('-------------Jogo Da Palavra Secreta-------------')
print('')
print('Tente adivinhar qual é a palavra secreta')
print('')

import os
 
while True:
  letra_digitada = input('Digite uma letra: ')
  if len(letra_digitada) > 1:
    print('Digite apenas uma letra')
    contador += 1
    continue
  if letra_digitada in palavra_secreta:
    letras_acertadas += letra_digitada
    contador += 1
            
  if letra_digitada not in palavra_secreta:
    contador += 1
    print(f'Tentativas: {contador}')

  palavra_formada = ''
  for letra_secreta in palavra_secreta:
    if letra_secreta in letras_acertadas:
      palavra_formada+= letra_secreta
    else:
      palavra_formada += '*'
  print(palavra_formada)
  
  if palavra_formada == palavra_secreta:
    os.system('cls')
    print('Parabens você ganhou o jogo')
    print(f'A palavra era : {palavra_formada}')
    print(f'Seu numero de tentativas total foi de : {contador}')
    break
  