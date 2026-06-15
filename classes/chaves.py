# classe principal do jogo. onde deve ter as funções principais do pygame (clock, eventos, etc.)

import pygame as pg
import sys, os

from classes.player import Player

SCREENRECT = pg.Rect(0, 0, 980, 770)

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    file = os.path.join(main_dir, "data", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit(f'Erro ao carregar "{file}" {pg.get_error()}')
    return surface.convert_alpha()

def carregar_sprite (nome, largura = 70, altura = 140) :
    img = pg.transform.scale(load_image(nome), (largura, altura))
    return img

class Jogo:

    def __init__(self):
        pg.init()
        self.tela = pg.display.set_mode(SCREENRECT.size)
        pg.display.set_caption('Chaves & Chapolin')
        self.clock = pg.time.Clock()
        self.rodando = True
        self.cenario_atual = 0

        cenario_img = load_image("cenario.png")
        self.background = cenario_img.convert()
        self.tela.blit(self.background, (0, 0)) # centralizei essa poha
        pg.display.flip()
    
    def processar_eventos(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                self.rodando = False
    
    def executar(self):
        proximo_movimento = 0
        cooldown_movimentos = 100
        cooldown_movimentos_diagonal = 141.4

        Player.images = [carregar_sprite("chaves_parado.png"),
                         carregar_sprite("chaves_baixo_1.png"),
                         carregar_sprite("chaves_baixo_2.png"),
                         carregar_sprite("chaves_baixo_3.png"),
                         carregar_sprite("chaves_baixo_4.png")]

        all = pg.sprite.RenderUpdates()

        player = Player(SCREENRECT, all)

        while self.rodando:
            self.processar_eventos()

            tempo_atual = pg.time.get_ticks()

            if (tempo_atual >= proximo_movimento):


                keystate = pg.key.get_pressed()

                # direcao vertical
                # desse jeito cancela caso os dois sejam apertados ao mesmo tempo
                # roubei a ideia do codigo de exemplo aliens.py
                direcao_v = keystate[pg.K_DOWN] - keystate[pg.K_UP]

                # direcao horizontal
                direcao_h = keystate[pg.K_RIGHT] - keystate[pg.K_LEFT]

                diagonal = direcao_h != 0 and direcao_v != 0

                if (diagonal) :
                    proximo_movimento = tempo_atual + cooldown_movimentos_diagonal
                elif direcao_v != 0 or direcao_h != 0: # se não for diagonal, verifica pelo menos se moveu antes de setar o cooldown
                    proximo_movimento = tempo_atual + cooldown_movimentos

                player.move(direcao_v, direcao_h, self.cenario_atual)

            if player.andando :

                if tempo_atual >= player.proximo_frame:

                    player.proximo_frame = tempo_atual + cooldown_movimentos

                    if player.frame == 7:
                        player.frame = 1 # 8 volta pro 1
                    else :
                        player.frame += 1 # 1, 2, 3, 4, 3, 2, 1

                    if (player.frame > 4) :
                        frame = 8 - player.frame
                    else :
                        frame = player.frame


                    player.image = player.images[frame]

                player.atualizar_movimento()

            # limpa os sprites da tela
            all.clear(self.tela, self.background)

            # desenha os sprite
            dirty = all.draw(self.tela)

            # atualiza os spirte na tela
            pg.display.update(dirty)
            self.clock.tick(60)
    
        pg.quit()
        sys.exit()


