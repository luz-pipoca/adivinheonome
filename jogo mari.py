import pygame
import random

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
pygame.display.set_caption("ADIVINHE O NOME")
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

# Perguntas para o modo Fácil
perguntas_facil = [
    {"pergunta": "Sabe o nome desse fenômeno?", "resposta": "Arco-íris"},
    {"pergunta": "Podemos comer salgado ou doce. É a...?", "resposta": "Tapioca"},
    {"pergunta": "Sabe qual o nome deste instrumento?", "resposta": "Pandeiro"},
    {"pergunta": "É uma planta com espinhos, e é...?", "resposta": "Cacto"},
    {"pergunta": "É vermelha e suculenta, é uma...?", "resposta": "Maçã"},
    {"pergunta": "É importante para nosso corpo esse...?", "resposta": "Coração"},
    {"pergunta": "Qual o nome dessa coisa que fazemos pulseiras?", "resposta": "Miçanga"},
    {"pergunta": "Ficamos um tempo juntando peças, é um...?", "resposta": "Quebra-cabeça"},
    {"pergunta": "Ouvimos música com ele, é um...?", "resposta": "Fone de ouvido"},
    {"pergunta": "Muito gosto, ainda mais com adicional, é um...?", "resposta": "Açaí"},
    {"pergunta": "Assistimos seriados, filmes, jornais...?", "resposta": "Televisão"},
    {"pergunta": "Usamos para cozinhar, é um...?", "resposta": "Fogão"},
    {"pergunta": "Nos locomovemos com ele, é público; é um...?", "resposta": "Ônibus"},
    {"pergunta": "Dormimos, sonhamos, babamos, é uma...?", "resposta": "Cama"},
    {"pergunta": "Quase todo brasileiro gosta de comer, é um...?", "resposta": "Feijão"},
    {"pergunta": "Uma roupa quentinha, que usamos no frio, é um...?", "resposta": "Moletom"},
    {"pergunta": "Pessoas compromissadas usam um...?", "resposta": "Anel"},
    {"pergunta": "Serve para tampar a luz do quarto, é uma...?", "resposta": "Cortina"},
    {"pergunta": "Abre essa...?", "resposta": "Porta"},
    {"pergunta": "Quase todo aniversário tem, é um...?", "resposta": "Bolo"},
]

# Perguntas para o modo Difícil
perguntas_dificil = [
    {"pergunta": "É linda e cheira bem essa...?", "resposta": "Orquídea"},
    {"pergunta": "É um tipo de salamandra, é um...?", "resposta": "Axolote"},
    {"pergunta": "Podemos ver coisas pequenas com esse...?", "resposta": "Telescópio"},
    {"pergunta": "Perry o...?", "resposta": "Ornitorrinco"},
    {"pergunta": "Iguaria típica do México, o...?", "resposta": "Guacamole"},
    {"pergunta": "Para colocar as velas usamos...?", "resposta": "Candelabro"},
    {"pergunta": "Tira o pó...?", "resposta": "Aspirador de pó"},
    {"pergunta": "Uma colher grande com furos...?", "resposta": "Escumadeira"},
    {"pergunta": "Especiaria e tempero...?", "resposta": "Açafrão"},
    {"pergunta": "Te protege da chuva...?", "resposta": "Capa de chuva"},
    {"pergunta": "Qual ferramenta aperta ou solta parafusos?", "resposta": "Chave de fenda"},
    {"pergunta": "Padrão de tecnologia sem fio, seu nome...?", "resposta": "Bluetooth"},
    {"pergunta": "Guardam seus bebês na bolsinha...?", "resposta": "Canguru"},
    {"pergunta": "Bico grande, colorido e achatado lateralmente, é...?", "resposta": "Tucano"},
    {"pergunta": "Uma grande caixa recipiente, usada para entulhos...?", "resposta": "Caçamba"},
    {"pergunta": "São instrumentos parecidos com os telescópios...", "resposta": "Binóculo"},
    {"pergunta": "Coloca suas roupas, e depois no guarda-roupa...?", "resposta": "Cabide"},
    {"pergunta": "É um mini bolo! É um...?", "resposta": "Cupcake"},
    {"pergunta": "Pode mudar de cor para se esconder, é um...?", "resposta": "Camaleão"},
    {"pergunta": "É um jogo de tabuleiro estratégico, é um...?", "resposta": "Xadrez"},
    {"pergunta": "É uma pequena luminária, é um...?", "resposta": "Abajur"},
    {"pergunta": "Serve para colocar brilho em quase tudo...?", "resposta": "Glitter"},
    {"pergunta": "Pequenina, vermelhinha, bonitinha essa...?", "resposta": "Joaninha"},
    {"pergunta": "É vermelha, suculenta, dá um bom suco!", "resposta": "Acerola"},
    {"pergunta": "Acaba deixando sua comida rosa;...?", "resposta": "Beterraba"},
]

