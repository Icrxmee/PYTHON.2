valor = float ( input('Qual o valor da casa: R$'))

salario = float ( input('Qual o salario do comprador: R$'))

financiamento = int ( input('Quantos anos de financiamento: '))

percentual = 0.30
percentual_ = 0.30 * salario

mensalidade = financiamento * 12
mensalidade_ = valor / mensalidade



print ('Para pagar {} de investimento, sua mensalidade vai ficar {:.0f}.' .format(valor,mensalidade_))

if mensalidade_ >= percentual_ :
   
    print('Seu investimento é NÃO é VÁLIDO')

else:
    print('Seu investimento VÁLIDO')


