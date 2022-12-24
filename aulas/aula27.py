numero_str = input('Vou dobrar o numero que voce digitar :')

try:
 print('Str :' , numero_str)
 numero_int = int(numero_str)
 print('Int :' , numero_int)
 print(f' o dobro do {numero_str} é : {numero_int * 2}')
except:
  print('isso nao é um numero')