import pygame
from assets.questions_facil import perguntas
from assets.questions_normal import perguntas
from assets.questions_dificil import perguntas

pygame.init()

# Estados do jogo
INICIO = 1
SELECIONAR_DIFICULDADE = 2
JOGANDO = 3
OPCOES = 4
PERDEU = 5
GANHOU = 6

largura_tela = 1000
altura_tela = 700
screen = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Botão Personalizado")
fonte = pygame.font.SysFont(None, 36)
fonte_titulo = pygame.font.SysFont(None, 72)

centro_x = largura_tela // 2

# Carrega imagens de fundo
try:
    fundo = pygame.image.load("assets/img/interface_jogo/fundo_menu.png").convert()
    fundo = pygame.transform.scale(fundo, (largura_tela, altura_tela))
except pygame.error:
    print("Não foi possível carregar fundo_menu.png, usando fundo preto.")
    fundo = None

try:
    fundo_dificuldade = pygame.image.load("assets/img/interface_jogo/fundo_escolha_dificuldade.png").convert()
    fundo_dificuldade = pygame.transform.scale(fundo_dificuldade, (largura_tela, altura_tela))
except pygame.error:
    print("Não foi possível carregar fundo_dificuldade.png, usando fundo preto.")
    fundo_dificuldade = None

try:
    fundo_facil = pygame.image.load("assets/img/interface_jogo/fundo_nivel_facil.png").convert()
    fundo_facil = pygame.transform.scale(fundo_facil, (largura_tela, altura_tela))
except pygame.error:
    print("Não foi possível carregar fundo_facil.png, usando fundo preto.")
    fundo_facil = None

try:
    fundo_medio = pygame.image.load("assets/img/interface_jogo/fundo_nivel_normal.png").convert()
    fundo_medio = pygame.transform.scale(fundo_medio, (largura_tela, altura_tela))
except pygame.error:
    print("Não foi possível carregar fundo_medio.png, usando fundo preto.")
    fundo_medio = None

try:
    fundo_dificil = pygame.image.load("assets/img/interface_jogo/fundo_nivel_dificil.png").convert()
    fundo_dificil = pygame.transform.scale(fundo_dificil, (largura_tela, altura_tela))
except pygame.error:
    print("Não foi possível carregar fundo_dificil.png, usando fundo preto.")
    fundo_dificil = None

# Botões
botoes_inicio = {
    "JOGAR": pygame.Rect(centro_x - 100, 325, 180, 50),
    "OPÇÕES": pygame.Rect(centro_x - 100, 400, 180, 50),
    "SAIR": pygame.Rect(centro_x - 100, 475, 180, 50),
}
botoes_dificuldade = {
    "FÁCIL": pygame.Rect(centro_x - 80, 325, 130, 50),
    "NORMAL": pygame.Rect(centro_x - 80, 400, 130, 50),
    "DIFÍCIL": pygame.Rect(centro_x - 80, 475, 130, 50),
}
botoes_opcoes = {
    "IDIOMA": pygame.Rect(centro_x - 90, 250, 180, 50),
    "TAMANHO DA TELA": pygame.Rect(centro_x - 125, 350, 250, 50),
}

clock = pygame.time.Clock()
running = True
estado = INICIO

tempo_restante = 0
tempo_inicio = 0
dificuldade_atual = None
pontuacao = 0

pergunta = ""
opcoes = []
botoes_opcoes_jogo = []

def carregar_proxima_pergunta():
    global pergunta, opcoes, botoes_opcoes_jogo
    pergunta = "Qual o nome deste animal?"
    opcoes = [
        {"texto": "Gato", "correta": False},
        {"texto": "Cachorro", "correta": True},
        {"texto": "Coelho", "correta": False},
        {"texto": "Pássaro", "correta": False},
    ]
    botoes_opcoes_jogo = []
    for i, opcao in enumerate(opcoes):
        rect_opcao = pygame.Rect(centro_x - 150, 300 + i*70, 300, 50)
        botoes_opcoes_jogo.append((rect_opcao, opcao))

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
                            carregar_proxima_pergunta()
                        elif nome == "NORMAL":
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
                                pontuacao += 10
                                estado = GANHOU
                            else:
                                print("Errou!")

            elif estado == PERDEU:
                botao_menu = pygame.Rect(centro_x - 90, altura_tela // 2 + 20, 180, 50)
                if botao_menu.collidepoint(pos):
                    estado = INICIO

    # Desenha fundo
    if estado == INICIO:
        if fundo:
            screen.blit(fundo, (0, 0))
        else:
            screen.fill((0, 0, 0))
    elif estado == SELECIONAR_DIFICULDADE:
        if fundo_dificuldade:
            screen.blit(fundo_dificuldade, (0, 0))
        else:
            screen.fill((0, 0, 0))
    elif estado == JOGANDO:
        if dificuldade_atual == "FÁCIL" and fundo_facil:
            screen.blit(fundo_facil, (0, 0))
        elif dificuldade_atual == "NORMAL" and fundo_medio:
            screen.blit(fundo_medio, (0, 0))
        elif dificuldade_atual == "DIFÍCIL" and fundo_dificil:
            screen.blit(fundo_dificil, (0, 0))
        else:
            screen.fill((0, 0, 0))
    else:
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

        pontuacao_text = f"Pontos: {pontuacao}"
        pontuacao_render = fonte.render(pontuacao_text, True, (255, 255, 255))
        pontuacao_rect = pontuacao_render.get_rect(topright=(largura_tela - 20, 20))
        screen.blit(pontuacao_render, pontuacao_rect)

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

        if tempo_restante_atual <= 0:
            estado = PERDEU

    elif estado == GANHOU:
        screen.fill((0, 0, 0))
        ganhou_text = fonte_titulo.render("Você Ganhou!", True, (0, 255, 0))
        ganhou_rect = ganhou_text.get_rect(center=(centro_x, altura_tela // 2 - 50))
        screen.blit(ganhou_text, ganhou_rect)

        instrucao_text = fonte.render("APERTE ESC PARA VOLTAR", True, (255, 255, 255))
        instrucao_rect = instrucao_text.get_rect(center=(centro_x, altura_tela // 2 + 50))
        screen.blit(instrucao_text, instrucao_rect)

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
