from db_function import *
import time

def incluir_turma(turmas):
    print('\n==== INCLUSÃO ====\n')
    cod_turma = int(input('\nCódigo da turma: '))
    cod_professor = int(input('Código do professor: '))
    cpf_disciplina= str(input('\nCódigo da disciplina: '))
    input('\nPressione ENTER para continuar ')
    print('Incluindo usuário, aguarde...')
    time.sleep(1)

    for turma in turmas:
        if turma['codigo'] == cod_turma:
            print('Erro: Código já existente!')
            return

    informacoes_turma = {"turma": cod_turma, "professor": cod_professor, "disciplina": cpf_disciplina}

    turmas.append(informacoes_turma)

    salvar_turmas(turmas)

    print('Turma cadastrado com sucesso.')

def listar_turmas(turmas):
    print('Coletando Informações, aguarde...')
    time.sleep(2)
    if len(turmas) == 0:
        print('Não há turmas cadastrados')
    else:
        print('\n---LISTAGEM---\n')
        for turma in turmas:
            print(turma)
        input('Pressione ENTER para continuar ')
        
def atualizar_turma(turmas):
    print('\n==== ATUALIZAÇÃO ====\n')
    codigo = int(input('Digite o código da turma que deseja atualizar: '))

    for turma in turmas:
        if turma['codigo'] == codigo:
            novo_professor = int(input('Digite o novo código do Professor: '))
            novo_disciplina = int(input('Digite o novo código da Disciplina: '))

            if novo_professor and novo_disciplina:
                novo_codigo = int(input('Digite o novo código da turma: '))
                print('Atualizando dados do usuário, aguarde...')
                time.sleep(2)
                for outro_turma in turmas:
                    if outro_turma['codigo'] == novo_codigo and outro_turma != turma:
                        print('Erro: Código já existente!')
                        return

                turma['professor'] = novo_professor
                turma['disciplina'] = novo_disciplina
                turma['codigo'] = novo_codigo
                

                print(f'Turma {codigo} atualizado com sucesso!')
                salvar_turmas(turmas)
                break
            else:
                print('Erro: Todos os campos devem ser preenchidos!')
                return
    else:
        print(f'Não foi encontrado nenhuma turma com o código {codigo}.')

def excluir_turma(turmas):
    print('\n==== EXCLUSÃO ====\n')
    codigo = int(input('Digite o código da turma que deseja excluir: '))
    for turma in turmas:
        if turma['codigo'] == codigo:
            turmas.remove(turma)
            input(f'Você deseja excluir a turma {turma}? Para confirmar aperte ENTER. ')
            print('Excluindo turma, aguarde...')
            time.sleep(2)
            print(f'Turma {codigo} excluído com sucesso!')
            salvar_turmas(turmas)
            break
    else:
        print(f'Não foi encontrado nenhuma turma com o código {codigo}.')