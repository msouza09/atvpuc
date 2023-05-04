from db_function import *
import time

def incluir_matricula(matriculas):
    print('\n==== INCLUSÃO ====\n')
    cod_matricula = int(input('\nCódigo da matricula: '))
    nome_matricula = input('Digite o nome da matricula: ')
    input('\nPressione ENTER para continuar ')
    print('Incluindo usuário, aguarde...')
    time.sleep(1)

    for matricula in matriculas:
        if matricula['codigo'] == cod_matricula:
            print('Erro: Código já existente!')
            return

    informacoes_matricula = {"codigo": cod_matricula, "nome": nome_matricula}

    matriculas.append(informacoes_matricula)

    salvar_matriculas(matriculas)

    print('Matricula cadastrado com sucesso.')

def listar_matriculas(matriculas):
    print('Coletando Informações, aguarde...')
    time.sleep(2)
    if len(matriculas) == 0:
        print('Não há matriculas cadastrados')
    else:
        print('\n---LISTAGEM---\n')
        for matricula in matriculas:
            print(matricula)
        input('Pressione ENTER para continuar ')
        
def atualizar_matricula(matriculas):
    print('\n==== ATUALIZAÇÃO ====\n')
    codigo = int(input('Digite o código da matricula que deseja atualizar: '))

    for matricula in matriculas:
        if matricula['codigo'] == codigo:
            nome_matricula = input('Digite o novo nome da matricula: ')

            if nome_matricula and novo_codigo:
                novo_codigo = int(input('Digite o novo código da matricula: '))
                print('Atualizando dados do usuário, aguarde...')
                time.sleep(2)
                for outro_matricula in matriculas:
                    if outro_matricula['codigo'] == novo_codigo and outro_matricula != matricula:
                        print('Erro: código já existente!')
                        return

                matricula['nome'] = nome_matricula
                matricula['codigo'] = novo_codigo
                

                print(f'Matricula {codigo} atualizado com sucesso!')
                salvar_matriculas(matriculas)
                break
            else:
                print('Erro: Todos os campos devem ser preenchidos!')
                return
    else:
        print(f'Não foi encontrado nenhuma matricula com o código {codigo}.')

def excluir_matricula(matriculas):
    print('\n==== EXCLUSÃO ====\n')
    codigo = int(input('Digite o código da matricula que deseja excluir: '))
    for matricula in matriculas:
        if matricula['codigo'] == codigo:
            matriculas.remove(matricula)
            input(f'Você deseja excluir a matricula {matricula}? Para confirmar aperte ENTER. ')
            print('Excluindo a matricula, aguarde...')
            time.sleep(2)
            print(f'Matricula {codigo} excluído com sucesso!')
            salvar_matriculas(matriculas)
            break
    else:
        print(f'Não foi encontrado nenhuma matricula com o código {codigo}.')