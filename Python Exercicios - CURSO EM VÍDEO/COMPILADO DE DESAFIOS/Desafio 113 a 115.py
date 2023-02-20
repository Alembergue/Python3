#EX 113
print('{:=^40}'.format('Mundo 3 - FUNÇÃO -  Tratamento de erros'))

def leiaint(msg):
      while True :
          try:
             numero = int(input(msg))
          except(TypeError,ValueError):
             print('\033[1;31mERROR!O valor nâo é valido!\033[m')
             continue
          except(KeyboardInterrupt):
              print('\033[1;31mOperação interrompida pelo usuário!\033[m')
              return 0
          else:
              return numero

def leiareal(msg):

    while True :
        try:
            nreal = float(input(msg))
        except(TypeError,ValueError):
             print('\033[1;31mERROR!O valor nâo é valido!\033[m')
             continue
        except(KeyboardInterrupt):
              print('\033[1;31mOperação interrompida pelo usuário!\033[m')
              return 0
        else:
            return nreal
#pp
numero = leiaint('Digite um valor inteiro:')
nreal = leiareal('Digite um valor real:')
print(f'Você acabou de digitar o número inteiro {numero} e o real foi {nreal}')

#EX 114
print('{:=^40}'.format('Mundo 3 - FUNÇÃO - Verificação de servidor disponivel'))
import urllib.request
try:
    site =urllib.request.urlopen("http://pudim.com.br/")
except(urllib.request.URLError):
    print("\033[1;31mO servidor está indisponível.\033[m")
else:
    print("\033[1;32mO servidor está disponível.\033[m")
    print(site.read()) #mostar o codigo do site inteiro


#EX115A
