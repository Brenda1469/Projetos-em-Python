i=0
cont=1
total=0
produtos=0

while (i<10 and produtos!='p'):
 produtos=float(input(f'Digete o valor do produto {cont} ou digete P para parar o programa:'))
 cont+=1
 total+=produtos
 
 print(f'A soma dos produtos e {total}') 
 i+=1