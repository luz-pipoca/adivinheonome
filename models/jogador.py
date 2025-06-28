class Jogador:
    def __init__(self, nome, dificuldade):
        self.nome = nome
        self.dificuldade = dificuldade
        self.pontuacao = 0
        self.vidas = {"facil": 4, "normal": 3, "dificil": 1} [dificuldade]
        self.tempo = {"facil": 30, "normal": 20, "dificil": 10} [dificuldade]

    def remover_vida(self):
        self.vidas -= 1

    def adicionar_letra(self, letra):
        self.letras_adivinhadas.append(letra)

    def adicionar_pontuacao(self):
        pontos = {"facil": 10, "normal": 20, "dificil": 35} [self.dificuldade]
        self.pontuacao += pontos

    def registrar_acerto(self):
        self.acertos_seguidos += 1
        self.erros_consecutivos = 0

    def registrar_erro(self):
        self.erros_consecutivos += 1
        self.acertos_seguidos = 0

    def verificar_letra_na_palavra(self, letra, palavra):
        if letra in palavra.upper():
            self.adicionar_letra(letra)
            self.registrar_acerto()
            self.adicionar_pontuacao()
            return True
        else:
            self.remover_vida()
            self.registrar_erro()
            return False