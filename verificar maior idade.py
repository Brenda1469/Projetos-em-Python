nome=input('Digete seu nome:')
ano=int(input('Digete seu ano de nascimento:'))
mes=int(input('Digete seu mes de nascimento:'))
dia=int(input('Digete seu dia de nascimento:'))


print(nome)
print(f'{dia}/{mes}/{ano}') 

mes=mes*30
idade=2024-ano
idadem=365-mes
#idaded=30-dia

if idade>=18 and idadem>180: #and idaded<=18): #oq ta errado
     print('Voce e maior de idade')


else:
   print('Voce e menor de idade')