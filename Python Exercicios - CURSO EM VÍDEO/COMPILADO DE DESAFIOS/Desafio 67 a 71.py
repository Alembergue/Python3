# 66
print('{:=^40}'.format('LEITOR DE NUMEROS Vr 3'))
numero = soma = cont = 0
while True :
    numero = int(input('Digite um numero [999/Parar programa] :'))
    if numero == 999 :
        break
    cont = cont + 1
    soma = soma + numero
print(f'Foram digitados {cont} e a soma entres ele é {soma}')

#67 TABUADA VR 3

print('{:=^40}'.format('TABUADA Vr 3'))
numero = int(input('Digite uma numero para ver sua tabada:'))
while True:
    for tabuada in range (1,10) :
      print('{} X {:2} = {}'.format(numero,tabuada,numero*tabuada))

    numero = int(input('Digite uma numero para ver sua tabada:'))

    if numero <= 0 :
        break
print('Esse valor não é valido!Programa encerrado!')


#67 PAR OU IMPAR Vr 3

import random
import time
print('{:=^40}'.format('PAR OU IMPAR Vr 3'))

print('=-'*20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*20)

jogador  = int(input('Escola o seu numero :'))
jogador2 = str(input('Par ou impar?[P/I]')).upper().strip()[0]
print('UM! DOIS! TRÊS EEEEE')

maquina = random.randint(0,11)
soma = par = impar = cont = 0
time.sleep(2)
print('JÁ!!!!')

while True :

      if jogador2 == 'P' :
         soma = jogador + maquina
         par = soma % 2
         if par == 0 :
              cont = cont + 1
              print('Jogador jogou {} e a maquina jogou {}.Total de {} que é PAR'.format(jogador,maquina,soma))
              print('\033[1:32mO JOGADOR VENCEU!\033[m\nVAMOS JOGAR NOVAMENTE.....')
         else :
              print('Jogador jogou {} e a maquina jogou {}.Total de {} que é IMPAR'.format(jogador,maquina,soma))
              print('\033[1:31mA MAQUINA VENCEU!\033[m\nGAME OVER!Você venceu {} vezes'.format(cont))
              break

      if jogador2 == 'I' :
          soma = jogador + maquina
          par = soma % 2
          if par != 0 :
             cont = cont + 1
             print('Jogador jogou {} e a maquina jogou {}.Total de {} que é IMPAR'.format(jogador,maquina,soma))
             print('\033[1:32mO JOGADOR VENCEU!\033[m\nVAMOS JOGAR NOVAMENTE.....')
          else :
              print('Jogador jogou {} e a maquina jogou {}.Total de {} que é PAR'.format(jogador,maquina,soma))
              print('\033[1:31mA MAQUINA VENCEU!\033[m\nGAME OVER!Você venceu {} vezes'.format(cont))
              break

      jogador  = int(input('Escola o seu numero :'))
      jogador2 = str(input('Par ou impar?[P/I]')).upper().strip()[0]


#68 Registro de dados

import time
print('{:=^40}'.format('REGISTRO DE DADOS Vr 3'))
print('=-'*20)
print('REGISTRE SEUs DADOS')
print('=-'*20)

totalid = totalh = totalm = 0

while True :

     idade = int(input('idade :'))

     while  idade <= 0 or idade > 110:
       print('Opção Invalida!Tente novamente!')
       idade = int(input('idade :'))

     sexo  =  str(input('Sexo [M/F] :')).upper().strip()[0]

     while  sexo != 'M' and sexo != 'F' :
       print('Opção Invalida!Tente novamente!')
       sexo =  str(input('Sexo [M/F] :')).upper().strip()[0]

     print('=-'*20)
     time.sleep(2)
     print('Dados registados com sucesso')

     if  idade >= 18 :
         totalid = totalid + 1

     if  sexo == 'M' :
         totalh = totalh + 1

     if sexo == 'F' and idade < 20 :
         totalm = totalm + 1

     continuar = str(input('Deseja continuar ?[S/N] ')).upper().strip()[0]
     print('=-'*20)

     while continuar != 'S' and continuar != 'N' :
         print('Opção Invalida!Tente novamente!')
         continuar = str(input('Deseja continuar ?[S/N] ')).upper().strip()[0]
         print('=-'*20)

     if continuar == 'N':
        break

print('Finalizando sistema,aguarde....')
time.sleep(3)
print(f'{totalid} pessoas são maior de idade !(18 anos)')
print(f'Foi cadastrado {totalh} pessoas do sexo masculino!')
print(f'Foi cadastrado {totalm} mulheres com menos de 20 anos!')

#69 LOJA
import time
print('{:=^40}'.format('MERCADO VR1'))
print('=-'*20)
print('MERCADO AZUL')
print('=-'*20)
total = tot1000 = soma = 0
while True :
     produto = str(input('Nome do produto :')).upper().strip()
     valor = float(input('Valor do produto:R$'))
     total = total + 1
     soma = soma + valor

     if valor >= 1000 :
         tot1000 = tot1000 + 1

     if total == 1 :
         nomemaisbarato = produto
         valormaisbarato = valor
     else :
         if valormaisbarato > valor :
             valormaisbarato = valor
             nomemaisbarato = produto

     continuar = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]

     while continuar != 'S'and continuar != 'N':
         print('Opção Invalida,Tente novamente!')
         continuar = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]

     if continuar == 'N' :
         break
print('Finalizando suas compras....')
time.sleep(3)
print(f'O custo total de suas compras foi de R${soma}')
print(f'{tot1000} produtos custaram R$1000 ou mais!')
print(f'O produto com menor preço é {nomemaisbarato} que custa R$ {valormaisbarato}')

#69 BANCO
print('{:=^40}'.format('CAIXA ELETRÔNICO VR1'))
print('=-'*20)
print('             BANCO BUDEGA')
print('=-'*20)

num = int(input('Qual valor você deseja sacar?R$'))
total = num
ced =50
totalced = 0

while True :
    if total >= ced :
        total = total - ced
        totalced = totalced +1
    else :
        if totalced > 0 :
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 50 :
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10 :
            ced = 1
        totalced = 0
        if total == 0:
                break
print('Volte sempre ao BANCO BUDEGA!Tenha um bom dia!')
