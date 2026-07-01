import pygame as pg

import classes.mapa
from classes.mapa import checar_colisao


class Npc(pg.sprite.Sprite):
    def __init__(self, imagem, imagem_outline, posicao, balao, texto_sem_item, texto_com_item, cenario, item, colisao=True):
        pg.sprite.Sprite.__init__(self)
        self.cenario = cenario

        self.imagem = imagem
        self.imagem_outline = imagem_outline

        self.rect = self.imagem.get_rect()
        self.posicao_matriz = posicao
        self.rect.center = (posicao[1] * 70, (posicao[0] - 1) * 70)

        self.fonte = pg.font.Font("data/fontes/fonte.ttf", 28)
        self.balao = balao
        self.texto_sem_item = texto_sem_item
        self.texto_com_item = texto_com_item
        self.texto_atual = self.texto_sem_item

        self.balao_visivel = False
        self.balao_tempo = 0

        self.item = item


        if colisao:
            classes.mapa.matrizes[cenario].alterar_elemento(self.posicao_matriz[0], self.posicao_matriz[1], True)

    def set_colisao(self, colisao):
        classes.mapa.matrizes[self.cenario].alterar_elemento(self.posicao_matriz[0], self.posicao_matriz[1], colisao)

    def player_adjacente(self, cenario, player_pos):
        if (self.cenario != cenario) :
            return False
        player_pos_x = player_pos[1]
        player_pos_y = player_pos[0]
        npc_pos_x = self.posicao_matriz[1]
        npc_pos_y = self.posicao_matriz[0]

        outline = False
        if (player_pos_x == npc_pos_x):
            if (player_pos_y <= npc_pos_y + 1 and player_pos_y >= npc_pos_y - 1):
                outline = True
        elif (player_pos_y == npc_pos_y):
            if (player_pos_x <= npc_pos_x + 1 and player_pos_x >= npc_pos_x - 1):
                outline = True
        return outline

    def desenhar(self, cenario, player_pos, tela):
        if (self.cenario != cenario) :
            return

        outline = self.player_adjacente(cenario, player_pos)

        if (outline):
            tela.blit(self.imagem_outline, self.rect.center)
        else :
            tela.blit(self.imagem, self.rect.center)

    def interagir(self, cenario, player, coletado) :

        pode_interagir = self.player_adjacente(cenario, player.pos_matriz)

        if not pode_interagir:
            return

        self.coletado = coletado

        if (coletado and checar_colisao(self.posicao_matriz[0], self.posicao_matriz[1], cenario)) :
            self.set_colisao(False)
            self.texto_atual = self.texto_com_item


        self.exibir_balao(player)

    def exibir_balao(self, player):
        player.pode_andar = False
        self.balao_visivel = True
        self.balao_tempo = pg.time.get_ticks() + 8000

    def atualizar_balao(self, player, tela):
        if self.balao_visivel :
            if pg.time.get_ticks() >= self.balao_tempo:
              self.balao_visivel = False
              player.pode_andar = True
            else :
                self.desenhar_balao(tela)

    def desenhar_balao(self, tela) :
        tela.blit(self.balao, (0,0))

        y = 640
        for linha in self.texto_atual.split("\n"):
            texto = self.fonte.render(linha, True, (255, 255, 255))
            tela.blit(texto, (352, y))
            y += 30




