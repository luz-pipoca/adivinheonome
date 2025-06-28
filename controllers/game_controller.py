import pygame
from assets.config import LARGURA, ALTURA, CORES #
from assets.strings import textos #
from assets.questions_facil import perguntas  #
from assets.questions_normal import perguntas #
from assets.questions_dificil import perguntas #
from views.tela_inicio import desenhar_tela_inicio #
from views.tela_ranking import desenhar_tela_ranking #
from views.tela_resultado import desenhar_tela_resultado #
from controllers.player_controller import criar_jogador, atualizar_nome