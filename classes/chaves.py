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
        cooldown_movimentos_diagonal = 282.8

        img = load_image("chaves1.png")
        img = pg.transform.smoothscale(img, (70, 140))
        Player.images = [img, pg.transform.flip(img, 1, 0)]

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

            # limpa os sprites da tela
            all.clear(self.tela, self.background)

            # desenha os sprite
            dirty = all.draw(self.tela)

            # atualiza os spirte na tela
            pg.display.update(dirty)
            self.clock.tick(60)
    
        pg.quit()
        sys.exit()



class Player(pg.sprite.Sprite):

    bounce = 24
    images: List[pg.Surface] = []

    def __init__(self, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect() # pelo visto, isso é o retangulo do sprite do jogador, tipo uma hitbox
        self.rect.center = (525, 490) # player spawna no meio

        # posição inicial da matriz que mandei no zap: 

        self.reloading = 0
        self.facing = -1

    def move(self, direcao_v, direcao_h):
        if direcao_h:
            self.facing = direcao_h

        self.rect.move_ip(70 * direcao_h, 70 * direcao_v)

        self.rect = self.rect.clamp(SCREENRECT)


        if direcao_h < 0:
            self.image = self.images[0]
        elif direcao_h > 0:
            self.image = self.images[1]


