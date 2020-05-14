def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f"\033[31mERRO! Digite um número inteiro válido\033[m")
            continue
        except (KeyboardInterrupt):
            print(f"\033[31mEntrada de dados interrompida pelo usuário\033[m")
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f"\033[31mERRO! Digite um número real válido\033[m")
            continue
        except (KeyboardInterrupt):
            print(f"\033[31mEntrada de dados interrompida pelo usuário\033[m")
            return 0
        else:
            return n

def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução

limpa()
x = leiaInt("Digite um Inteiro: ")
print(x)
y = leiaFloat("Digite um Float: ")
print(y)