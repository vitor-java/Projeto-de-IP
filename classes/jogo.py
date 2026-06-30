import pygame as pg
import sys

from classes import items
from classes.items import Item
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

        self.dicionario_mapas = {0: load_image("cenarios/cenario0.png").convert(), 1: load_image("cenarios/cenario1.png").convert(),
                                 2: load_image("cenarios/cenario2.png").convert()}


        self.dicionario_mapas_overlays = {0: load_image("cenarios/overlays/cenario0_overlay.png").convert_alpha(), 1: load_image("cenarios/overlays/cenario1_overlay.png").convert_alpha(),
                                 2: load_image("cenarios/overlays/cenario2_overlay.png").convert_alpha()}


        item_bola = Item(carregar_sprite("coletaveis/bola_item.png", 70, 70), carregar_sprite("coletaveis/bola.png", 60, 60), (6, 6), 1)

        item_marreta = Item(carregar_sprite("coletaveis/marreta_item.png", 70, 70),
                         carregar_sprite("coletaveis/marreta.png", 60, 60), (2, 4), 0)

        item_sanduiche = Item(carregar_sprite("coletaveis/sanduiche_item.png", 70, 70),
                         carregar_sprite("coletaveis/sanduiche.png", 60, 60), (6, 10), 2)

        self.items = [item_bola, item_marreta, item_sanduiche]

        self.tela.blit(self.dicionario_mapas[0], (0, 0))

        pg.display.flip()

        iniciar_cenarios()

    def trocar_cenario(self, cenario):
        self.cenario_atual = cenario
        self.tela.blit(self.dicionario_mapas[self.cenario_atual], (0, 0))
        pg.display.flip()

    def processar_eventos(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                self.rodando = False

    def executar(self):
        proximo_movimento = 0
        cooldown_movimentos = 70
        cooldown_movimentos_diagonal = cooldown_movimentos * (2 ** 0.5)
        cooldown_animacao = {
            0: 70, # baixo
            1: 110, # direita
            2: 110, # esquerda
            3: 70 # cima
        }

        Player.images[0] = [carregar_sprite("chaves/chaves_parado.png"),
                         carregar_sprite("chaves/chaves_baixo_1.png"),
                         carregar_sprite("chaves/chaves_baixo_2.png"),
                         carregar_sprite("chaves/chaves_baixo_3.png"),
                         carregar_sprite("chaves/chaves_baixo_4.png")] # sprites do chaves pra baixo

        Player.images[1] = [carregar_sprite("chaves/chaves_direita_parado.png"),
                         carregar_sprite("chaves/chaves_direita_1.png"),
                         carregar_sprite("chaves/chaves_direita_2.png"),
                         carregar_sprite("chaves/chaves_direita_3.png"),
                         carregar_sprite("chaves/chaves_direita_4.png")]

        Player.images[2] = [carregar_sprite("chaves/chaves_direita_parado.png", 70, 140, True),
                         carregar_sprite("chaves/chaves_direita_1.png", 70, 140, True),
                         carregar_sprite("chaves/chaves_direita_2.png", 70, 140, True),
                         carregar_sprite("chaves/chaves_direita_3.png", 70, 140, True),
                         carregar_sprite("chaves/chaves_direita_4.png", 70, 140, True)]


        Player.images[3] = [carregar_sprite("chaves/chaves_cima_parado.png"),
                         carregar_sprite("chaves/chaves_cima_1.png"),
                         carregar_sprite("chaves/chaves_cima_2.png"),
                         carregar_sprite("chaves/chaves_cima_3.png"),
                         carregar_sprite("chaves/chaves_cima_4.png")]


        all = pg.sprite.RenderUpdates()

        player = Player(all)

        while self.rodando:
            self.processar_eventos()
            tempo_atual = pg.time.get_ticks()

            if player.proximocenario != -1:
                self.trocar_cenario(player.proximocenario)
                player.proximocenario = -1

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
                    player.proximo_frame = tempo_atual + cooldown_animacao[player.facing]
                    if player.frame == 7:
                        player.frame = 1
                    else:
                        player.frame += 1

                    if (player.frame > 4):
                        frame = 8 - player.frame
                    else:
                        frame = player.frame

                    player.image = player.images[player.facing][frame]

                player.atualizar_movimento(self.cenario_atual)

            self.tela.blit(self.dicionario_mapas[self.cenario_atual], (0, 0))

            carregar_com_overlay = set()

            for i in range(len(self.items)) :
                item = self.items[i]

                if (not item.coletado) :

                    item_deve_aparecer = self.cenario_atual == item.cenario

                    if (item_deve_aparecer) :
                      if (not player.andando) :
                        if (item.posicao_matriz == player.pos_matriz) :
                          item.coletado = True

                    item_atras_do_jogador = item_deve_aparecer and item.posicao_matriz[0] < player.pos_matriz[0] + 1

                    if (item_atras_do_jogador):
                       item.update()
                       self.tela.blit(item.image, item.rect)
                    elif (item_deve_aparecer) :
                        carregar_com_overlay.add(item)

                    self.tela.blit(item.icone_apagado, (20 + 70 * i, 20))
                else :
                    self.tela.blit(item.icone, (20 + 70 * i, 20))


            all.draw(self.tela) # jogador

            for item in carregar_com_overlay :
              item.update()
              self.tela.blit(item.image, item.rect)

            self.tela.blit(self.dicionario_mapas_overlays[self.cenario_atual], (0, 0))

            pg.display.flip()

            self.clock.tick(60)

        pg.quit()
        sys.exit()