perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
quantidade_de_acertos = 0
for pergunta in perguntas:
    print(pergunta['Pergunta'])
    print()
    
    opcoes = pergunta['Opções']
    
    for i,opcao in enumerate(opcoes):
       print(f'{i})', opcao)
    
    print()
    
    resposta = input('A resposta é : ')
    
    resposta_int = None
    acertou = False
    quantidade_de_opcoes = len(opcoes)
    
    if resposta.isdigit():
        resposta_int = int(resposta)  
          
    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < quantidade_de_opcoes:
            if opcoes[resposta_int] == pergunta['Resposta']:
                acertou = True
    if acertou :
        quantidade_de_acertos += 1
        print()
        print('Acertou')
        print()
    else:
        print('Errou')

print('Você acertou ', quantidade_de_acertos , 'de ' , len(pergunta))