class Jogador:
    def __init__(self, nome, dificuldade):
        self.nome = nome
        self.dificuldade = dificuldade
        self.pontuacao = 0
        self.vidas = {"facil": 4, "normal": 3, "dificil": 1} [dificuldade]
        self.tempo = {"facil": 30, "normal": 20, "dificil": 10} [dificuldade]

    def perder_vida(self):
        self.vidas -= 1

    def adicionar_pontuacao(self):
        pontos = {"facil": 10, "normal": 20, "dificil": 35} [self.dificuldade]
        self.pontuacao += pontos