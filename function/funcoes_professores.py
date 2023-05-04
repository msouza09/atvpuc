from db_function import *
import time

def incluir_professor(professores):
    print('\n==== INCLUSÃO ====\n')
    cod_professor = int(input('\nCódigo do professor: '))
    nome_professor = str(input('Digite o nome do professor: '))
    cpf_professor = str(input('\nDigite o CPF do professor: '))
    input('\nPressione ENTER para continuar ')
    print('Incluindo usuário, aguarde...')
    time.sleep(1)

    for professor in professores:
        if professor['codigo'] == cod_professor:
            print('Erro: Código já existente!')
            return

    informacoes_professor = {"codigo": cod_professor, "nome": nome_professor, "cpf": cpf_professor}

    professores.append(informacoes_professor)

    salvar_professores(professores)

    print('Professor cadastrado com sucesso.')

def listar_professores(professores):
    print('Coletando Informações, aguarde...')
    time.sleep(2)
    if len(professores) == 0:
        print('Não há professores cadastrados')
    else:
        print('\n---LISTAGEM---\n')
        for professor in professores:
            print(professor)
        input('Pressione ENTER para continuar ')
        
def atualizar_professor(professores):
    print('\n==== ATUALIZAÇÃO ====\n')
    codigo = int(input('Digite o código do professor que deseja atualizar: '))

    for professor in professores:
        if professor['codigo'] == codigo:
            nome_professor = str(input('Digite o novo nome do professor: '))
            cpf_professor = str(input('Digite o novo CPF do professor: '))

            if nome_professor and cpf_professor:
                novo_codigo = int(input('Digite o novo código do professor: '))
                print('Atualizando dados do usuário, aguarde...')
                time.sleep(2)
                for outro_professor in professores:
                    if outro_professor['codigo'] == novo_codigo and outro_professor != professor:
                        print('Erro: código já existente!')
                        return

                professor['nome'] = nome_professor
                professor['cpf'] = cpf_professor
                professor['codigo'] = novo_codigo
                

                print(f'Professor {codigo} atualizado com sucesso!')
                salvar_professores(professores)
                break
            else:
                print('Erro: Todos os campos devem ser preenchidos!')
                return
    else:
        print(f'Não foi encontrado nenhum professor com o código {codigo}.')

def excluir_professor(professores):
    print('\n==== EXCLUSÃO ====\n')
    codigo = int(input('Digite o código do professor que deseja excluir: '))
    for professor in professores:
        if professor['codigo'] == codigo:
            professores.remove(professor)
            input(f'Você deseja excluir o professor {professor}? Para confirmar aperte ENTER. ')
            print('Excluindo professor, aguarde...')
            time.sleep(2)
            print(f'professor {codigo} excluído com sucesso!')
            salvar_professores(professores)
            break
    else:
        print(f'Não foi encontrado nenhum professor com o código {codigo}.')