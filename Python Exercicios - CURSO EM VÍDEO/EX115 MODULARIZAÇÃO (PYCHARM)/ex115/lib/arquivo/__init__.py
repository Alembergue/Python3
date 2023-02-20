from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome,'rt')      # para abrir o arquivo r = read t = text
        a.close()
    except FileNotFoundError :
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome,'wt+')  # para criar o arquivo w = write t = text  + = caso o arquivo n exista ele criar
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'arquivo {nome} \033[1;32mcriado com sucesso!\033[m')


def lerArquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq,nome='desconhecido',idade=0):
    try:
        a = open(arq, 'at')  # a = append t = text
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de \033[1;34m{nome}\033[m adicionado.')
            a.close()

