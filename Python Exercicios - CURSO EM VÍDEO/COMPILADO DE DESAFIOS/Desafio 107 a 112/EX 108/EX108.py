print('{:=^40}'.format('Mundo 3 - FUNÇÃO -  SISTEMA DE AJUDA PYTHON '))
#pp
import moeda
numero = float(input('Digite o preço:R$'))
print(f'A metade de {moeda.moeda(numero)} é {moeda.moeda(moeda.metade(numero))}.')
print(f'O dobro de {moeda.moeda(numero)} é {moeda.moeda(moeda.dobro(numero))}.')
print(f'Aumentando 10%,temos {moeda.moeda(moeda.aumento10(numero))}')
print(f'Reduzindo 13%,temos {moeda.moeda(moeda.reduzindo13(numero))}')
