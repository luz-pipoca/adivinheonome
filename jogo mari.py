import pygame

pygame.init()

# Estados do jogo
INICIO = 1
SELECIONAR_DIFICULDADE = 2
JOGANDO = 3
OPCOES = 4

largura_tela = 1000
altura_tela = 700
screen = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Botão Personalizado")
fonte = pygame.font.SysFont(None, 36)
fonte_titulo = pygame.font.SysFont(None, 72)

centro_x = largura_tela // 2

# Carrega imagem de fundo
try:
    fundo = pygame.image.load("fundo_menu.jpg").convert()
    fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))
except pygame.error:
    print("Não foi possível carregar fundo_menu.jpg, usando fundo preto.")
    fundo = None

# Botões tela inicial (reposicionados)
botoes_inicio = {
    "JOGAR": pygame.Rect(centro_x - 90, 250, 180, 50),
    "OPÇÕES": pygame.Rect(centro_x - 90, 350, 180, 50),
    "SAIR": pygame.Rect(centro_x - 90, 450, 180, 50),
}

# Botões tela de seleção de dificuldade
botoes_dificuldade = {
    "FÁCIL": pygame.Rect(centro_x - 90, 250, 180, 50),
    "MÉDIO": pygame.Rect(centro_x - 90, 350, 180, 50),
    "DIFÍCIL": pygame.Rect(centro_x - 90, 450, 180, 50)
}

# Botões tela de opções
botoes_opcoes = {
    "IDIOMA": pygame.Rect(centro_x - 90, 250, 180, 50),
    "TAMANHO DA TELA": pygame.Rect(centro_x - 125, 350, 250, 50)
}

clock = pygame.time.Clock()
running = True
estado = INICIO

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()

            if estado == INICIO:
                for nome, rect in botoes_inicio.items():
                    if rect.collidepoint(pos):
                        if nome == "JOGAR":
                            estado = SELECIONAR_DIFICULDADE
                        elif nome == "OPÇÕES":
                            estado = OPCOES
                        elif nome == "SAIR":
                            running = False

            elif estado == SELECIONAR_DIFICULDADE:
                for nome, rect in botoes_dificuldade.items():
                    if rect.collidepoint(pos):
                        print(f"Dificuldade selecionada: {nome}")
                        estado = JOGANDO

            elif estado == OPCOES:
                for nome, rect in botoes_opcoes.items():
                    if rect.collidepoint(pos):
                        print(f"Opção selecionada: {nome}")
                        estado = INICIO

    # Desenha o fundo (imagem ou preto se não carregou)
    if fundo:
        screen.blit(fundo, (0, 0))
    else:
        screen.fill((0, 0, 0))

    if estado == INICIO:
        titulo_render = fonte_titulo.render("ADIVINHE O NOME", True, (255, 255, 255))
        titulo_rect = titulo_render.get_rect(center=(centro_x, 120))
        screen.blit(titulo_render, titulo_rect)

        for texto, rect in botoes_inicio.items():
            pygame.draw.rect(screen, (138, 43, 226), rect)  # roxo
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)
            txt_render = fonte.render(texto, True, (255, 255, 255))
            txt_rect = txt_render.get_rect(center=rect.center)
            screen.blit(txt_render, txt_rect)

    elif estado == SELECIONAR_DIFICULDADE:
        for texto, rect in botoes_dificuldade.items():
            pygame.draw.rect(screen, (50, 200, 100), rect)  # verde
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)
            txt_render = fonte.render(texto, True, (255, 255, 255))
            txt_rect = txt_render.get_rect(center=rect.center)
            screen.blit(txt_render, txt_rect)

    elif estado == OPCOES:
        for texto, rect in botoes_opcoes.items():
            pygame.draw.rect(screen, (200, 150, 50), rect)  # laranja
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)
            txt_render = fonte.render(texto, True, (255, 255, 255))
            txt_rect = txt_render.get_rect(center=rect.center)
            screen.blit(txt_render, txt_rect)

    elif estado == JOGANDO:
        txt = fonte.render("TELA DE JOGO - pressione ESC para voltar", True, (255, 255, 255))
        screen.blit(txt, (centro_x - 250, altura_tela // 2))

    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        estado = INICIO

pygame.quit()
