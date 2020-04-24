num = int(input("Digite um número inteiro: "))

print("Escolha uma das bases para conversão:")
print("[ 1 ] converter para {}BINÁRIO{}".format('\033[31m', '\033[m'))
print("[ 2 ] converter para {}OCTAL{}".format('\033[32m', '\033[m'))
print("[ 3 ] converter para {}HEXADECIMAL{}".format('\033[33m', '\033[m'))

op = int(input("Sua opção: "))

if op == 1:
    print('{} convertido para {}BINÁRIO{} é igual a {}'.format(num, '\033[31m', '\033[m', bin(num)[2:]))
    # o [2:] serve para eliminar o 0b/0o/0x padrão pós conversão

elif op == 2:
    print('{} convertido para {}OCTAL{} é igual a {}'.format(num, '\033[32m', '\033[m', oct(num)[2:]))

elif op == 3:
    print('{} convertido para {}BINÁRIO{} é igual a {}'.format(num, '\033[33m', '\033[m', hex(num)[2:]))
    
else:
    print("Opção inválida. Tente novamente.")