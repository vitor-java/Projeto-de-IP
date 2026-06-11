import pygame as pg
import sys, os

from typing import List

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
        cooldown_movimentos = 200
        cooldown_movimentos_diagonal = 282.8 * 2


        Player.images = [carregar_sprite("chaves_parado.png"),
                         carregar_sprite("chaves_baixo_1.png"),
                         carregar_sprite("chaves_baixo_2.png"),
                         carregar_sprite("chaves_baixo_3.png"),
                         carregar_sprite("chaves_baixo_4.png")]

        all = pg.sprite.RenderUpdates()

        player = Player(all)

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

                player.move(direcao_v, direcao_h)

            if player.andando :

                if tempo_atual >= player.proximo_frame:

                    player.proximo_frame = tempo_atual + cooldown_movimentos/2

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

def get_posicao_na_matriz(pos_x, pos_y): # se baseie na matriz enviada no zap
    pos_x *= 70
    pos_x += 35
    pos_y *= 70
    return (pos_x, pos_y)

class Player(pg.sprite.Sprite):

    bounce = 24
    images: List[pg.Surface] = []

    def __init__(self, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect() # pelo visto, isso é o retangulo do sprite do jogador, tipo uma hitbox
        self.rect.center = get_posicao_na_matriz(7, 7) # player spawna aqui

        self.andando = False
        self.proxima_pos = (0, 0)
        self.proximo_frame = 0
        self.frame = 0

        self.reloading = 0
        self.facing = -1

    def move(self, direcao_v, direcao_h):
        if not self.andando :
            suposta_prox_pos = (self.rect.centerx + 70 * direcao_h, self.rect.centery + 70 * direcao_v)
            proximo_rect = self.rect.copy()
            proximo_rect.center = suposta_prox_pos
            if (SCREENRECT.contains(proximo_rect)) : # impede que saia da tela
              self.proxima_pos = suposta_prox_pos
              self.andando = True

    def atualizar_movimento(self): # só pra animação isso aq

        if (not self.andando) :
            return

        velocidade = 2
        proxima_pos_x = self.proxima_pos[0]
        proxima_pos_y = self.proxima_pos[1]

        vx = 0
        vy = 0

        if (self.rect.centerx < proxima_pos_x) :
            vx = 1
        elif (self.rect.centerx > proxima_pos_x) :
            vx = -1

        if (self.rect.centery < proxima_pos_y) :
            vy = 1
        elif (self.rect.centery > proxima_pos_y) :
            vy = -1

        self.rect.move_ip(vx * velocidade, vy * velocidade)

        self.rect = self.rect.clamp(SCREENRECT)

        if (self.rect.center == self.proxima_pos) :
            self.andando = False
            self.image = self.images[0]


