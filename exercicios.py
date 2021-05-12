#1
def soma(a,b,c):
    print('A soma é:', a+b+c)

soma(10,12,14)

print()
#2

def fun(a):
    if a > 0:
        print('P')
    elif a < 0:
        print('N')
    else:
        print('0')

n1 = int(input('Digite um número:'))

fun(n1)

print ()
#3

def somaImposto(t,c):
    print('T corresponde a quantia de imposto sobre vendas: valor ={0}'.format(t))
    
    print('C corresponde ao custo: valor ={0}'.format(c))
    


taxa = int(input('Digite um número:'))
custo = int(input('Digite um número: '))

somaImposto(taxa,custo)
print('O valor de custo com imposto incluso é de: ', (taxa * custo / 100)+custo)

#4
print()

def salario(h):
    if (h > 40):
        print('Adicional de', (horas-40)*1.5, ',de acordo com as horas extras trabalhadas.')
    else:
        print('Salário de acordo com as horas trabalhadas')

print()

horas = int(input('Digite a quantidade de horas trabalhadas: '))

salario(horas)

#5
print()

def IMCcalculo(p,a):
    print(f'O IMC de uma pessoa é: {p/a:.2f}')

IMCcalculo(75,1.68**2)

#6
print()

def conc(n):
    if (n >= 9.0) and (n < 10.0):
        print('A')
    elif (n >= 8.0) and (n < 8.9):
        print('B')
    elif (n >= 7.0) and (n < 7.9):
        print('C')
    elif (n >= 4.1) and (n < 6.9):
        print('D')
    else:
        print('F')

num = float(input('Qual nota você tirou?'))

conc(num)

#7
print()

def menor(z,t):
    if z>t:
        return t
    elif z<t:
        return z
    else:
        print('Números iguais')

n3 = int(input('digite um número:'))
n4 = int(input('digite um outro número:'))
menor(n3,n4)

#DESAFIO
def mes(m):
    if (m==(1)): 
        print('Janeiro')
    elif (m==(2)):
        print('Fevereiro')
    elif (m==(3)):
        print('Março')
    elif (m==(4)):
         print('Abril')
    elif (m==(5)):
        print('Maio')
    elif (m==(6)):
        print('Junho')
    elif (m==(7)):
        print('Julho')
    elif (m==(8)):
        print('Agosto')
    elif (m==(9)):
        print('Setembro')
    elif (m==(10)):
        print('Outubro')
    elif (m==(11)):
        print('Novembro')
    elif (m==(12)):
        print('Dezembro')
    else:
        print('NULL')
    

print('Digite sua data de nascimento:')
dia = int(input('Dia '))
meses = int(input('do mês '))
ano = int(input('do ano de '))

mes(meses)

print( dia,'de', mes , 'de', ano)
#desafio continua.. 
