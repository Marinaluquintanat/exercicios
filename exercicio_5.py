def cadastrar_aluno(nome, email, serie, nota_1, nota_2, nota_3): 
    alunos = []

    aluno = {
        "nome": nome,
        "email": email,
        "serie": serie, 
        "notas": [nota_1, nota_2, nota_3]
    }
    alunos.append(aluno)
    return alunos 














