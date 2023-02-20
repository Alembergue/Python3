print('{:=^40}'.format('Mundo 3 - FUNÇÃO -  SISTEMA DE AJUDA PYTHON '))
#pp
import moeda
numero =float(input('Digite o preço:R$'))
print(f'A metade de {numero} é {moeda.metade(numero)}.')
print(f'O dobro de {numero} é {moeda.dobro(numero)}.')
print(f'Aumentando 10%,temos {moeda.aumento10(numero)}')
print(f'Reduzindo 13%,temos {moeda.reduzindo13(numero)}')
