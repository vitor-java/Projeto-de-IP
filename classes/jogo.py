import pygame as pg
import sys

from classes import items, gif_overlay
from classes.gif_overlay import Gif
from classes.items import Item
from classes.npc import Npc
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

        self.explosao = Gif() # gif da explosão

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
        # item 0 -> bola
        # item 1 -> marreta
        # item 2 -> sanduiche

        self.tela.blit(self.dicionario_mapas[0], (0, 0))

        pg.display.flip()

        iniciar_cenarios()

        chapolim = Npc(carregar_sprite("chapolim/chapolim.png", 70, 140, True),
                  carregar_sprite("chapolim/chapolim_outline.png", 70, 140, True), (5, 12), load_image("balao_de_fala/chapolin.png").convert_alpha(), "Eu posso te deixar \npassar se você encontrar \na minha marreta!", "Obrigado! Você pode \npassar agora.", 0, 1) # #

        quico = Npc(carregar_sprite("quico/quico.png", 70, 140, True),
                       carregar_sprite("quico/quico_outline.png", 70, 140, True), (8, 2), load_image("balao_de_fala/quico.png").convert_alpha(), "Eu vou te deixar \npassar se você achar \nminha bola quadrada!", "Pode passar.", 0, 0)

        self.npcs = [chapolim, quico]

        self.proximo_interact = 0
        self.cooldown_interact = 200

    def trocar_cenario(self, cenario):
        self.cenario_atual = cenario
        self.tela.blit(self.dicionario_mapas[self.cenario_atual], (0, 0))
        pg.display.flip()

    def processar_eventos(self):
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                self.rodando = False

            elif (evento.type == pg.KEYDOWN and evento.key == pg.K_e and pg.time.get_ticks() >= self.proximo_interact):
                self.proximo_interact = pg.time.get_ticks() + self.cooldown_interact

                for npc in self.npcs:
                    if (not npc.balao_visivel):
                        npc.interagir(self.cenario_atual, self.player, self.items[npc.item].coletado)
                    else :
                        npc.balao_visivel = False
                        self.player.pode_andar = True

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

        tela_final = load_image("cenarios/overlays/final.png").convert_alpha()

        gato_sprites = [carregar_sprite("gato/gatofdp1.png", 100, 100, True).convert_alpha(), carregar_sprite("gato/gatofdp2.png", 100, 100, True).convert_alpha()]

        all = pg.sprite.RenderUpdates()

        player = Player(all)
        self.player = player

        while self.rodando:


            self.processar_eventos()

            tempo_atual = pg.time.get_ticks()

            if player.proximocenario != -1:
                self.trocar_cenario(player.proximocenario)
                player.proximocenario = -1


            keystate = pg.key.get_pressed()
            if (tempo_atual >= proximo_movimento and player.pode_andar):
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

            if player.explodido and self.explosao.pode_teleportar:
                self.explosao.pode_teleportar = False
                player.explodido = False
                self.trocar_cenario(0)
                player.teleportar(3, 9, 2)

            elif player.explodido and not self.explosao.ta_tocando:
                self.explosao.iniciar()

            self.tela.blit(self.dicionario_mapas[self.cenario_atual], (0, 0))

            carregar_com_overlay = set()

            for i in range(len(self.items)) :
                item = self.items[i]

                if (not item.coletado) :

                    item_deve_aparecer = self.cenario_atual == item.cenario

                    if (item_deve_aparecer) :
                      if (not player.andando) :
                        if (item.posicao_matriz == player.pos_matriz) :
                          if i == 2 :
                              self.explosao.iniciar() # so de resenha
                              player.pode_andar = False
                              player.acabou = True
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

            npcs_na_frente = set()
            baloes = set()

            for i in range(len(self.npcs)) :
                npc = self.npcs[i]

                npc_atras_do_jogador = npc.posicao_matriz[0] < player.pos_matriz[0]

                if (npc.balao_visivel) :
                    baloes.add(npc)

                if npc_atras_do_jogador:
                    npc.desenhar(self.cenario_atual, player.pos_matriz, self.tela)
                else :
                    npcs_na_frente.add(npc)

            all.draw(self.tela) # jogador

            for npc in npcs_na_frente:
                npc.desenhar(self.cenario_atual, player.pos_matriz, self.tela)

            if (self.cenario_atual == 1) :
                if (not player.explodido) :
                    self.tela.blit(gato_sprites[0], (748, 523))
                else :
                    self.tela.blit(gato_sprites[1], (748, 523))

            for item in carregar_com_overlay :
              item.update()
              self.tela.blit(item.image, item.rect)

            self.tela.blit(self.dicionario_mapas_overlays[self.cenario_atual], (0, 0))

            for npc in baloes :
                npc.atualizar_balao(player, self.tela)

            self.explosao.atualizar()
            self.explosao.desenhar(self.tela)

            if player.acabou and not self.explosao.ta_tocando:
                self.tela.blit(tela_final, (0, 0))

            pg.display.flip()

            self.clock.tick(60)

        pg.quit()
        sys.exit()