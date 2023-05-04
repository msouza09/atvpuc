# Implementação da atividade concluída por Matheus Souza
# Curso: Análise e Desenvolvimento de Sistemas
# salvar_estudantes(estudantes): recebe uma lista de dicionários com informações de estudantes e as salva em um arquivo JSON chamado 
# "estudantes.json". Se a operação for bem-sucedida, a mensagem "Lista de estudantes salva com sucesso." é impressa.
# carregar_estudantes(): tenta abrir o arquivo "estudantes.json" e carregar as informações de estudantes. Se o arquivo não existir, retorna 
# uma lista vazia.
# menu_principal(estudantes): apresenta ao usuário um menu principal com opções para gerenciar estudantes, disciplinas, professores, turmas e 
# matrículas. A função entra em um loop infinito até que o usuário escolha a opção "0" para sair. Dependendo da opção escolhida, a função chama 
# outras funções para gerenciar estudantes ou exibe uma mensagem de "EM DESENVOLVIMENTO".
# menu_estudantes(estudantes): apresenta ao usuário um menu com opções para gerenciar estudantes, como incluir, listar, atualizar e excluir 
# estudantes. A função entra em um loop infinito até que o usuário escolha a opção "0" para voltar ao menu principal. Dependendo da opção 
# escolhida, a função chama outras funções para realizar as operações de gerenciamento.
# incluir_estudante(estudantes): solicita informações do usuário para incluir um novo estudante na lista. Se o código do estudante já existir 
# na lista, uma mensagem de erro é exibida. Caso contrário, as informações são adicionadas à lista de estudantes e salvas no arquivo JSON.
# listar_estudantes(estudantes): exibe uma lista com todas as informações de estudantes na lista.
# atualizar_estudante(estudantes): solicita ao usuário o código do estudante que deseja atualizar e, em seguida, solicita as novas informações 
# do estudante. Se o novo código já existir na lista e não pertencer ao mesmo estudante que está sendo atualizado, uma mensagem de erro é 
# exibida. Caso contrário, as informações do estudante são atualizadas na lista de estudantes e salvas no arquivo JSON.
# excluir_estudante(estudantes): solicita ao usuário o código do estudante que deseja excluir e remove as informações do estudante da lista de 
# estudantes. As informações atualizadas são salvas no arquivo JSON. Se o código do estudante não existir na lista, uma mensagem de erro é 
# exibida
# Funções atualizadas, o main.py é o arquivo principal para execução.

from db_function import *
from menu import *

# estudantes = carregar_estudantes()
# professores = carregar_professores()
# disciplinas = carregar_disciplinas()
# turmas = carregar_turmas()
# matriculas = carregar_matriculas()

menu_principal(estudantes, professores, disciplinas, turmas, matriculas)