
def metade(n):
    resultado = n / 2
    return resultado

def dobro(n):
    resultado = n * 2
    return resultado

def aumento10(n):
    aumento = (n * 10) /100
    resultado = n + aumento
    return resultado

def reduzindo13(n):
    redu = (n * 13) /100
    resultado = n - redu
    return resultado

def moeda(preço = 0,moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')
