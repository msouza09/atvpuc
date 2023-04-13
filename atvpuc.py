# Implementação da atividade concluída por Matheus Souza
# Curso: Análise e Desenvolvimento de Sistemas
# menu_principal(estudantes): função que exibe o menu principal do sistema e permite a escolha das opções. A função recebe uma lista de estudantes como parâmetro e encaminha a opção selecionada para a função correspondente.
# incluir_estudante(estudantes): função que realiza a inclusão de um novo estudante na lista de estudantes. A função solicita ao usuário o nome, código e CPF do estudante e cria um dicionário com essas informações, que é adicionado à lista de estudantes.
# listar_estudantes(estudantes): função que lista todos os estudantes cadastrados na lista de estudantes. Se não houver estudantes cadastrados, a função exibe uma mensagem informando isso.
# atualizar_estudante(estudantes): função que permite a atualização das informações de um estudante cadastrado na lista de estudantes. A função solicita ao usuário o código do estudante a ser atualizado e, em seguida, permite a atualização do nome e CPF do estudante selecionado.
# excluir_estudante(estudantes): função que permite a exclusão de um estudante da lista de estudantes. A função solicita ao usuário o código do estudante a ser excluído e, em seguida, remove o estudante da lista.
# menu_estudantes(estudantes): função que exibe o menu de operações para os estudantes e permite a escolha das opções. A função recebe uma lista de estudantes como parâmetro e encaminha a opção selecionada para a função correspondente. As opções incluem inclusão, listagem, atualização e exclusão de estudantes. A opção "0" retorna para o menu principal.

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
    cpf_estudante = str(input('\nDigite o CPF do Estudante: '))
    input('\nPressione ENTER para continuar')
    informacoes_estudante = {"codigo": cod_estudante, "nome": nome_estudante, "cpf": cpf_estudante}
    estudantes.append(informacoes_estudante)
    print('Estudante cadastrado com sucesso.')

def listar_estudantes(estudantes):
    if len(estudantes) == 0:
        print('Não há estudantes cadastrados')
    else:
        print('\n---LISTAGEM---\n')
    for estudante in estudantes:
        print(estudante)
    input('Pressione ENTER para continuar')

def atualizar_estudante(estudantes):
    print('\n==== ATUALIZAÇÃO ====\n')
    codigo = int(input('Digite o código do estudante que deseja atualizar: '))
    for estudante in estudantes:
        if estudante['codigo'] == codigo:
            nome_estudante = input('Digite o novo nome do estudante: ')
            cpf_estudante = input('Digite o novo CPF do estudante: ')
            estudante['nome'] = nome_estudante
            estudante['cpf'] = cpf_estudante
            print(f'Estudante {codigo} atualizado com sucesso!')
            break
    else:
        print(f'Não foi encontrado nenhum estudante com o código {codigo}.')

def excluir_estudante(estudantes):
    print('\n==== EXCLUSÃO ====\n')
    codigo = int(input('Digite o código do estudante que deseja excluir: '))
    for estudante in estudantes:
        if estudante['codigo'] == codigo:
            estudantes.remove(estudante)
            print(f'Estudante {codigo} excluído com sucesso!')
            break
    else:
        print(f'Não foi encontrado nenhum estudante com o código {codigo}.')

estudantes = []

menu_principal(estudantes)


