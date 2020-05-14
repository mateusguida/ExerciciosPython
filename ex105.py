def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    turma = dict()
    turma['total'] = len(n)
    turma['maior'] = max(n)
    turma['menor'] = min(n)
    turma['media'] = sum(n)/len(n)

    if sit:
        if media >= 7:
            turma['situação'] = 'BOA'
        elif media >= 5:
            turma['situação'] = 'RAZOÁVEL'
        else:
            turma['situação'] = 'RUIM'
    
    return turma


def limpa():
    import os
    os.system("cls") #limpa janela terminal antes da execução

limpa()
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
print()
resp = notas(5.5, 2.5, 1.5)
print(resp)
print()
resp = notas(5.5, 2.5, 10, 6.5, sit=True)
print(resp)
print()
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)