def cadastrar_filme(nome, classificacao, descricao, categoria_1, categoria_2, categoria_3):
    filmes = []
    filme = {
        "nome": nome, 
        "classificacao": classificacao,
        "descricao": descricao,
        "categorias": [categoria_1, categoria_2, categoria_3]

    }
    filmes.append(filme)
    return filmes
print(cadastrar_filme("mariflix", 16, "filmes e séries para toda a familia", "romance", "comedia", "terror"))





















