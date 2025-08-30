from datetime import date
from time import sleep


nascimentno = int ( input( "Informe o ano em que você nasceu:"))
sleep(1)

ano_atual = date.today().year
idade = ano_atual - nascimentno

print (f"Se você nasceu em {nascimentno}, então você possui {idade} anos")

if idade <= 9:
    print("Sua categoria será: MIrim. ")

elif idade > 9 and idade <= 11:
    print ("Sua categoria será: Infantil.")

elif idade > 11 and idade <= 19:
    print ("Sua categoria será: Junior")

elif idade > 19 and idade <= 25:
    print ("Sua categoria será: Senior.")

elif idade > 25:
    print ("Sua categoria será: Master")