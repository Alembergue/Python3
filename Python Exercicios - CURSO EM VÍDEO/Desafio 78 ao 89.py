# 78MAIORES E MENORES ADICIONADOS NA LISTA
num = list()
for contador in range (0,5) :
    num.append(int(input(f'Digite um valor para a posição {contador}:')))
print(f'Os valores digitados foram {num}')
print(f'O maior valor digitado foi {max(num)} nas posições ' ,end= '')
for posicao,valor in enumerate(num) :
    if valor == max(num) :
        print(f'...{posicao}',end=' ')
print(f'\nO menor valor digitado foi {min(num)} nas posições ',end ='')
for posicao,valor in enumerate(num) :
    if valor == min(num) :
        print(f'...{posicao} ',end='')

#EX 79 ADICIONANDO NUMEROS NÃO REPETIDOS
print('{:=^40}'.format('ADICIONANDO NUMEROS NÃO REPETIDOS'))
lista = []
while True :
    valor = (int(input('Digite uma valor:')))
    if valor in lista :
        print('Valor duplicado,Não sera adicionado')
    else :
        lista.append(valor)
        print('Valor Adicionado com sucesso!')
    continuar = str(input('Deseja continuar ? [S/N]')).upper().strip()
    while continuar != 'N'and continuar != 'S' :
            print('Opção Invalida!,Tente Novamente!')
            continuar = str(input('Deseja continuar ? [S/N]')).upper().strip()
    if 'S'in continuar :
        print('Continuando...')
    elif 'N' in continuar :
        break
print(f'Foi adicionado os valores {sorted(lista)}')

#EX 80 LISTA ORDENADA
print('{:=^40}'.format('LISTA ORDENADA'))
lista = []
for c in range (0,5) :
    numero = int(input('Digite uma valor :'))
    if c == 0 or numero > max(lista) :
        lista.append(numero)
        print('Adicionado ao final da lista')
    else :
        for posicao,valor in enumerate(lista) :
            if numero < valor :
                lista.insert(posicao,numero)
                print(f'adicionado a posição {posicao} da lista')
                break
print(f'Os valores digitados em ordem foram {lista}')

#EX 80 LISTA ORDENADA POR GUANABARA
print('{:=^40}'.format('SELECIONADNO POSIÇÕES'))
lista = []
for c in range (0,5) :
    numero = int(input('Digite um valor :'))
    if c == 0 or numero > lista[-1] :
        lista.append(numero)
        print('Adicionado ao final da lista...')
    else :
        pos = 0
        while pos < len(lista) :
            if numero <= lista[pos] :
                lista.insert(pos,numero)
                print(f'Adicionado na posição {pos} da lista ...')
                break
            pos+=1
print(f'Os valores digitados foram {lista}')

#EX 81
print('{:=^40}'.format('Mundo 3 - Lendo lista e posição'))
import time
lista =[]
while True :
    lista.append(int(input('Digite um valor :')))
    print('\033[1;33mAdicionando...\033[m')
    time.sleep(2)
    print('\033[1;32mValor adicionado com sucesso!\033[m')
    continuar = str(input('Deseja continuar:[S/N]')).upper().strip()

    while continuar != 'S' and continuar != 'N' :
        print('\033[1;31Opção invalida! Tente novamente!\033m')
        continuar = str(input('Deseja continuar:[S/N]')).upper().strip()
    if 'N' in continuar :
        break
print('-='*19)
print(f'Foram digitadoas {len(lista)} elementos.')
print(f'Os valores em ordem decrescente são ' ,end='')
print(sorted(lista,reverse=True)) # para ordem reversa
if 5 in lista :
    print(f'O valor 5 faz parte da lista na posição {lista.index(5)+1}')
else:
    print('\033[1;31O valor 5 não faz parte da lista\033[m')
print('-='*19)

#EX 82
print('{:=^40}'.format('Mundo 3 - Usando + Listas'))
lista = []
listapar = []
listaimpar = []
while True :
    valor = (int(input('Digite um valor :')))
    lista.append(valor)
    continuar = str(input('Deseja continuar?[S/N]')).upper().strip()
    par = valor % 2
    if par == 0 :
        listapar.append(valor)
    else:
        listaimpar.append(valor)
    while continuar != 'S' and continuar != 'N' :
        print('\033[1;31Opção Invalida! tente novamente!\033m')
        continuar = str(input('Deseja continuar?[S/N]')).upper().strip()
    if continuar == 'N':
        break
print('-='*19)
print(f'A lista completa é {lista}')
print(f'A lista de numeros pares é {sorted(listapar)}')
print(f'A lista de numeros impares é {sorted(listaimpar)}')


