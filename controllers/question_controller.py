import random
def carregar_perguntas(difiuldade):
    if dificuldade == "facil":
        arquivo = "questions_facil.py"
    elif dificuldade == "normal":
        arquivo = "questions_normal.py"
    else:
        arquivo = "questions_dificil.py"
        from importlib import import_module
        perguntas = import_module(arquivo.replace(".py", ""))
        random.shuffle(perguntas.QUESTOES)
        return perguntas.QUESTOES