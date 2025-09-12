frase = str( input("Digite uma frase: ")).strip().upper() #strip tira os espaços e upper joga tudo para maiúsculo.

palavra = frase.split() #vai separar cada palavra escrita.
juntar = ''.join(palavra) #vai juntar todas a palavras com o que estiver dentro das aspas, nesse caso, como não tem nada, vai juntar os espaços.

inverso = ''

for letra in range (len(juntar) -1, -1, -1): 
   inverso += juntar[letra] #puxando o "juntar" modificado pelo FOR, inveés de ser o lá de cima.

print(inverso)

if inverso == juntar: 
   print("Você tem um PALINDROMO")
else:
   print("Você não tem um PALINDROMO")