#EX 83
print('{:=^40}'.format('Mundo 3 - Lendo expressões matematicas'))
expressao = str(input('Digite uma expressão:'))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb ==')':
        if len(pilha) > 0 :
            pilha.pop() # remove ultimo iten da pilha
        else:
            pilha.append(')')
            break
if len(pilha) == 0 :
    print('Sua expressão esta valida')
else:
    print('Sua expressão está errada!')


#EX 84
print('{:=^40}'.format('Mundo 3 - separando pesos'))
lista =[]
dado = []
total = 0
pesomaior = pesomenor =  0
while True :
    nome = str(input('Nome:'))
    dado.append(nome)
    peso = float(input('Peso:'))
    dado.append(peso)
    continuar = str(input('Deseja continuar?[S/N]')).upper().strip()
    total = total + 1
    lista.append(dado[:])
    dado.clear()
    while continuar != 'N' and continuar != 'S' :
        print('\033[1;31mOpção invalida!Tente novamente\033[m')
        continuar = str(input('Deseja continuar?[S/N]')).upper().strip()
    if continuar == 'N':
        break
for p in lista :
    if p[1] > pesomaior :
        pesomaior = p[1]

    elif p[1] < pesomaior:
            pesomenor = p[1]
print('-='*19)
print(f'Ao todo foram cadastradas {total} pessoas!')
print(f'O maior peso cadastradado foi de {pesomaior}Kg. Peso de ',end=' ')
for p in lista :
    if p[1] == pesomaior :
        print(f'[{p[0]}]',end=' ')
if pesomenor == 0 :
        print('\n\033[1:33Não foi identificado o menor peso!A lista possui pesos de mesmo valor!\033[m')
print(f'\nO menor peso cadastrado foi de {pesomenor}Kg. Peso de ',end=' ')
for p in lista :
    if p[1] == pesomenor:
        print(f'[{p[0]}]',end=' ')

#EX 85 pares e impares com 1 lista
print('{:=^40}'.format('Mundo 3 - pares e impares com 1 lista'))
lista = [[],[]]
cont = 0
for c in range (0,7) :
    valor = int(input(f'Digite o valor {cont + 1}° :'))
    cont = cont +1
    par = valor % 2
    if par == 0 :
      lista[0].append(valor)
    else :
      lista[1].append(valor)
print(f'Os valores pares são - {sorted(lista[0])}')
print(f'Os valores impares são - {sorted(lista[1])}')

#EX 86 LISTA COM MATRIZ
print('{:=^40}'.format('Mundo 3 - Matriz'))
lista = [[],[],[]]
cont = cont2 = cont4 = cont6 = 0
cont3 = 1
cont5 = 2
for c in range (0,3) :
    valor = int(input(f'Digite um valor para a posição {[cont,cont2]}:'))
    cont2 = cont2+1
    lista[0].append(valor)
for c1 in range (0,3) :
    valor = int(input(f'Digite um valor para a posição {[cont3,cont4]}:'))
    cont4 = cont4 + 1
    lista[1].append(valor)
for c2 in range (0,3):
    valor = int(input(f'Digite um valor para a posição {[cont5,cont6]}:'))
    cont6 = cont6 + 1
    lista[2].append(valor)
print(f'[{lista[0][0]:^5}] [{lista[0][1]:^5}] [{lista[0][2]:^5}]')
print(f'[{lista[1][0]:^5}] [{lista[1][1]:^5}] [{lista[1][2]:^5}]')
print(f'[{lista[2][0]:^5}] [{lista[2][1]:^5}] [{lista[2][2]:^5}]')

#EX 86 LISTA COM MATRIZ (MODO 2 )
print('{:=^40}'.format('Mundo 3 - Matriz'))
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range (0,3) :
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]:'))
print('=-'*30)
for l in range (0,3) :
    for c in range (0,3) :
        print(f'[{matriz[l][c]:^5}]',end ='')
    print()

#EX 87 LISTA COM MATRIZ COM APRES E IMAPRES
print('{:=^40}'.format('Mundo 3 - Matriz com pares e imapares'))
lista = [[],[],[]]
listapar = [[],[],[]]
cont = cont2 = cont4 = cont6 = 0
cont3 = 1
cont5 = 2
for c in range (0,3) :
    valor = int(input(f'Digite um valor para a posição {[cont,cont2]}:'))
    cont2 = cont2+1
    lista[0].append(valor)
    if valor%2 == 0 :
       listapar[0].append(valor)
    else:
       valor1 = 0
       listapar[0].append(valor1)
