#EX 96
print('{:=^40}'.format('Mundo 3 - FUNÇÕES  '))
def area(valor1,valor2) :
    dimensao = valor1 * valor2
    print(f'A área de um terreno {valor1}X{valor2} é de {dimensao}m quadrados.')
def titulo() :
    print('-='*15)
    print(f'    CONTROLE DE TERRENOS')
    print('-='*15)
titulo()
valor1 = float(input('LARGURA :'))
valor2 = float(input('COMPRIMENTO :'))
area(valor1,valor2)

#EX 96
def escreva(txt):
    print('~' * len(txt)) #PARA ACOMPAANHAR O TAMANDO DO TEXTO
    print(txt)
    print('~' * len(txt))
escreva('Alembergue')
escreva('Curso')
escreva('Cev')

#EX 97
def escreva(msg):
    tam=len(msg)+4
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
#PROGRAMA PRINCIPAL
escreva('Alembergue')
escreva('Curso')
escreva('Cev')

#EX 98
print('{:=^40}'.format('Mundo 3 - FUNÇÃO CONTAGEM  '))
import time
def crescente():
    print('-='*20)
    print('Contagem de 1 até 10 de 1 em 1.')
    for c in range (0,10):
        time.sleep(1)
        print(f'{c}',end=' ')
    print('FIM!')
time.sleep(2)
def descrescente():
    print('-='*20)
    print('Contagem de 10 até 0 de 2 em 2.')
    for d in range (10,0,-2):
        time.sleep(1)
        print(f'{d}',end=' ')
    print('FIM!')
time.sleep(2)
def personalizar():
    print('-='*20)
    print('Agora é sua vez de personalizar a contagem!')
    inicio = int(input('Inicio:'))
    fim = int(input('Fim:'))
    passo = int(input('Passo:'))
    if passo < 0 :
        passo *= -1
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    print('-='*20)
    for p in range(inicio,fim,passo):
        time.sleep(1)
        print(f'{p}',end=' ')
    print('FIM!')
#Programa Principal
crescente()
descrescente()
time.sleep(2)
personalizar()


#EX 99
import  time
def maior(*num):
    print("-="*30)
    print('Analisando valores passados...')
    for n in num:
         time.sleep(0.5)
         print(f'{n}',end=' ')
    if len(num) == 0 :
        print(f'Foram informados {0} valores ao todo.')
        print(f'O maior valor informado foi {0}.')
    else:
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}.')
maior(1,2,6,8,3,2,)
maior(4,2,9)
maior(5,2)
maior(6)
maior()

#EX 100
print('{:=^40}'.format('Mundo 3 - FUNÇÃO SORTEIO + SOMA  '))
import time
import random
lista = []
def sorteio() :
        for c in range(0,5) :
            lista.append(random.randint(1,10))
        print(f'Sorteando {len(lista)} valores da lista :', end=' ')
        for n,v in enumerate(lista):
            time.sleep(0.5)
            print(v,end=' ')
        print('PRONTO!')
def somapar(lista):
        soma = 0
        for valor in lista:
           if valor % 2 == 0 :
               soma = soma + valor
        print(f'Somando os valores pares de {lista}, temos {soma} .')
#PP
sorteio()
somapar(lista)

#EX 101
print('{:=^40}'.format('Mundo 3 - FUNÇÃO - VOTO  '))
def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade == 0:
        resp = ('Idade invalida!')
    elif idade < 16:
        resp =(f'Voce tem {idade} anos : VOCÊ NÃO PODE A VOTAR!')
    elif idade <=16 and idade < 18 :
        resp =(f'Voce tem {idade} anos : O VOTO É OPCIONAL!')
    elif idade > 18 and idade <= 65:
        resp =(f'Voce tem {idade} anos : O VOTO É OBRIGATORIO!')
    else:
        resp =(f'Voce tem {idade} anos : O VOTO É OPCIONAL!')
    return resp
print('-'*40)
ano = int(input('Em que ano você nasceu?'))
print(voto(ano))

