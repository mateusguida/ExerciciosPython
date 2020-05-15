from lib.interface import *

def arquivoExiste(arq):
    try:
        # r = read, t= text -> lê um arquivo.
        a= open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArquivo(arq):
    try:
        # w = write, t= text -> escreve um arquivo.
        # se não existir, o '+' indica que se crie o arquivo.
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {arq} criado com sucesso!')

def lerArquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Houve um ERRO ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30} {dado[1]:>3} anos')

    finally:
        a.close()
    
def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO ao abrir o arquivo!')
    else:
        
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()