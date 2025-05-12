from exercicio_4 import somar_pares

def cadastrar_aluno(nome, email, serie, nota_1, nota_2, nota_3): 
    alunos = []

    notas = [nota_1, nota_2, nota_3]
    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie, 
        "media": somar_pares([nota_1, nota_2, nota_3])
    }
    alunos.append(aluno)
    
    return alunos
print(cadastrar_aluno("marina", "marinaluiza@gmail.com", "2TB", 8,9,9)) 























