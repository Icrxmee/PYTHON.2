from time import sleep

print ("=" * 10, "LOJAS JUSE DANTE", "=" * 10)

valor = float ( input ("Digite o valor a ser pago: R$"))
sleep(1)


print("[ 1 ] Â vista dinheiro/pix")
print("[ 2 ] Â vista cartão")
print("[ 3 ] 2x no cartão ")
print("[ 4 ] 3x ou mais no cartão")
pagamento = int( input("Selecione a fomra de pagamento:"))
sleep(1)


if pagamento == 1:
    print (f"O valor a ser pago, será de R${ valor - (valor * 0.10)} com desconto")

elif pagamento == 2:
    print (f"O valor a ser pago, será de R${valor - (valor * 0.05)} com desconto")

elif pagamento == 3:
    print (f"O valor a ser pago, será de R${valor / 2} mensal")

elif pagamento == 4:
    meses = int ( input("Digite em qwuantos meses você deseja parcelar:"))
    juros = valor * 1.20
    parcela = juros / meses

    print (f"o seu valor parcelado em {meses} meses será de: {parcela} ao mês")