from time import sleep

peso = float ( input("Digite seu peso:"))
sleep(1)

altura = float ( input("Digite sua altura:"))
sleep(1)

imc =   peso  / (altura ** 2)
print (f"Seu valor de IMC é: {imc:.1f}")

if imc < 18.5:
    print ("Você está ABAIXO do peso.")

elif imc > 18.5 and imc <= 25:
    print ("Você está no peso IDEAL.")

elif imc > 25 and imc < 30:
    print("Você está com SOBREPESO.")

elif imc > 30 and imc < 40:
    print ("Você está com OBESIDADE.")

elif imc > 40:
    print ("Você está com OBESIDADE MORBIDA.")

