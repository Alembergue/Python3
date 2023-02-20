#EX 90
print('{:=^40}'.format('Mundo 3 -Media - Dicionario '))
dados = {}
dados['nome'] = str(input('Nome :')).strip()
dados['média']= float(input(f'Média de {dados["nome"]} :'))
print('-='*30)
print(f' - Aluno {dados["nome"]}.')
print(f' - Média = {dados["média"]}')
if dados["média"] < 5:
    dados['situação'] = 'Reprovado'
    print(f' - Aluno \033[1;31m{dados["situação"]}\033[m.')
elif dados["média"] >=5 and dados["média"] < 7:
    dados['situação'] = 'Recuperção'
    print(f' - Aluno em \033[1;33m{dados["situação"]}\033[m.')
else:
    dados["situação"] = 'Aprovado'
    print(f' - O aluno \033[1;32m{dados["situação"]}\033[m.')
print('-='*30)

#EX 90  COM FOR
print('{:=^40}'.format('Mundo 3 -Media - Dicionario '))
dados = {}
dados['nome'] = str(input('Nome :')).strip()
dados['média']= float(input(f'Média de {dados["nome"]} :'))
print('-='*30)
if dados["média"] < 5:
    dados['situação'] = 'Reprovado'
elif dados["média"] >=5 and dados["média"] < 7:
    dados['situação'] = 'Recuperção'
else:
    dados["situação"] = 'Aprovado'
for k,v in dados.items():
    print(f' - {k} é igual a {v}')
print('-='*30)

#EX 91
print('{:=^40}'.format('Mundo 3 - Dicionario -jogo de dados'))
import random
import time
dados = {}
final = []
iniciar = input()
time.sleep(1)
print('Valores sorteados:')
for c in range(0,4) :
    dados['jogador'] = c+1
    dados['valor'] = random.randint(0,6)
    print(f'    O Jogador{dados["jogador"]} tirou {dados["valor"]} no dado.')
    final.append(dados.copy())
    time.sleep(1)
final = sorted(final,key=lambda k:(k['jogador']), reverse=True)
print('Ranking dos jogadores :')
for c in final:
    print(f'    {final.index(c)+1}° lugar : jogador {c["jogador"]} com {c["valor"]}')
    time.sleep(1)
print('-=PROGRAMA ENCERRADO=-')

#EX 91 MODO 2
print('{:=^40}'.format('Mundo 3 - Dicionario -jogo de dados'))
import random
import time
from operator import itemgetter
input()
jogo = {'Jogador1':random.randint(1,6),
        'Jogador2':random.randint(1,6),
        'Jogador3':random.randint(1,6),
        'Jogador4':random.randint(1,6)
        }
ranking = list()
print('   == VALORES SORTEADOS: ==')
for k,v in jogo.items():
    print(f'   {k} tirou {v} no dado.')
    time.sleep(1)
ranking = sorted(jogo.items(),key=itemgetter(1),reverse=True)
print('-='*30)
print('  == RANKING DOS JOGDORES ==')
for i,v in enumerate(ranking) :
    print(f'   {i+1}° lugar {v[0]} com {v[1]}')
    time.sleep(1)
print()
print('   -=PROGRAMA ENCERRADO=-')

#EX 92
print('{:=^40}'.format('Mundo 3 - Aposentadoria '))
from datetime import date
dados = {}
dados['nome'] = str(input('Nome:')).upper().strip()
idade = int(input('Ano de nascimento :'))
dados['idade'] = date.today().year - idade
if dados['idade'] >= 15 and dados['idade'] < 18 :
    print('Liberado apenas para trabalhar como menor aprendiz!')
elif dados['idade'] < 15 :
    print('Menor de idade , não esta liberado para trabalhar!')
if dados['idade'] >= 18 :
  dados['ctps'] = int(input('Carteira de trabalaho[N°0 não tem]:'))
  if  dados['ctps'] == 0 :
    print('-='*40)
    print(dados)
    print(f'Nome = {dados["nome"]}\nIdade = {dados["idade"]}\nCTPS = {dados["ctps"]}')
  else:
    contratação = int(input('Ano de contratação:'))
    dados['contratação'] = contratação
    dados['salario'] = int(input('Salário:R$'))
    aposentadoria = dados['idade'] + (date.today().year - contratação)
    dados['aposentadoria'] = aposentadoria
    print('-='*40)
    print(dados)
    for c ,v in dados.items():
       print(f' - {c} : {v}')
print()
print('   -=PROGRAMA ENCERRADO=-')

