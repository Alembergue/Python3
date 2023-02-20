from ex115.lib.interface import *
from ex115.lib.arquivo import *
import time

arq = 'cursoemvideo.txt'

#if arquivoExiste(arq):
#    print('Arquivo encontrado com sucesso!')
#else:
#    print('Arquivo não encontrado!')
#   criarArquivo(arq)

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
     resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
     if resposta == 1 :
         #opção de listar o conteudo de uma arquivo
         lerArquivo(arq)
     elif resposta == 2:
         #opção de cadastrar uma nova pessoa
         cabecalho('NOVO CADASTRO')
         nome = str(input('Nome:'))
         idade =leiaint('Idade:')
         cadastrar(arq,nome,idade)

     elif resposta == 3 :
         cabecalho('Saindo do sistema...Até logo!')
         break
     else:
         print('\033[1;31mERRO!Digite uma opção válida!\033[m')
     time.sleep(2)
