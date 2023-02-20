# 72 Pegando numeros
sequencia = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez')
while True :
     numero = int(input('Digite um numero entre 0 e 10 :'))
     if numero < 0 or numero > 10 :
        print('\033[1;31mOpção invalida!\033[mTente novamente')
     elif numero >= 0 or numero <= 10 :
        print(f'Você digitou o número {sequencia[numero]}!')
        continuar = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
        if continuar == 'N' :
             break
print('Programa Encerrado')

# 73 TIMES
print('{:=^40}'.format('BRASILEIRÃO'))
times = ('Grêmio','Flamengo','Fluminense','Chapecoense','Inter','Vasco','Botafogo','Corinthians','Palmeiras','Portuguesa')
print(f'Os 5 primeiros colocados são {times[0:5]}')
print('-='*20)
print(f'Os 4 ultimos colocados são {times[-4:]}')
print('-='*20)
print(f'Times por ordem alfabetica {sorted(times)}')
print('-='*20)
print('A chapecoense esta na {}ª posição'.format(times.index('Chapecoense')+1))
print('-='*20)

# 74 SORTEIO E MAIO/MENOR COM FOR
import random
print('{:=^40}'.format('SORTEIO'))
primeiro = random.randint(0,5)
segundo = random.randint(0,5)
terceiro = random.randint(0,5)
quarto = random.randint(0,5)
quinto = random.randint(0,5)
total = primeiro,segundo, terceiro ,quarto ,quinto
print('Os maiores valores sorteados foram :', end=' ')
for n in total :
    print(f'{n}',end=' ')
print(f'\nO maior valor sorteado foi {max(total)}')
print(f'O menor valor sorteado foi {min(total)}')

# 75 Números
print('{:=^40}'.format('NÚMEROS'))
num1 = int(input('Digite um numero :'))
num2 = int(input('Digite outro numero :'))
num3 = int(input('Digite mais um numero :'))
num4 = int(input('Digite o ultimo numero :'))
total = num1,num2,num3,num4
print(f'Você digito os valores {total}')
print(f'O valor 9 apareceu {total.count(9)} vezes')
if total.count(3) == 0 :
    print('O valor 3 não foi digitado nenhuma vez!')
else :
    print(f'O valor 3 foi apareceu a primeira vez na posiçao {total.index(3)+1}ª')
print(f'Os números pares digitados foram ', end='')
for c in total :
    if c %2 == 0 :
     print( c,end=' ')

# 76 Listagem de Preços
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
listagem =  ('Lápis', 0.50, 'Caneta', 1.50, 'Estojo', 15.99, 'Mochila', 120.90, 'Folha de Ofício', 13.50, 'Caneca',
            19.90, 'Lapiseira', 5.90, 'Gift Card $30', 30, 'Shampoo', 17.80)
for pos in range (0,len(listagem)) :
    if pos % 2 == 0 :
        print(f'{listagem[pos]:.<30}',end='') # regula os pontos em parelho :<30
    else :
        print(f'R${listagem[pos]:>7.2f}')  # regula os espaços em parelho :>7
print('-'*40)

# 77 Listagem de Preços
print('{:=^40}'.format('VOGAIS'))
print('-'*40)
print(f'{"LISTAGEM DE VOGAIS":^40}')
print('-'*40)
listagem =  ('Lapis', 'Caneta', 'Estojo', 'Mochila','Folha', 'Caneca','Lapiseira','Gift','Shampoo')
vogal = ('a','e','i','o','u')
for palavra in listagem :
    print(f'\n Na palavra {palavra.upper()} temos ', end='')
    for letra in palavra :
        if letra.lower() in 'aeiou' :
            print(letra,end=' ')
