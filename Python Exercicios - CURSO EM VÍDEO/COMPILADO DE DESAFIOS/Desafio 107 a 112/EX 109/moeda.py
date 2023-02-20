
def aumentar(preco,show=False):
    preco = preco + (preco * 10 )/ 100

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
