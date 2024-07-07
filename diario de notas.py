nota1=int(input('Digete a primeira nota:'))
nota2=float(input('Digete a segunda nota:'))
nota3=float(input('Digete a terceira nota:'))
nota4=float(input('Digete o valor da quarta nota:'))

soma=nota1+nota2+nota3+nota4
media=soma/4
midiafinal=media*4

if midiafinal>=60:
  print(f'O aluno foi aprovado com a media final de {midiafinal}')
  
if midiafinal>=40 and midiafinal<60:
 print(f'O aluno foi para recuperaçao com a media final de {midiafinal}')

else:
  print(f'O aluno foi reprovado com a media final de {midiafinal}')

  