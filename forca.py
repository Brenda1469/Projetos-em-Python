import random

def escolher_palavra():
    palavras = ['python', 'javascript', 'html', 'ruby', 'css', 'programação']
    return random.choice(palavras)

palavra = escolher_palavra()
letras_usuario = []
chances = 7
ganhou = False

 #criar logica
while True:
    for letra in palavra:
     if letra.lower() in letras_usuario:
        print(letra,end=" ")
    else:
     print('_',end=" ")

     print(f'\nVoce tem {chances} chances')

     tentativa=input('Escolha uma letra para adivinhar: ')
     letras_usuario.append(tentativa.lower())

     if tentativa.lower() not in palavra.lower():
        chances-=1

     ganhou=True
     for letra in palavra:
       if letra.lower()not in letras_usuario:
         ganhou=False

    if chances==0 or ganhou: 
     break
    

if ganhou:
    print(f"Parabens, voce ganhou. A palavra era: {palavra}")
else:
    (f"Voce perdeu! A palavra era:{palavra}")

