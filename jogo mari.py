import pygame_gui
import pygame
from pygame_gui.core import ObjectID

pygame.init()

INICIO = 1
 
DIFICULDADE =  2

# aqui temos a configuraçao de tela do jogo.

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Botão Personalizado")

#aqui temos a modificaçao do botao

gerente = pygame_gui.UIManager((1000, 800), "theme.json")

botao_personalizado = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((410, 280), (180, 50)),
    text = 'JOGAR',
    manager = gerente,
    object_id = "#botao_personalizado"
)

botao_personalizado = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((410, 380), (180, 50)),
    text ='DIFICULDADE',
    manager = gerente,
    object_id ="#botao_personalizado"
)

botao_personalizado = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((410, 480), (180, 50)),
    text ='OPÇOES',
    manager = gerente,
    object_id ="#botao_personalizado"
)

running = True
estado = INICIO
while running:

    # percorrendo os eventos

    for event in pygame.event.get():
        gerente.process_events(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == botao_personalizado:
                estado = DIFICULDADE
    if estado == INICIO: 
        gerente.update(1 / 60)
        gerente.draw_ui(screen)
    pygame.display.flip()
 #preenchimento da tela com as imagens
    
'''   screen.fill((0,0,0))
    if estado == JOGANDO:

        pygame.draw.rect(screen)

    if estado == INICIO: 
        gerente.update(1 / 60)
        gerente.draw_ui(screen)
    #atalizacao de tela...
    pygame.display.flip()

'''