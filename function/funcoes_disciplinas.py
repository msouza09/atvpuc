from db_function import *
import time

def incluir_disciplina(disciplinas):
    print('\n==== INCLUSÃO ====\n')
    cod_disciplina = int(input('\nCódigo da disciplina: '))
    nome_disciplina = str(input('Digite o nome da disciplina: '))
    input('\nPressione ENTER para continuar ')
    print('Incluindo usuário, aguarde...')
    time.sleep(1)

    for disciplina in disciplinas:
        if disciplina['codigo'] == cod_disciplina:
            print('Erro: código já existente!')
            return

    informacoes_disciplina = {"codigo": cod_disciplina, "nome": nome_disciplina}

    disciplinas.append(informacoes_disciplina)

    salvar_disciplinas(disciplinas)

    print('Disciplina cadastrado com sucesso.')

def listar_disciplinas(disciplinas):
    print('Coletando Informações, aguarde...')
    time.sleep(2)
    if len(disciplinas) == 0:
        print('Não há disciplinas cadastrados')
    else:
        print('\n---LISTAGEM---\n')
        for disciplina in disciplinas:
            print(disciplina)
        input('Pressione ENTER para continuar ')
        
def atualizar_disciplina(disciplinas):
    print('\n==== ATUALIZAÇÃO ====\n')
    codigo = int(input('Digite o código do disciplina que deseja atualizar: '))

    for disciplina in disciplinas:
        if disciplina['codigo'] == codigo:
            nome_disciplina = str(input('Digite o novo nome do disciplina: '))

            if nome_disciplina and novo_codigo:
                novo_codigo = int(input('Digite o novo código do disciplina: '))
                print('Atualizando dados do usuário, aguarde...')
                time.sleep(2)
                for outro_disciplina in disciplinas:
                    if outro_disciplina['codigo'] == novo_codigo and outro_disciplina != disciplina:
                        print('Erro: código já existente!')
                        return

                disciplina['nome'] = nome_disciplina
                disciplina['codigo'] = novo_codigo
                

                print(f'disciplina {codigo} atualizado com sucesso!')
                salvar_disciplinas(disciplinas)
                break
            else:
                print('Erro: todos os campos devem ser preenchidos!')
                return
    else:
        print(f'Não foi encontrado nenhum disciplina com o código {codigo}.')

def excluir_disciplina(disciplinas):
    print('\n==== EXCLUSÃO ====\n')
    codigo = int(input('Digite o código do disciplina que deseja excluir: '))
    for disciplina in disciplinas:
        if disciplina['codigo'] == codigo:
            disciplinas.remove(disciplina)
            input(f'Você deseja excluir a disciplina {disciplina}? Para confirmar aperte ENTER. ')
            print('Excluindo disciplina, aguarde...')
            time.sleep(2)
            print(f'disciplina {codigo} excluído com sucesso!')
            salvar_disciplinas(disciplinas)
            break
    else:
        print(f'Não foi encontrado nenhuma disciplina com o código {codigo}.')