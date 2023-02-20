print('{:=^40}'.format('Mundo 3 - FUNÇÃO -  SISTEMA DE AJUDA PYTHON '))
#pp
import moeda
preco = float(input('Digite o preço:R$'))
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, show = True)}.')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, show = True)}.')
print(f'Aumentando 10%,temos {moeda.aumentar(preco, show = True)}')
print(f'Reduzindo 13%,temos {moeda.diminuir(preco, show = True)}')
