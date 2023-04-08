def duplicar(*agrs):
  for numero in agrs:
    numero *= 2
  return numero

def triplicar(*agrs):
  for numero in agrs:
    numero *= 3
  return numero

def quadruplicar(*agrs):
  for numero in agrs:
    numero *= 4
  return numero

multiplicacao_1 = duplicar(5)
multiplicacao_2 = triplicar(5)
multiplicacao_3 = quadruplicar(5)

print(multiplicacao_1)
print(multiplicacao_2)
print(multiplicacao_3)

# outra forma de resolução

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
     return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(9))
print(triplicar(9))
print(quadruplicar(9))
