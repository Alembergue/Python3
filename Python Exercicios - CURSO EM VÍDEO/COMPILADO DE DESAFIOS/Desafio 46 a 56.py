#46 CONTAGEM REGRESSIVA
import time
print('{:=^40}'.format('FOGOS DE ARTIFÍCIO'))
for c in range (10,-1,-1) :
    time.sleep(1)
    print(c)
time.sleep(1)
print('{:=^40}'.format('FELIZ ANO NOVO'))

#47 CONTAGEM DE PARES
print('{:=^40}'.format('NUMEROS PARES'))
for c in range (0,52,2) :
    print(c,end=' ')
print('FIM!')

#48 SOMA IMPARES
print('{:=^40}'.format('SOMA NUMEROS IMPARES'))
soma = 0
cont = 0
for c in range (1,501,2):
    if c % 3 == 0 :
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores solicitados é {}'.format(cont,soma))

#49 TABUADA REDUZIDA

print('{:=^40}'.format('TABUADA'))
num = int(input('Digite um numero:'))
for c in range (1,11) :
    print('{} X {:2} = {} '.format(num,c,num*c))

#50 SOMA NUMEROS PARES
print('{:=^40}'.format('NUMEROS PARES'))
soma = 0
cont = 0
for c in range (1,7) :
    num = int(input('Digite um valor :'))
    if num % 2 == 0 :
        soma = soma + num
        cont = cont + 1
print('Foi informado {} PARES e a soma deles é {}'.format(cont,soma))


#51
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão:'))
decimo = primeiro + (10-1) * razao
for c in range (primeiro,decimo + razao,razao):
    print(' {} '.format(c),end='>')
print(' Acabou')


#52 NUMEOR PRIMO
num = int(input('Digite um numero: '))
total = 0
for c in range (1, num + 1):
    if num % c == 0:
      print('\033[33m', end='')
      total = total + 1

    else:
      print('\033[31m', end='')

    print('{} '.format(c), end ='')
print('\033[m\nO numero {} foi divisivel {} vezes'.format(num,total))
if total == 2 :
    print('Por isso ele É PRIMO!')
else:
    print('Por isso ele NÃO É PRIMO!')


#53 FRASE INVERTIDA

frase = str(input('Digite uma frase : ')).upper().lower().strip()
#invertida = junto[::-1]
inverso =''
palavras = frase.split()
junto =''.join(palavras)
for letra in range (len(junto)-1,-1,-1) : #
    inverso= inverso +junto[letra]
print('O inverso de  {} é {}'.format(junto,inverso))
if inverso== junto:
    print('Temos um palíndromo!')
else :
    print('A frase digitada não é um palíndromo')


#54 MAIOR DE IDADE
from datetime import date
anoatual = date.today().year
cont = 0
cont1 = 0
for pessoa in range (1,8) :
    data = int(input('Ano de nascimento da {}° pessoa:'.format(pessoa)))
    maioridade = anoatual - data
    if maioridade < 18 :
     cont = cont + 1
    else :
     cont1 = cont1 + 1

print('{} pessoas ainda não são maior de idade!\n{} pessoas são maior de idade'.format(cont,cont1))

#56 PESO MAIOR MENOR
maior  = 0
menor = 0

for p in range(1,6) :
    peso = float(input('Peso da pessoa {}°:Kg'.format(p)))
    if p == 1 :
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso lido foi de {}Kg".format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))



#56 GRUPO
som = 0
vel = 0
m20 = 0
for c in range(1, 5):
    print(f'------- {c}ª PESSOA -------')
    nome = str(input('Nome: ')).strip()
    idd = int(input('Idade: '))
    sex = str(input('Sexo [M/F]: ')).strip().upper()
    som += idd
    med = som/4
    if sex == 'M':
        if idd > vel:
            vel = idd
            hnome = nome
    if sex == 'F':
        if idd < 20:
            m20 += 1
print(f'A média de idade do grupo é {med} anos')
print(f'O homem mais velho tem {vel} anos e se chama {hnome}')
print(f'Existem {m20} mulheres com menos de 20 anos.')
