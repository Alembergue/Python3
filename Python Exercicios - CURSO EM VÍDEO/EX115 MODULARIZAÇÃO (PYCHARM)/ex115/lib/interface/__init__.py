def leiaint(msg):
      while True :
          try:
             numero = int(input(msg))
          except(TypeError,ValueError):
             print('\033[1;31mERROR!Digite uma opção válida!\033[m')
             continue
          except(KeyboardInterrupt):
              print('\033[1;31mOperação interrompida pelo usuário!\033[m')
              return 0
          else:
              return numero

def linha(tam=42):
    return '-'*tam

def cabecalho (txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c=1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c = c+1
    print(linha())
    opc = leiaint('\033[1;32mSua Opção:\033[m')
    return opc
