import pygame
from controllers.game_controller import iniciar_jogo

def abrir_tela():
    screen = pygame.display.set_mode((800, 1000))
    pygame.display.set_caption("Adivinhe o Nome")

    rodando = True
    fonte = pygame.font.SysFont("Cursive", 48)
    while rodando:
        screen.fill((255, 255, 255))
        titulo = fonte.render("Escolha a dificuldade: 1- Fácil, 2- Médio, 3- Difícil", True, (0, 0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            if event.type == pygame.KEYDOWN:
                if evento.key ==pygame.K_1:
                    iniciar_jogo("facil")
                elif evento.key == pygame.K_2:
                    iniciar_jogo("medio")
                elif evento.key == pygame.K_3:
                    iniciar_jogo("dificil")
                rodando = False
        
        pygame.display.flip()