soma = listapar[0][0] + listapar[0][1] + listapar[0][2]
for c1 in range (0,3) :
    valor = int(input(f'Digite um valor para a posição {[cont3,cont4]}:'))
    cont4 = cont4 + 1
    lista[1].append(valor)
    if valor%2 == 0 :
       listapar[1].append(valor)
    else:
       valor2 = 0
       listapar[1].append(valor2)
soma2 = listapar[1][0] + listapar[1][1] + listapar[1][2]
for c2 in range (0,3):
    valor = int(input(f'Digite um valor para a posição {[cont5,cont6]}:'))
    cont6 = cont6 + 1
    lista[2].append(valor)
    if valor%2 == 0 :
        listapar[2].append(valor)
    else:
       valor3 = 0
       listapar[2].append(valor3)
soma3 = listapar[2][0] + listapar[2][1] + listapar[2][2]
print('=-'*30)
print(f'[{lista[0][0]:^5}] [{lista[0][1]:^5}] [{lista[0][2]:^5}]')
print(f'[{lista[1][0]:^5}] [{lista[1][1]:^5}] [{lista[1][2]:^5}]')
print(f'[{lista[2][0]:^5}] [{lista[2][1]:^5}] [{lista[2][2]:^5}]')
print('=-'*30)
print(f'A soma dos valores pares é {soma + soma2 +soma3}.')
print(f'A soma dos valores da terceira coluna é {lista[0][2]+lista[1][2]+lista[2][2]}.')
print(f'O maior valor da segunda linha é {max(lista[1])}.')

#EX 87 LISTA COM MATRIZ COM PARES E IMPARES (MODO 2 )
print('{:=^40}'.format('Mundo 3 - Matriz com pares e imapares'))
matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol = 0
for l in range (0,3) :
    for c in range (0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]:'))
print('=-'*30)
for l in range (0,3) :
    for c in range (0,3) :
        print(f'[{matriz[l][c]:^5}]',end ='')
        if matriz [l][c] % 2 == 0 :
            spar +=matriz[l][c]
    print()
print('=-'*30)
print(f'A soma do valores pares é {spar}')
for l in range(0,3) :
    scol+= matriz [l][2]
print(f'A soma dos valores da terceira coluna é {scol}')
for c in range (0,3) :
    if c == 0 :
        mai = matriz[1][c]
    elif matriz [1] [c] > mai :
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}')

#EX 88 GERADOR DE JOGOS
print('{:=^40}'.format('Mundo 3 - Gerador de palpites'))
import random
import time
palpites =[]
print('-'*30)
print('      JOGA NA MEGA SENA    ')
print('-'*30)
valor = int(input('Quantos jogos você quer que eu sorteie?'))
print(f'-=-=-= SORTEANDO {valor} JOGOS -=-=-=')
for c in range(0,valor) :
    time.sleep(2)
    jogo = random.sample(range(1,60),6)
    print(f'jOGO {c+1}:{sorted(jogo)}')
    palpites.append(jogo)
time.sleep(1)
print('-'*30)
print(f'     IMPRIMINDO BILHETES')
print('-'*30)
time.sleep(5)
for i,p in enumerate (palpites):
   print(f'Jogo {i+1}: {sorted(p)}')
print('{:=^30}'.format('<BOA SORTE>'))

#EX 89 BOLETIM
print('{:=^40}'.format('Mundo 3 -Boletim Escolar '))
dados = []
while True :
    nome = str(input('Nome:')).upper().strip()
    nota1 = float(input('Nota 1 :'))
    nota2 = float(input('Nota 2 :'))
    media = (nota1 + nota2)/2
    dados.append([nome,[nota1,nota2],media])
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        print('Opção Invalida!Tente Novamente!')
        continuar = str(input('Deseja continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break
print('-='*25)
print('-='*4,'BOLETIM','-='*4)
print(f'{"No":<4}{"NOME":<10} {"MÉDIA":>8}')
print('-'*24)
for c , aluno in enumerate (dados) :
    print(f'{c:<4}{aluno[0]:<10}{aluno[2]:>8.1f}') #aluno 2 = media
print('-'*24)
while True :
    verificar = int(input('Deseja verificar a nota de qual aluno? [999 para encerrar]'))
    if verificar == 999 :
        break
    if verificar <= len(dados) - 1 :
        print(f'As notas do aluno(a) {dados[verificar][0]} são {dados[verificar][1]}')
print('FINALIZANDO...')
time.sleep(3)
print('Programa encerrado!')
