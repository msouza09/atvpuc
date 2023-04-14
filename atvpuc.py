import json
import time

def salvar_estudantes(estudantes):
    with open('estudantes.json', 'w') as file:
        json.dump(estudantes, file)
    print('Lista de estudantes salva com sucesso.')

import json

def carregar_estudantes():
    try:
        with open('estudantes.json', 'r') as file:
            estudantes = json.load(file)
    except FileNotFoundError:
        estudantes = []
    return estudantes

import json

def menu_principal(estudantes): 
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
            print('\nEM DESENVOLVIMENTO.\n')
        elif opcao == 3:
            print('\nEM DESENVOLVIMENTO.\n')
        elif opcao == 4:
            print('\nEM DESENVOLVIMENTO.\n')
        elif opcao == 5:
            print('\nEM DESENVOLVIMENTO.\n')
        else:
            print('Opção inválida, tente novamente.')

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

def incluir_estudante(estudantes):
    print('\n==== INCLUSÃO ====\n')
    nome_estudante = input('Digite o nome do estudante: ')
    cod_estudante = int(input('\nCódigo do Estudante: '))
    cpf_estudante = input('\nDigite o CPF do Estudante: ')
    input('\nPressione ENTER para continuar ')
    print('Incluindo usuário, aguarde...')
    time.sleep(1)

    # verificar se o novo código já está em uso
    for estudante in estudantes:
        if estudante['codigo'] == cod_estudante:
            print('Erro: código já existente!')
            return

    # criar um novo estudante com as informações fornecidas
    informacoes_estudante = {"codigo": cod_estudante, "nome": nome_estudante, "cpf": cpf_estudante}

    # adicionar o novo estudante à lista
    estudantes.append(informacoes_estudante)

    # salvar a lista atualizada
    salvar_estudantes(estudantes)

    print('Estudante cadastrado com sucesso.')

def listar_estudantes(estudantes):
    print('Coletando Informações, aguarde...')
    time.sleep(2)
    if len(estudantes) == 0:
        print('Não há estudantes cadastrados')
    else:
        print('\n---LISTAGEM---\n')
        for estudante in estudantes:
            print(estudante)
        input('Pressione ENTER para continuar ')
        


def atualizar_estudante(estudantes):
    print('\n==== ATUALIZAÇÃO ====\n')
    codigo = int(input('Digite o código do estudante que deseja atualizar: '))

    # procurar pelo estudante com o código fornecido
    for estudante in estudantes:
        if estudante['codigo'] == codigo:
            # obter os novos valores do usuário
            nome_estudante = input('Digite o novo nome do estudante: ')
            cpf_estudante = input('Digite o novo CPF do estudante: ')

            # verificar se os campos não estão vazios
            if nome_estudante and cpf_estudante:
                # verificar se o novo código já está em uso
                novo_codigo = int(input('Digite o novo código do estudante: '))
                print('Atualizando dados do usuário, aguarde...')
                time.sleep(2)
                for outro_estudante in estudantes:
                    if outro_estudante['codigo'] == novo_codigo and outro_estudante != estudante:
                        print('Erro: código já existente!')
                        return

                # atualizar os valores do estudante
                estudante['nome'] = nome_estudante
                estudante['cpf'] = cpf_estudante
                estudante['codigo'] = novo_codigo
                

                print(f'Estudante {codigo} atualizado com sucesso!')
                salvar_estudantes(estudantes)
                break
            else:
                print('Erro: todos os campos devem ser preenchidos!')
                return
    else:
        print(f'Não foi encontrado nenhum estudante com o código {codigo}.')

def excluir_estudante(estudantes):
    print('\n==== EXCLUSÃO ====\n')
    codigo = int(input('Digite o código do estudante que deseja excluir: '))
    for estudante in estudantes:
        if estudante['codigo'] == codigo:
            estudantes.remove(estudante)
            input(f'Você deseja excluir o usuário {estudante}? Para confirmar aperte ENTER. ')
            print('Excluindo Estudante, aguarde...')
            time.sleep(2)
            print(f'Estudante {codigo} excluído com sucesso!')
            salvar_estudantes(estudantes)
            break
    else:
        print(f'Não foi encontrado nenhum estudante com o código {codigo}.')

def salvar_estudantes(estudantes):
    with open('estudantes.json', 'w') as f:
        json.dump(estudantes, f)

def recuperar_estudantes():
    try:
        with open('estudantes.json', 'r') as f:
            estudantes = json.load(f)
    except FileNotFoundError:
        estudantes = []
    return estudantes

estudantes = recuperar_estudantes()

menu_principal(estudantes)
