import pygame

pygame.init()

# Estados do jogo
INICIO = 1
SELECIONAR_DIFICULDADE = 2
JOGANDO = 3
OPCOES = 4
PERDEU = 5

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

# Botões tela inicial
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

# Variáveis para temporizador e jogo
tempo_restante = 0
tempo_inicio = 0
dificuldade_atual = None

# Variáveis para pergunta do modo fácil
pergunta = "Qual o nome deste animal?"
opcoes = [
    {"texto": "Gato", "correta": False},
    {"texto": "Cachorro", "correta": True},  # a correta
    {"texto": "Coelho", "correta": False},
    {"texto": "Pássaro", "correta": False},
]
botoes_opcoes_jogo = []

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
                        dificuldade_atual = nome
                        if nome == "FÁCIL":
                            tempo_restante = 5 * 60
                            botoes_opcoes_jogo = []
                            for i, opcao in enumerate(opcoes):
                                rect_opcao = pygame.Rect(centro_x - 150, 300 + i*70, 300, 50)
                                botoes_opcoes_jogo.append((rect_opcao, opcao))
                        elif nome == "MÉDIO":
                            tempo_restante = 2 * 60
                        elif nome == "DIFÍCIL":
                            tempo_restante = 30
                        tempo_inicio = pygame.time.get_ticks()
                        estado = JOGANDO

            elif estado == OPCOES:
                for nome, rect in botoes_opcoes.items():
                    if rect.collidepoint(pos):
                        print(f"Opção selecionada: {nome}")
                        estado = INICIO

            elif estado == JOGANDO:
                if dificuldade_atual == "FÁCIL":
                    for rect, opcao in botoes_opcoes_jogo:
                        if rect.collidepoint(pos):
                            if opcao["correta"]:
                                print("Acertou!")
                                # Exemplo: poderia mudar de estado ou pontuar
                            else:
                                print("Errou!")

            elif estado == PERDEU:
                botao_menu = pygame.Rect(centro_x - 90, altura_tela // 2 + 20, 180, 50)
                if botao_menu.collidepoint(pos):
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
            pygame.draw.rect(screen, (138, 43, 226), rect)
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)
            txt_render = fonte.render(texto, True, (255, 255, 255))
            txt_rect = txt_render.get_rect(center=rect.center)
            screen.blit(txt_render, txt_rect)

    elif estado == SELECIONAR_DIFICULDADE:
        for texto, rect in botoes_dificuldade.items():
            pygame.draw.rect(screen, (50, 200, 100), rect)
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)
            txt_render = fonte.render(texto, True, (255, 255, 255))
            txt_rect = txt_render.get_rect(center=rect.center)
            screen.blit(txt_render, txt_rect)

    elif estado == OPCOES:
        for texto, rect in botoes_opcoes.items():
            pygame.draw.rect(screen, (200, 150, 50), rect)
            pygame.draw.rect(screen, (255, 255, 255), rect, 2)
            txt_render = fonte.render(texto, True, (255, 255, 255))
            txt_rect = txt_render.get_rect(center=rect.center)
            screen.blit(txt_render, txt_rect)

    elif estado == JOGANDO:
        tempo_passado_ms = pygame.time.get_ticks() - tempo_inicio
        tempo_restante_atual = max(0, tempo_restante - tempo_passado_ms // 1000)

        minutos = tempo_restante_atual // 60
        segundos = tempo_restante_atual % 60
        timer_text = f"Tempo restante: {minutos:02}:{segundos:02}"
        timer_render = fonte.render(timer_text, True, (255, 255, 255))
        screen.blit(timer_render, (centro_x - 100, 50))

        if dificuldade_atual == "FÁCIL":
            pergunta_render = fonte.render(pergunta, True, (255, 255, 255))
            pergunta_rect = pergunta_render.get_rect(center=(centro_x, 150))
            screen.blit(pergunta_render, pergunta_rect)

            for rect, opcao in botoes_opcoes_jogo:
                pygame.draw.rect(screen, (100, 100, 255), rect)
                pygame.draw.rect(screen, (255, 255, 255), rect, 2)
                txt_render = fonte.render(opcao["texto"], True, (255, 255, 255))
                txt_rect = txt_render.get_rect(center=rect.center)
                screen.blit(txt_render, txt_rect)
        else:
            txt = fonte.render("TELA DE JOGO - pressione ESC para voltar", True, (255, 255, 255))
            screen.blit(txt, (centro_x - 250, altura_tela // 2))

        if tempo_restante_atual <= 0:
            estado = PERDEU

    elif estado == PERDEU:
        perdeu_text = fonte_titulo.render("Tentar novamente", True, (255, 0, 0))
        perdeu_rect = perdeu_text.get_rect(center=(centro_x, altura_tela // 2 - 50))
        screen.blit(perdeu_text, perdeu_rect)

        botao_menu = pygame.Rect(centro_x - 90, altura_tela // 2 + 20, 180, 50)
        pygame.draw.rect(screen, (0, 0, 255), botao_menu)
        pygame.draw.rect(screen, (255, 255, 255), botao_menu, 2)
        txt_render = fonte.render("MENU", True, (255, 255, 255))
        txt_rect = txt_render.get_rect(center=botao_menu.center)
        screen.blit(txt_render, txt_rect)

    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        estado = INICIO

pygame.quit()
