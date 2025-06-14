
import pygame
import pygame_gui

# inicialização do pygame
pygame.init()


#estado do jogo
#criacao de coisas que nao mudam (constantes) eu uso o padrao de tudo maiusculo

INICIO = 1
JOGANDO = 2
FINAL = 3

largura_tela = 800
altura_tela = 600
largura_snake = 40
altura_snake = 40

x_snake = largura_tela/2 - largura_snake/2
y_snake = altura_tela/2 - altura_snake/2

# criar a tela
screen = pygame.display.set_mode((largura_tela, altura_tela))


#criar gerenciador do pygame_gui
gerente = pygame_gui.UIManager((largura_tela, altura_tela))

botao_inicio = pygame_gui.elements.UIButton(
relative_rect = pygame.Rect((x_snake, y_snake), (140, 40)),
text = 'start game',
manager = gerente
)

# loop principal do jogo
running = True
estado = INICIO
while running:
    # percorrendo os eventos
    for event in pygame.event.get():
        gerente.process_events(event)
        # verificando se o evento é do tipo QUIT
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and estado == JOGANDO:
            if event.key == pygame.K_w:
                y_snake = y_snake - 10
            elif event.key == pygame.K_a:
                x_snake = x_snake - 10
            elif event.key == pygame.K_s:
                y_snake = y_snake + 10
            elif event.key == pygame.K_d:
                x_snake = x_snake + 10
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == botao_inicio:
                estado = JOGANDO
        
    #preenchimento da tela...
    
    screen.fill((0,0,0))
    if estado == JOGANDO:

        pygame.draw.rect(screen, (30, 255, 255),[(x_snake, y_snake), (largura_snake, altura_snake)])

    if estado == INICIO: 
        gerente.update(1 / 60)
        gerente.draw_ui(screen)
    #atalizacao de tela...
    pygame.display.flip()