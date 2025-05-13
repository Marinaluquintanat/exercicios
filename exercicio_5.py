from exercicio04 import somar_pares

alunos = []

def obter_dados_aluno():
    nome = input("digite o nome do aluno")
    email = input("digite o email do aluno")
    serie = input("qual a serie do aluno")
    nota01 = int(input("nota01"))
    nota02 = int(input("nota02"))
    nota03 = int(input("nota03"))
    return cadastrar_aluno(nome, email, serie, nota01, nota02, nota03)

def cadastrar_aluno(nome, email, serie, nota01=0, nota02=0, nota03=0):


    notas =  [nota01, nota02, nota03]

    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie,
        "media": somar_pares([nota01, nota02, nota03])
    }
    alunos.append(aluno)

    return alunos

def mostrar_dados_alunos(dados_alunos):
    for aluno in dados_alunos:
        print(f"nome do aluno: {aluno["nome"]}")
    return

def iniciar_sistema():
    while True: 
        print("="*80)
        print("opção 1 => Mostrar lista de alunos cadastrados. ")
        print("opção 2 => Cadastrar Alunos. ")
        print("opção 3 => Sair do sistema. ")
        print("="*80)

        opcao = input("Escolha uma das opções acima: ")

iniciar_sistema()






























