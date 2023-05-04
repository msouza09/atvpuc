from function.funcoes_estudantes import *
from function.funcoes_professores import *
from function.funcoes_disciplinas import *
from function.funcoes_turmas import *
from function.funcoes_matriculas import *

def menu_principal(estudantes, professores, disciplinas, turmas, matriculas): 
    while True:
        print('\n---MENU PRINCIPAL---\n')
        print('1. Estudantes')
        print('2. Disciplinas')
        print('3. Professores')
        print('4. Turmas')
        print('5. Matriculas')
        print('0. Sair')
        opcao = int(input('\nDigite a opção desejada: '))

        if opcao == 0:
            break
        elif opcao == 1:
            menu_estudantes(estudantes)
        elif opcao == 2:
            menu_disciplinas(disciplinas)
        elif opcao == 3:
            menu_professores(professores)
        elif opcao == 4:
            menu_turmas(estudantes)
        elif opcao == 5:
            menu_matriculas(matriculas)
        else:
            print('Opção inválida, tente novamente.')

#Estudantes

def menu_estudantes(estudantes):
    while True:
        print('\n---[ESTUDANTES] MENU DE OPERAÇÕES---\n')
        print('1. Incluir')
        print('2. Listar')
        print('3. Atualizar')
        print('4. Excluir')
        print('0. Voltar ao menu principal')
        opcao_estudante = int(input('\nDigite a opção desejada: '))

        if opcao_estudante == 0:
            break
        elif opcao_estudante == 1:
            incluir_estudante(estudantes)
        elif opcao_estudante == 2:
            listar_estudantes(estudantes)
        elif opcao_estudante == 3:
            atualizar_estudante(estudantes)
        elif opcao_estudante == 4:
            excluir_estudante(estudantes)
        else:
            print('Opção inválida. Tente novamente.')

#Professores

def menu_professores(professores):
    while True:
        print('\n---[PROFESSORES] MENU DE OPERAÇÕES---\n')
        print('1. Incluir')
        print('2. Listar')
        print('3. Atualizar')
        print('4. Excluir')
        print('0. Voltar ao menu principal')
        opcao_professor = int(input('\nDigite a opção desejada: '))

        if opcao_professor == 0:
            break
        elif opcao_professor == 1:
            incluir_professor(professores)
        elif opcao_professor == 2:
            listar_professores(professores)
        elif opcao_professor == 3:
            atualizar_professor(professores)
        elif opcao_professor == 4:
            excluir_professor(professores)
        else:
            print('Opção inválida. Tente novamente.')

#Disciplinas 

def menu_disciplinas(disciplinas):
    while True:
        print('\n---[DISCIPLINA] MENU DE OPERAÇÕES---\n')
        print('1. Incluir')
        print('2. Listar')
        print('3. Atualizar')
        print('4. Excluir')
        print('0. Voltar ao menu principal')
        opcao_disciplinas = int(input('\nDigite a opção desejada: '))

        if opcao_disciplinas == 0:
            break
        elif opcao_disciplinas == 1:
            incluir_disciplina(disciplinas)
        elif opcao_disciplinas == 2:
            listar_disciplinas(disciplinas)
        elif opcao_disciplinas == 3:
            atualizar_disciplina(disciplinas)
        elif opcao_disciplinas == 4:
            excluir_disciplina(disciplinas)
        else:
            print('Opção inválida. Tente novamente.')

#Turmas

def menu_turmas(turmas):
    while True:
        print('\n---[TURMAS] MENU DE OPERAÇÕES---\n')
        print('1. Incluir')
        print('2. Listar')
        print('3. Atualizar')
        print('4. Excluir')
        print('0. Voltar ao menu principal')
        opcao_turmas = int(input('\nDigite a opção desejada: '))

        if opcao_turmas == 0:
            break
        elif opcao_turmas == 1:
            incluir_turma(turmas)
        elif opcao_turmas == 2:
            listar_turmas(turmas)
        elif opcao_turmas == 3:
            atualizar_turma(turmas)
        elif opcao_turmas == 4:
            excluir_turma(turmas)
        else:
            print('Opção inválida. Tente novamente.')

#Matriculas

def menu_matriculas(matriculas):
    while True:
        print('\n---[MATRICULAS] MENU DE OPERAÇÕES---\n')
        print('1. Incluir')
        print('2. Listar')
        print('3. Atualizar')
        print('4. Excluir')
        print('0. Voltar ao menu principal')
        opcao_matriculas = int(input('\nDigite a opção desejada: '))

        if opcao_matriculas == 0:
            break
        elif opcao_matriculas == 1:
            incluir_matricula(matriculas)
        elif opcao_matriculas == 2:
            listar_matriculas(matriculas)
        elif opcao_matriculas == 3:
            atualizar_matricula(matriculas)
        elif opcao_matriculas == 4:
            excluir_matricula(matriculas)
        else:
            print('Opção inválida. Tente novamente.')