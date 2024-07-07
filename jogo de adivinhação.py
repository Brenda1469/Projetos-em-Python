import random as rnd

palpite=999

sorteio=rnd.randint(0,50)
cont=1

palpite=int(input('Digete seu palpite: (um valor de 0 a 50)'))


#pq ta dando erro
while  palpite!=sorteio: 
 palpite=int(input('Digete seu palpite: (um valor de 0 a 50)'))
 if palpite==sorteio:
  (print(f'Voce arcertou, o numero era {palpite}'))
 else:
  print(f'Voce errou, tenete mais uma vez (tentativa {cont})')
  cont+=1