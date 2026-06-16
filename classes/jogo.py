import pygame as pg
import sys

from classes.utils import SCREENRECT, load_image, carregar_sprite

from classes.personagem import Player

from classes.mapa import iniciar_cenarios

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
        self.tela.blit(self.background, (0, 0))

        pg.display.flip()

        iniciar_cenarios()
    
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
        
        player = Player(all)

        while self.rodando:
            self.processar_eventos()
            tempo_atual = pg.time.get_ticks()

            if (tempo_atual >= proximo_movimento):
                keystate = pg.key.get_pressed()
                direcao_v = keystate[pg.K_DOWN] - keystate[pg.K_UP]
                direcao_h = keystate[pg.K_RIGHT] - keystate[pg.K_LEFT]
                diagonal = direcao_h != 0 and direcao_v != 0

                if (diagonal):
                    proximo_movimento = tempo_atual + cooldown_movimentos_diagonal
                elif direcao_v != 0 or direcao_h != 0:
                    proximo_movimento = tempo_atual + cooldown_movimentos

                player.move(direcao_v, direcao_h, self.cenario_atual)

            if player.andando:
                if tempo_atual >= player.proximo_frame:
                    player.proximo_frame = tempo_atual + cooldown_movimentos
                    if player.frame == 7:
                        player.frame = 1
                    else:
                        player.frame += 1

                    if (player.frame > 4):
                        frame = 8 - player.frame
                    else:
                        frame = player.frame

                    player.image = player.images[frame]

                player.atualizar_movimento()

            all.clear(self.tela, self.background)
            dirty = all.draw(self.tela)
            pg.display.update(dirty)
            self.clock.tick(60)
    
        pg.quit()
        sys.exit()