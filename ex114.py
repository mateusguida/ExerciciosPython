import urllib
import urllib.request

def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução

limpa()
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Erro de conexão...')
else:
    print('Tudo ok!')