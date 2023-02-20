

def aumentar(preco,show=False):
    preco = preco + (preco * 13 )/ 100

    if show:
        return moeda(preco)
    else:
        return preco


def diminuir(preco,show=False):
    preco = preco - (preco * 13) / 100

    if show:
        return moeda(preco)
    else:
        return preco


def dobro(preco, show=False):
    preco *= 2

    if show:
        return moeda(preco)
    else:
        return preco


def metade(preco, show=False):
    preco /= 2

    if show:
        return moeda(preco)
    else:
        return preco


def moeda(preco):
    return f'R${preco:.2f}'.replace('.', ',')


def resumo(preco,a=0,b=0):
    print(f'-'*40)
    tit= 'RESUMO DO VALOR'
    titulo = tit.center(40)
    print(titulo)
    print(f'-'*40)
    print(f'Preço analisado: \t{moeda(preco)}') #\t para alinhar a tabulação.. tme que ter um espaço antes do \t
    print(f'Dorbo do preço: \t{dobro(preco,show=True)}')
    print(f'Metade do preço:\t{metade(preco,show= True)}')
    aumento = preco + (preco * a )/ 100
    print(f'{a}% de aumento: \t{moeda(aumento)}')
    reduzir = preco - (preco * b) / 100
    print(f'{b}% de aumento:  \t{moeda(reduzir)}')
    print(f'-'*40)