def carregar_proxima_pergunta():
    global pergunta, opcoes, botoes_opcoes_jogo
    botoes_opcoes_jogo = []

    if dificuldade_atual == "FÁCIL":
        pergunta_escolhida = random.choice(perguntas_facil)
    elif dificuldade_atual == "DIFÍCIL":
        pergunta_escolhida = random.choice(perguntas_dificil)
    else:
        pergunta_escolhida = {"pergunta": "Modo não implementado.", "resposta": "Erro"}

    pergunta = pergunta_escolhida["pergunta"]
    resposta_correta = pergunta_escolhida["resposta"]

    if dificuldade_atual == "FÁCIL":
        pool = [p["resposta"] for p in perguntas_facil if p["resposta"] != resposta_correta]
    elif dificuldade_atual == "DIFÍCIL":
        pool = [p["resposta"] for p in perguntas_dificil if p["resposta"] != resposta_correta]
    else:
        pool = []

    opcoes_incorretas = random.sample(pool, min(3, len(pool)))
    todas_opcoes = opcoes_incorretas + [resposta_correta]
    random.shuffle(todas_opcoes)

    opcoes = []
    for texto in todas_opcoes:
        correta = texto == resposta_correta
        opcoes.append({"texto": texto, "correta": correta})

    for i, opcao in enumerate(opcoes):
        rect_opcao = pygame.Rect(centro_x - 150, 300 + i * 70, 300, 50)
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
                            carregar_proxima_pergunta()
                        tempo_inicio = pygame.time.get_ticks()
                        estado = JOGANDO

            elif estado == OPCOES:
                for nome, rect in botoes_opcoes.items():
                    if rect.collidepoint(pos):
                        print(f"Opção selecionada: {nome}")
                        estado = INICIO

            elif estado == JOGANDO:
                if dificuldade_atual in ["FÁCIL", "DIFÍCIL"]:
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
        screen.blit(fundo, (0, 0)) if fundo else screen.fill((0, 0, 0))
    elif estado == SELECIONAR_DIFICULDADE:
        screen.blit(fundo_dificuldade, (0, 0)) if fundo_dificuldade else screen.fill((0, 0, 0))
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
        screen.blit(fundo, (0, 0)) if fundo else screen.fill((0, 0, 0))

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

        minutos, segundos = tempo_restante_atual // 60, tempo_restante_atual % 60
        timer_text = f"Tempo restante: {minutos:02}:{segundos:02}"
        timer_render = fonte.render(timer_text, True, (255, 255, 255))
        screen.blit(timer_render, (centro_x - 100, 50))

        pontuacao_text = f"Pontos: {pontuacao}"
        pontuacao_render = fonte.render(pontuacao_text, True, (255, 255, 255))
        pontuacao_rect = pontuacao_render.get_rect(topright=(largura_tela - 20, 20))
        screen.blit(pontuacao_render, pontuacao_rect)

        if dificuldade_atual in ["FÁCIL", "DIFÍCIL"]:
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
