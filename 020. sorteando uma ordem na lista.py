import random

aluno1 = str(input('Digite um nome: '))
aluno2 = str(input('Digite mais um nome: '))
aluno3 = str(input('Digite outro nome: '))
aluno4 = str(input('Digite o último nome: '))
alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)
print('A ordem aleatória é {}.'.format(alunos))