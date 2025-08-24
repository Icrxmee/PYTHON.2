from time import sleep

valor = int ( input('Escreva um valor inteiro:')) 

sleep(1)

print ('Escolha um conversão')
print ('[ 1 ]  Binário')
print ('[ 2 ]  Octal' )
print ('[ 3 ]  Exadecimal')

escolha = int ( input('opção:'))

binario = bin(valor)[2:]
octal = oct(valor)[2:]
hexadecimal = hex(valor)[2:]

if escolha == 1:
    print ("A forma de conversão escolhida foi Binário.", end='')
    print ( "A conversão do valor {} será: {}" .format(valor, binario))

elif escolha == 2:
    print("A forma de conversão escolhida foi Octal.", end='')
    print (" A conversão do valor {} será: {}" .format(valor, octal))

elif escolha == 3:
    print ("A forma de conversão escolhida foi Hexadecimal.", end='')
    print ("A conversão do valor {} será: {}" .format(valor, hexadecimal))
    
