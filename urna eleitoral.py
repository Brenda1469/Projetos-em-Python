i=8
Breno=0
Lula=0
Lucas=0

T1=0
T2=0
T3=0

print('Digete 0 para votar em outro candidato que nao seja ou seu ou para votar nulo:')

while i<=10:

 Breno=int(input('Digete 1 para votar no candidato Breno: '))
 Lucas=int(input('Digete 2 para votar no candidato Lucas: '))
 Lula=int(input('Digete 3 para votar no candidato Lula: '))

 if Breno==1:
  T1+=1
  print(f"O candidato Breno tem {T1} votos")

 elif Lucas==2:
   T2+=1
   print(f"O candidato Lucas o tem {T2} votos")

 elif Lula==3:
  T3+=1
  print(f"O candidato Breno tem {T3} votos")

 i+=1

print(f"Total de votos:")
print(f"Candidato Breno: {T1} votos.")
print(f"Candidato Lucas: {T2} votos.")
print(f"Candidato Lula: {T3} votos.") 