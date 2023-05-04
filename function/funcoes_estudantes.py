from db_function import *
import time

def incluir_estudante(estudantes):
    print('\n==== INCLUSÃO ====\n')
    nome_estudante = input('Digite o nome do estudante: ')
    cod_estudante = int(input('\nCódigo do Estudante: '))
    cpf_estudante = str(input('\nDigite o CPF do Estudante: '))
    input('\nPressione ENTER para continuar ')
    print('Incluindo usuário, aguarde...')
    time.sleep(1)

    for estudante in estudantes:
        if estudante['codigo'] == cod_estudante:
            print('Erro: Código já existente!')
            return

    informacoes_estudante = {"codigo": cod_estudante, "nome": nome_estudante, "cpf": cpf_estudante}

    estudantes.append(informacoes_estudante)

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

    for estudante in estudantes:
        if estudante['codigo'] == codigo:
            nome_estudante = input('Digite o novo nome do estudante: ')
            cpf_estudante = input('Digite o novo CPF do estudante: ')

            if nome_estudante and cpf_estudante:
                novo_codigo = int(input('Digite o novo código do estudante: '))
                print('Atualizando dados do usuário, aguarde...')
                time.sleep(2)
                for outro_estudante in estudantes:
                    if outro_estudante['codigo'] == novo_codigo and outro_estudante != estudante:
                        print('Erro: código já existente!')
                        return

                estudante['nome'] = nome_estudante
                estudante['cpf'] = cpf_estudante
                estudante['codigo'] = novo_codigo
                

                print(f'Estudante {codigo} atualizado com sucesso!')
                salvar_estudantes(estudantes)
                break
            else:
                print('Erro: Todos os campos devem ser preenchidos!')
                return
    else:
        print(f'Não foi encontrado nenhum estudante com o código {codigo}.')

def excluir_estudante(estudantes):
    print('\n==== EXCLUSÃO ====\n')
    codigo = int(input('Digite o código do estudante que deseja excluir: '))
    for estudante in estudantes:
        if estudante['codigo'] == codigo:
            estudantes.remove(estudante)
            input(f'Você deseja excluir o estudante {estudante}? Para confirmar aperte ENTER. ')
            print('Excluindo Estudante, aguarde...')
            time.sleep(2)
            print(f'Estudante {codigo} excluído com sucesso!')
            salvar_estudantes(estudantes)
            break
    else:
        print(f'Não foi encontrado nenhum estudante com o código {codigo}.')