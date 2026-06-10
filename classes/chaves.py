import pygame as pg
import sys, os

from typing import List

SCREENRECT = pg.Rect(0, 0, 1280, 720)

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    file = os.path.join(main_dir, "data", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit(f'Erro ao carregar "{file}" {pg.get_error()}')
    return surface.convert()

class Jogo:

    def __init__(self):
        pg.init()
        self.tela = pg.display.set_mode(SCREENRECT.size)
        pg.display.set_caption('Chaves & Chapolin')
        self.clock = pg.time.Clock()
        self.rodando = True

        cenario_img = load_image("cenario.png")
        self.background = cenario_img.convert()
        self.tela.blit(self.background, (0, 0)) # o background não está centralizado, por algum motivo
        pg.display.flip()
    
    def processar_eventos(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                self.rodando = False
    
    def executar(self):
        ultimo_movimento = 0
        cooldown_movimentos = 200

        img = load_image("player1.gif")
        Player.images = [img, pg.transform.flip(img, 1, 0)]

        all = pg.sprite.RenderUpdates()

        player = Player(all)

        while self.rodando:
            self.processar_eventos()

            tempo_atual = pg.time.get_ticks()

            if (tempo_atual - ultimo_movimento >= cooldown_movimentos):

                keystate = pg.key.get_pressed()

            # direcao vertical
                direcao_v = keystate[pg.K_DOWN] - keystate[pg.K_UP]

            # direcao horizontal
                direcao_h = keystate[pg.K_RIGHT] - keystate[pg.K_LEFT]


                player.move(direcao_v, direcao_h)

                if direcao_h != 0 or direcao_v != 0:
                    ultimo_movimento = tempo_atual

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
        self.rect = SCREENRECT
        self.reloading = 0
        self.facing = -1

    def move(self, direcao_v, direcao_h):
        if direcao_h:
            self.facing = direcao_h

        self.rect.move_ip(300 * direcao_h, 300 * direcao_v)

        self.rect.clamp(SCREENRECT) # deveria colidir no screenrect, mas não ta pegando
        # provavelmente o retangulo do screenrect tá maior do que deveria ser


        if direcao_h < 0:
            self.image = self.images[0]
        elif direcao_h > 0:
            self.image = self.images[1]