#EX 93
print('{:=^40}'.format('Mundo 3 - Desempenho jogador '))
dados ={}
gols = []
total = 0
dados['jogador'] = str(input('Nome do jogador :')).strip()
partidas = int(input(f'Quantas partidas {dados["jogador"]} jogou ?'))
for c in range (0,partidas) :
    gol = int(input(f'Quantos gols na partida {c +1}?'))
    gols.append(gol)
    total = total + gol
print('-='*40)
dados['gols'] = gols
dados['total']= total
print(dados)
print('-='*40)
for c , v in dados.items() :
    print(f'{c} : {v}.')
print('-='*40)
print(f'O jogador {dados["jogador"]} jogou {partidas} partidas.')
for c ,n in enumerate(dados['gols']):
    print(f'    => Na partida {c +1},fez {n} gols.')
print()
print(f'Foi um total de {total} gols!')
print()
print()
print('   -=PROGRAMA ENCERRADO=-')


#EX 94
print('{:=^40}'.format('Mundo 3 - Cadastros (lista.dicionario) '))
cadastro = {}
dados = []
dadosf = []
soma = cont = 0
while True :
    nome = str(input('Nome:')).upper().strip()
    cadastro['nome'] = nome
    sexo = str(input('Sexo:[M/F]')).upper()[0].strip()
    cadastro['sexo'] = sexo
    idade = int(input('Idade :'))
    cadastro['idade'] = idade
    if sexo == 'F':
        dadosf.append(nome)
    soma = soma + cadastro['idade']
    dados.append(cadastro.copy())
    continuar = str(input('Deseja continuar?[S/N]')).upper().strip()
    cont = cont + 1
    while continuar != 'S' and continuar != 'N':
        print(f'Opção invalida! Tente novamente!')
        continuar = str(input('Deseja continuar?[S/N]')).upper().strip()
    if continuar == 'N' :
        break
print('-='*40)
print(f' - O grupo tem {len(cadastro)} pessoas cadastradas.')
print(' - A média de idade é de {:.2f} anos.'.format(soma/cont))
print(f' - A lista das mulheres cadastradas é :' , end='')
for c , n in enumerate(dadosf):
        print(f'{n},',end=' ') #imprimir sem parenteses
print()
print(f' - Lista de pessoas com idade acima da média:')
for v in dados:
    if v['idade'] >= (soma/cont):
        print('    ',end='')
        for t , d in v.items():
            print(f'{t} = {d};',end= ' ',)
        print()
print('\n')
print('   -=PROGRAMA ENCERRADO=-')


#EX :95
print('{:=^40}'.format('Mundo 3 - Desempenho jogador '))
jogador = {}
registro = []
gols = []
while True :
    print('-'*42)
    gols.clear()  # limpar os dados ao reiniciar o ciclo para cadastrar novo jogador e não somar os dados
    jogador.clear() # limpar os dados ao reiniciar o ciclo para cadastrar novo jogador e não somar os dados
    jogador['nome'] = str(input('Nome do jogador:'))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou ?'))
    for c in range(0,partidas) :
        gol = int(input(f'Quantos gols na partida {c+1}?'))
        gols.append(gol)
    jogador['gol'] = gols[:]
    jogador['total'] = sum(gols)
    registro.append(jogador.copy())
    continuar = str(input('Deseja continuar?[S/N]')).strip()[0].upper()
    while continuar != 'S' and continuar != 'N':
        print(f'Opção invalida! Tente novamente!')
        continuar = str(input('Deseja continuar?[S/N]')).upper().strip()[0]
    if continuar == 'N' :
        break
print('-='*42)
print('Cod nome        gols      total')
print('-'*42)
for c,v in enumerate(registro):
  print('{:<4}'.format(c+1), end='') # :<4 define a posiçãoq ue você quer a frase
  for k ,valor in registro[c].items():
     print('{:<12}'.format(str(valor)), end='')
  print()
while True :
    print('-'*42)
    pesquisa = int(input('Mostrar dados de qual jogador?[999 - cancelar]'))
    if pesquisa == 999 :
        break
    if pesquisa - 1 >= len(registro) :
       print('\033[1;31mJogador inexistente\033[m!Tente novamente!')
    elif pesquisa - 1 < 0 :
        print('\033[1;31mJogador inexistente\033[m!Tente novamente!')
    else:
        print(f'-- \033[1;34mDADOS DO JOGADOR\033[m => {registro[pesquisa -1]["nome"].upper()}')
        for c ,g in enumerate(registro[pesquisa - 1 ]['gol']):
            print(f'-- Na partida {c+1}, fez {g} gols.')
