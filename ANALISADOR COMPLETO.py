somaidade = 0
mediaidade = 0
maioridadehome = 0
nomevelho = ""
mulher20 = 0

for c in range (1, 5):
    
    print (f'---------- {c}° PESSOA ----------')
    
    nome = str ( input ("Digite o nome: ")).strip()
    idade = int ( input("Digite a idade:"))
    sexo = str ( input("Sexo [F/M]: ")).strip()

    somaidade += idade

    if c == 1 and sexo in 'Mm':
        maioridadehome = idade
        nomevelho = nome

    if sexo in 'Mm' and idade > maioridadehome:
        maioridadehome = idade
        nomevelho = nome 

    if sexo in 'Ff' and idade < 20:
        mulher20 += 1

mediaidade = somaidade / 4
print (f"A media de idade do grupo é de: {mediaidade}")
print (f'O homem mais velho tem {maioridadehome} anos e se chama {nomevelho}')
print (f'Temos {mulher20} mulheres menores que 20 anos.')