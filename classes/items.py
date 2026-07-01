import math

import pygame as pg

from classes.mapa import get_posicao_na_matriz


class Item(pg.sprite.Sprite):
    def __init__(self, imagem, icone, posicao, cenario):
        pg.sprite.Sprite.__init__(self)
        self.coletado = False
        self.cenario = cenario

        self.icone = icone
        self.icone_apagado = icone.copy()
        self.icone_apagado.set_alpha(128)

        self.image = imagem
        self.rect = self.image.get_rect()
        self.posicao_matriz = posicao
        self.rect.center = get_posicao_na_matriz(posicao[1], posicao[0])
        self.y_inicial = self.rect.y

    def update(self):
        if (self.coletado) :
            return
        self.rect.y = self.y_inicial + math.sin(pg.time.get_ticks() / 250) * 3 # pra ficar balançando pra cima e pra baixo