#EX 102
print('{:=^40}'.format('Mundo 3 - FUNÇÃO - Fatorial + docstring  '))
def fatorial(num=1,show=False) :
    """
    fatorial(num,show=False)
    :param num: O número a ser calculado.
    :param show:(opicinal) mostrar ou não a conta.
    :return:O valor de Fatorial de uma numero num.
    """
    print('-'*40)
    if show == False:
      f = 1
      for c in range(num,0,-1) :
          f = f * c
      return f
    elif show == True :
      f = 1
      for c in range(num,0,-1) :
          f = f * c
          print(f'{c} ',end=' ')
          if c > 1:
              print('x',end=' ')
          else:
              print('=',end=' ')
      return f
print(fatorial(5,show=True))

#EX 103
def ficha(nome, gols):
    if nome == '':
        nome = f'\033[33m {"<Desconhecido>"} \033[m'
    if gols == '':
        gols = f'\033[33m {"0"} \033[m'
    return f'O Jogador: {nome}, fez {gols} gol(s) no campeonato.'
nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
print(ficha(nome, gols))

#EX 104
def leiaint() :
    print('-'*40)
    n = str(input('Digite um valor:'))
    while True :
        if n.isnumeric() :
           print(f'Você digitou o valor {n}.')
           break
        else :
            print('Valor invalido!Tente novamente ')
            n = str(input('Digite um valor:'))
leiaint()


#EX 104 By Guanabra
print('{:=^40}'.format('Mundo 3 - FUNÇÃO  '))
def leiaint(msg):
    ok = False
    valor = 0
    while True :
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else :
            print('\033[0;31mErro!Digite um número inteiro válido.\033[m')
        if ok :
            break
    return valor
#pp
n = leiaint('Digite um valor:')
print(f'Você acabou de digitar o número {n}')

#EX 105
print('{:=^40}'.format('Mundo 3 - FUNÇÃO  '))
def notas(*notas,sit=False):
    """
    :param notas:
    :param sit:
    :return:
    """
    registro = {}
    registro['Total'] = len(notas)
    registro['Maior'] = max(notas)
    registro['Menor'] = min(notas)
    total = 0
    media =[]
    for c, v in enumerate(notas) :
        total += v
        media.append(total/len(notas))
    registro['Media'] = max(media)
    if sit == True :
        if registro['Media'] >= 7 :
            registro['Situação'] = str('BOA')
            print(registro)
        elif registro['Media'] >= 5 and registro['Media'] < 7 :
            registro['Situação'] = str('RAZOÁVEL')
            print(registro)
        else :
           registro['Situação'] = str('RUIM')
           print(registro)
    elif sit == False :
        print(registro)
#PP
notas(8,1,6,1,sit=True)
help(notas)



#EX 106
print('{:=^40}'.format('Mundo 3 - FUNÇÃO -  SISTEMA DE AJUDA PYTHON '))
while True :
 import time
 time.sleep(1)
 def titulo(txt):
    print('\033[1;42m~' * len(txt)) # PARA ACOMPAANHAR O TAMANDO DO TEXTO
    print(txt)
    print('~'* len(txt))
 titulo('SISTEMA DE AJUDA pyHELP')
 opcao = str(input('\033[mFunção ou Biblioteca >')).strip().lower()
 if opcao == 'fim':
     def fim(txt):
       print('\033[1;41m~' * len(txt)) # PARA ACOMPAANHAR O TAMANDO DO TEXTO
       print(txt)
       print('~'* len(txt))
       print('\033[m')
     fim('Programa encerrado!Até logo!')
     break
 def acesso(txt):
    print('\033[1;44m~' * len(txt)) # PARA ACOMPAANHAR O TAMANDO DO TEXTO
    print(txt)
    print('~'* len(txt))
 acesso(f'Acessando o manual do commando {opcao}')
 print('\033[mCarregando...')
 time.sleep(3)
 help(f'{opcao}')
