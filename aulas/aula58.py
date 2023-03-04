def soma(*args):
  total = 0
  for numero in args:
    print('total', total ,'+', numero)
    total += numero
    print(total)
    
    
soma(1,2,3,4,5)
