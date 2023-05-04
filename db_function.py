import json

def salvar_estudantes(estudantes):
    with open('db/estudantes.json', 'w') as file:
        json.dump(estudantes, file)
    print('Lista de estudantes salva com sucesso.')

def carregar_estudantes():
    try:
        with open('db/estudantes.json', 'r') as file:
            estudantes = json.load(file)
    except FileNotFoundError:
        estudantes = []
    return estudantes

def salvar_estudantes(estudantes):
    with open('db/estudantes.json', 'w') as f:
        json.dump(estudantes, f)

def recuperar_estudantes():
    try:
        with open('db/estudantes.json', 'r') as f:
            estudantes = json.load(f)
    except FileNotFoundError:
        estudantes = []
    return estudantes

estudantes = recuperar_estudantes()

#Professores

def salvar_professores(professores):
    with open('db/professores.json', 'w') as file:
        json.dump(professores, file)
    print('Lista de professores salva com sucesso.')

def carregar_professores():
    try:
        with open('db/professores.json', 'r') as file:
            professores = json.load(file)
    except FileNotFoundError:
        professores = []
    return professores

def salvar_professores(professores):
    with open('db/professores.json', 'w') as f:
        json.dump(professores, f)

def recuperar_professores():
    try:
        with open('db/professores.json', 'r') as f:
            professores = json.load(f)
    except FileNotFoundError:
        professores = []
    return professores

professores = recuperar_professores()

#Disciplinas

def salvar_disciplinas(disciplinas):
    with open('db/disciplinas.json', 'w') as file:
        json.dump(disciplinas, file)
    print('Lista de disciplinas salva com sucesso.')

def carregar_disciplinas():
    try:
        with open('db/disciplinas.json', 'r') as file:
            disciplinas = json.load(file)
    except FileNotFoundError:
        disciplinas = []
    return disciplinas

def salvar_disciplinas(disciplinas):
    with open('db/disciplinas.json', 'w') as f:
        json.dump(disciplinas, f)

def recuperar_disciplinas():
    try:
        with open('db/disciplinas.json', 'r') as f:
            disciplinas = json.load(f)
    except FileNotFoundError:
        disciplinas = []
    return disciplinas

disciplinas = recuperar_disciplinas()

#Turmas

def salvar_turmas(turmas):
    with open('db/turmas.json', 'w') as file:
        json.dump(turmas, file)
    print('Lista de turmas salva com sucesso.')

def carregar_turmas():
    try:
        with open('db/turmas.json', 'r') as file:
            turmas = json.load(file)
    except FileNotFoundError:
        turmas = []
    return turmas

def salvar_turmas(turmas):
    with open('db/turmas.json', 'w') as f:
        json.dump(turmas, f)

def recuperar_turmas():
    try:
        with open('db/turmas.json', 'r') as f:
            turmas = json.load(f)
    except FileNotFoundError:
        turmas = []
    return turmas

turmas = recuperar_turmas()

#Matriculas

def salvar_matriculas(matriculas):
    with open('db/matriculas.json', 'w') as file:
        json.dump(matriculas, file)
    print('Lista de matriculas salva com sucesso.')

def carregar_matriculas():
    try:
        with open('db/matriculas.json', 'r') as file:
            matriculas = json.load(file)
    except FileNotFoundError:
        matriculas = []
    return matriculas

def salvar_matriculas(matriculas):
    with open('db/matriculas.json', 'w') as f:
        json.dump(matriculas, f)

def recuperar_matriculas():
    try:
        with open('db/matriculas.json', 'r') as f:
            matriculas = json.load(f)
    except FileNotFoundError:
        matriculas = []
    return matriculas

matriculas = recuperar_matriculas()