import os
os.system("cls") #limpa janela terminal antes da execução

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))

flag = False
while flag == False:
    print("    [ 1 ] somar")
    print("    [ 2 ] multiplicar")
    print("    [ 3 ] maior")
    print("    [ 4 ] novos números")
    print("    [ 5 ] sair do programa")
    op = int(input(">>>>> Qual é a sua opção? "))

    if op == 1:
        print(f'A soma dos números {n1} e {n2} é {n1+n2}.')

    elif op == 2:
        print(f'A multiplicação dos números {n1} e {n2} é {n1*n2}.')

    elif op == 3:
        if n1 > n2:
            print(f'{n1} é maior do que {n2}.')
        elif n2 > n1:
            print(f'{n2} é maior do que {n1}.')
        else:
            print(f'{n1} é igual a {n2}.')

    elif op == 4:
        print("Informe os números novamente:")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))

    elif op == 5:
        flag = True

    else:
        print("Opção inválida! Escolha outra opção: ")

    print('=-=' * 10)

print("Fim do programa! Volte sempre!")