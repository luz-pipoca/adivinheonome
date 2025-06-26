from models.jogador import jogador
from controllers.question_controller import carregar_perguntas
from views import tela_jogo, tela_resultado

def iniciar_jogo(dificuldade):
    jogador = Jogador(nome = "Jogador", dificuldade = dificuldade)
    perguntas = carregar_perguntas(dificuldade)
    tela_jogo.rodar_jogo(jogador, perguntas)
    tela_resultado.mostrar_resultado(jogador)