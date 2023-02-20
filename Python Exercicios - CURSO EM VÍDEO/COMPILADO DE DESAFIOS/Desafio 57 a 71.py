# 57 ESCOLHA O SEXO
sexo = str(input('Digite o seu sexo [M/F] ?')).upper().strip()[0]
while sexo != 'M' and sexo != 'F':
      sexo = str(input('\033[1;31mDados invalido!\033[m\nPor favor,informe o seu sexo [M/F] ?')).upper().strip()[0]
print('\033[1;32mA opção {} é valida,\nDados registrados com sucesso!'.format(sexo))

sexo = str(input('Digite o seu sexo [M/F] ?')).upper().strip()[0]
while sexo not in 'MmFf':
      sexo = str(input('\033[1;31mDados invalido!\033[m\nPor favor,informe o seu sexo [M/F] ?')).upper().strip()[0]
print('\033[1;32mA opção {} é valida,\nDados registrados com sucesso!'.format(sexo))


# 58 ADVINHAÇÃO MODO 1
import random
print('{:=^40}'.format('JOGO DA ADVINHAÇÃO'))
print('Vamos jogar um jogo?\nADVINHE O NUMERO EM QUE A MAQUINA ESTA PENSANDO')
jogador = int(input('Digite um numero [0/10]:'))
maquina = random.randint(0,5)
total = 0
while jogador != maquina :
      jogador = int(input('\033[1;31mVocê errou!\033[mEu pensei no {}\nDigite outro número [0/10]:'.format(maquina)))
      maquina = random.randint(0,5)
      total = total + 1
print('{:=^40}'.format('\033[1;32mPARABÉNS!VOCÊ VENCEU!\033[m'))
print(f'MAQUINA PENSO NO NUMERO {maquina} / JOGADOR PENSOU NO NUMERO {jogador}\nO TOTAL DE TENTATIVAS DO JOGADOR FOi {total}')
print('{:=^40}'.format('FIM'))

# 58 ADVINHAÇÃO MODO 2
import random
computador = random.randint(0,10)
print('Sou seu computador... Acabei de pensar em um npumero entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
acertou = False
palpites = 0
while not acertou :
      jogador = int(input('Qual é o seu palpite?'))
      palpites = palpites + 1
      if jogador == computador :
            acertou = True
      else:
            if jogador < computador :
                  print('Mais...Tente mais uma vez.')
            elif jogador > computador :
                  print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas.Parabéns!'.format(palpites))

# 59  MENUS

import time
print('{:=^40}'.format('MENUS'))
valor1 = float(input('Digite o primeiro valor:'))
valor2 = float(input('Digite o segundo valor:'))
print('Qual operação você deseja realizar?')
operacao = int(input('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NUMEROS\n[5]SAIR DO PROGRAMA\nDIGITE A OPÇÃO:'))

while operacao != 5 :
    if operacao == 1 :
        soma = valor1 + valor2
        print('A soma de {:.2f} com {:.2f} é {:.2f}'.format(valor1,valor2,soma))
        operacao = int(input('DESEJA FAZER OUTRA OPERAÇÃO?\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NUMEROS\n[5]SAIR DO PROGRAMA\nDIGITE A OPÇÃO:'))
        if operacao < 5:
         valor1 = float(input('Digite o primeiro valor:'))
         valor2 = float(input('Digite o segundo valor:'))

    if operacao == 2 :
     muilt = valor1 * valor2
     print('A Multiplicação entre {:.2f} e {:.2f} é {:.2f}'.format(valor1,valor2,muilt))
     operacao = int(input('DESEJA FAZER OUTRA OPERAÇÃO?\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NUMEROS\n[5]SAIR DO PROGRAMA\nDIGITE A OPÇÃO:'))

     if operacao < 5 :
        valor1 = float(input('Digite o primeiro valor:'))
        valor2 = float(input('Digite o segundo valor:'))

    if operacao == 3 :
        if valor1 > valor2 :
            print('O numero {:.2f} é maior que o numero {:.2f}'.format(valor1,valor2))
            operacao = int(input('DESEJA FAZER OUTRA OPERAÇÃO?\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NUMEROS\n[5]SAIR DO PROGRAMA\nDIGITE A OPÇÃO:'))

            if operacao < 5 :
             valor1 = float(input('Digite o primeiro valor:'))
             valor2 = float(input('Digite o segundo valor:'))

        if valor1 == valor2 :
               print('O numero {:.2f} é igual ao numero {:.2f}'.format(valor1,valor2))
               operacao = int(input('DESEJA FAZER OUTRA OPERAÇÃO?\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NUMEROS\n[5]SAIR DO PROGRAMA\nDIGITE A OPÇÃO:'))
               if operacao < 5 :
                       valor1 = float(input('Digite o primeiro valor:'))
                       valor2 = float(input('Digite o segundo valor:'))

        else :
            print('O numero {:.2f} é menor que o numero {:.2f}'.format(valor1,valor2))
            operacao = int(input('DESEJA FAZER OUTRA OPERAÇÃO?\n[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NUMEROS\n[5]SAIR DO PROGRAMA\nDIGITE A OPÇÃO:'))
            if operacao < 5 :
                  valor1 = float(input('Digite o primeiro valor:'))
                  valor2 = float(input('Digite o segundo valor:'))

    elif operacao == 4 :
        operacao = int(input('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NUMEROS\n[5]SAIR DO PROGRAMA\nDIGITE A OPÇÃO:'))

    elif operacao > 5 :
        print("Opção invalida, tente novamente")
        operacao = int(input('[1]SOMAR\n[2]MULTIPLICAR\n[3]MAIOR\n[4]NOVOS NUMEROS\n[5]SAIR DO PROGRAMA\nDIGITE A OPÇÃO:'))
print('Finalizando....')
time.sleep(2)
print('OBRIGADO POR USAR NOSSO SISTEMA,TENHA UM BOM DIA!')

# 60 FATORIAL
numero = int(input('Digite uma número para calcular seu Fatorial:'))
contagem = numero
fatorial = 1
print('Calculando {}!.'.format(numero),end='')
while contagem > 0:
    print('{}'.format(contagem),end='')
    print(' X ' if contagem > 1 else ' = ',end='')
    fatorial = fatorial * contagem
    contagem = contagem - 1
print('{}'.format(fatorial))

# COM FOR
n = int(input('Digite um numero para calcular seu fatorial: '))
c = 0
f = 1
for c in range (1, n):
    f *= n
    n -= 1
print('Seu fatorial é {}.'.format(f))


#61 GERADOR DE pa 2.0
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão da PA:'))
termo = primeiro
cont = 1
while cont <= 10 :
    print(' {} >'.format(termo), end ='')
    termo = termo + razao
    cont = cont + 1
print(' Fim')

#62 Progressão 2.0
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão da PA:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0 :
   total = total + mais
   while cont <= total :
      print(' {} >'.format(termo), end ='')
      termo = termo + razao
      cont = cont + 1
   print('PAUSA')
   mais=int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} termos mostrados'.format(total))

