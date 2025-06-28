import pygame
from views.componentes import desenhar_botao

def desenhar_tela_inicio(
  tela, fontes, textos, cores, 
  input_ativo, caixa_texto, nome_jogador,
  img_sair

):
    
    fonte_media = fontes["media"]
    fonte_grande = fontes["grande"]
    fonte_titulo = fontes["titulo"]

    AZUL  = cores["AZUL"]
    BRANCO = cores["BRANCO"]
    ROSA = cores["ROSA"]
    ROSA_CLARO = cores["ROSA_CLARO"]
    ROXO = cores["ROXO"]
    CINZA = cores["CINZA"]
    ROXO_FORTE = cores["ROXO_FORTE"]

    LARGURA, ALTURA = tela.get_size()

    #fundo azul
    tela.fill(AZUL)

    titulo = fonte_titulo.render(textos["titulo"], True, BRANCO)

    #desenhar o retangulo rosa ####talvez eu tire####
    titulo_rect = pygame.draw.rect(
        tela, ROSA,
        (LARGURA // 2 - titulo.get_width()//2 -20, 80,
         titulo.get_width() + 40, titulo.get_height() + 40),
         border_radius = 20
    )

    #desenhar/escrever o título
    tela.blit(titulo,(LARGURA//2 - titulo.get_width()//2, 100))


    #retangulo do input
    pygame.draw.rect(
        tela, BRANCO if input_ativo else ROXO_FORTE,
        caixa_texto, 0, border_radius=15
)
    pygame.draw.rect(tela, CINZA, caixa_texto, 3, border_radius=15)
    texto_nome = fonte_media.render(textos["digite_nome"], True, CINZA)
    tela.blit(texto_nome, (caixa_texto.x, caixa_texto.y - 40))

    texto_input = fonte_media.render(nome_jogador, True, CINZA)
    tela.blit(texto_input, (caixa_texto.x + 10, caixa_texto.y + 15))

    #botao de jogar yay
    texto_botao = fonte_grande.render(textos["coemcar"], True, BRANCO)
    largura_botao = max(288, texto_botao.get_width() + 60)
    botao_inicio_rect = pygame.Rect(
        LARGURA // 2 - largura_botao // 2, ALTURA // 2 + 70, largura_botao, 70
    )

    mouse_pos = pygame.mouse.get_pos()
    cor_botao = ROSA if botao_inicio_rect.collidepoint(mouse_pos) else ROXO

    desenhar_botao(
        tela,
        botao_inicio_rect,
        texto_botao,
        fonte_grande,
        BRANCO,
        border_radius = 20
    )

