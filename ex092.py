import os
os.system("cls") #limpa janela terminal antes da execução

from datetime import date

func = dict()

func["nome"] = str(input("Nome: "))
func["idade"] = date.today().year - int(input("Ano de Nascimento: "))
func["ctps"] = int(input("Carteira de Trabalho (0 não tem): "))

if func["ctps"] != 0:
    func["contratação"] = int(input("Ano de Contratação: "))
    func["salário"] = float(input("Salário: "))
    func["aposentadoria"] = func["contratação"] + 35 - date.today().year + func["idade"]

print('-=' * 30)
for k, v in func.items():
    print(f"  - {k} tem o valor {v}")
print()