# 63 FIBONACCI
n = int(input('Digite um numero:'))
t1 = 0
t2 = 1
print('{} > {}'.format(t1,t2),end='')
cont = 3
while cont <= n :
    t3 = t1 + t2
    print(' > {}'.format(t3),end='')
    t1=t2
    t2=t3
    cont = cont + 1
print(' > FIM')

#64 LEITOR DE NUMEROS
print('{:=^40}'.format('LEITOR DE NUMEROS'))
numero = int(input('Digite um número [999 para para a operação]:'))
soma = numero
cont = 0
while numero != 999 :
      numero = int(input('Digite outro número [999 para para a operação]:'))
      soma = soma + numero
      cont = cont + 1
      if numero == 999 :
            soma = soma - 999
print('Foram digitados {} números e o total da soma entre eles é {}'.format(cont,soma))

#64 LEITOR DE NUMEROS
print('{:=^40}'.format('LEITOR DE NUMEROS'))
numero = cont = soma = 0
numero = int(input('Digite um número [999 para para a operação]:'))
while numero != 999 :
      soma = soma + numero
      cont = cont + 1
      numero = int(input('Digite outro número [999 para para a operação]:'))
print('Foram digitados {} números e o total da soma entre eles é {}'.format(cont,soma))

#65 LEITOR DE NUMEROS VR2

print('{:=^40}'.format('LEITOR DE NUMEROS Vr 2'))
numero = int(input('Digite um número :'))
sair = str(input('Deseja continuar? [S/N]')).upper().strip()[0]

soma  = numero
cont  = 0
media = 0
maior = menor = numero

if numero != 0 :
      cont = 1

while not sair == 'N':

    while sair != 'N' and sair != 'S':
        print('Opção Invalida!,Tente Novamente!')
        sair = str(input('Deseja continuar? [S/N]')).upper().strip()[0]

    numero = int(input('Digite outro número :'))
    cont = cont + 1
    soma = soma + numero
    media = soma/cont
    sair = str(input('Deseja continuar? [S/N]')).upper().strip()[0]

    if numero > maior :
             maior = numero

    elif numero < menor:
            menor = numero

print('Foram digitados {} números e o total da média entre eles é {} '.format(cont,media))
print('O maior valor digitado foi {} e o menor foi {}'.format(maior,menor))



