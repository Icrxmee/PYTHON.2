from time import sleep

valor1 = float ( input ("Digite um valor:"))
sleep(1)

valor2 = float ( input ("Dgite um valor:"))
sleep(1)

valor3 = float ( input ("Digite um valor:"))
sleep(1)

if valor1 + valor2 > valor3 and valor1 + valor3 > valor2 and valor2 + valor3 > valor1:
    print ("Os valores podem gerar uma triângulo.")

    if valor1 == valor2 == valor3:
        print ("O triangulo formado é um: EQUILÁTERO")

    elif valor1 == valor2 or valor1 == valor3 or valor2 == valor3:
        print ("O triángulo formado será um: Isósceles")

    else:
        print ("O triângulo formado será um: Escaleno")

else:
    print ("Os valores NÃO podem gerar um triângulo")




