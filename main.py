import pygame
from controllers.game_controller import GameController

def main():
    pygame.init()
    tela = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Adivinhe o Nome")

    jogo = GameController(tela)
    jogo.executar()

    pygame.quit()

if __name__ == "__main__":
    main()
