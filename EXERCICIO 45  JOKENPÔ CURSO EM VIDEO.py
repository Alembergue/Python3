#45 JOKENPÔ 
import random
import time
print('{:=^40}'.format('JOKENPÔ'))
print('OPÇÕES:\n[0] PEDRA\n[1] PAPEL\n[2] TESOURA')
itens = ('PEDRA','PAPEL','TESOURA')
jogador = int(input('Qual é sua jogada ?'))
maquina = random.randint(0,2)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!!')
print('=-'*20)
print('              RESULTADO')
print('=-'*20)
if   jogador == 0 and maquina == 1 :
      print('JOGADOR = {}\nMAQUINA = {}\n\033[1;31mMAQUINA VENCEU!!\033[m'.format(itens[jogador],itens[maquina]))

elif jogador == 0 and maquina == 2 :
      print('JOGADOR = {}\nMAQUINA = {}\n\033[1;32mJOGADOR VENCEU!\033[m'.format(itens[jogador],itens[maquina]))

elif jogador == 1 and maquina == 0 :
      print('JOGADOR = {}\nMAQUINA = {}\n\033[1;32mJOGADOR VENCEU!!\033[m'.format(itens[jogador],itens[maquina]))

elif jogador == 1 and maquina == 2 :
      print('JOGADOR = {}\nMAQUINA = {}\n\033[1;31mMAQUINA VENCEU!!\033[m'.format(itens[jogador],itens[maquina]))

elif jogador == 2 and maquina == 1 :
      print('JOGADOR = {}\nMAQUINA = {}\n\033[1;32mJOGADOR VENCEU!!\033[m'.format(itens[jogador],itens[maquina]))

elif jogador == 2 and maquina == 0 :
      print('JOGADOR = {}\nMAQUINA = {}\n\033[1;31mMAQUINA VENCEU!!\033[m'.format(itens[jogador],itens[maquina]))

elif jogador > 2 :
      print('\033[1;31mEsta opção não é valida! tente uma das opções mencionadas nas instruções!\033[m')
else:
     print('JOGADOR = {}\nMAQUINA = {}\n\033[1;33mEMPATAMOS!!\033[m'.format(itens[jogador],itens[maquina]))
    