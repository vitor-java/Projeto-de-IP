import pygame as pg
from typing import List
from classes.utils import SCREENRECT
from classes.mapa import get_posicao_na_matriz, checar_colisao



class Player(pg.sprite.Sprite):

    bounce = 24
    images: List[pg.Surface] = []

    def __init__(self, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.proximocenario = -1
        self.image = self.images[0]
        self.rect = self.image.get_rect()

        self.pos_matriz = (7, 7)
        self.rect.center = get_posicao_na_matriz(7, 7)

        self.prox_cenario = -1
        self.andando = False
        self.proxima_pos = (0, 0)
        self.proximo_frame = 0
        self.frame = 0

        self.reloading = 0
        self.facing = -1    

    def move(self, direcao_v, direcao_h, cenario):
        if not self.andando:
            suposta_prox_pos = (self.rect.centerx + 70 * direcao_h, self.rect.centery + 70 * direcao_v)
            proximo_rect = self.rect.copy()
            proximo_rect.center = suposta_prox_pos
            if (SCREENRECT.contains(proximo_rect)):
                pos_atual = self.pos_matriz
                y, x = pos_atual[0], pos_atual[1]
                yi, xi = y + direcao_v, x + direcao_h


                if direcao_h != 0 and direcao_v != 0:
                    colisao = checar_colisao(y, xi, cenario) or checar_colisao(yi, x, cenario) or checar_colisao(yi, xi, cenario)
                else :
                    colisao = checar_colisao(yi, xi, cenario)
                if not colisao:

                    self.pos_matriz = (yi, xi)
                    self.proxima_pos = suposta_prox_pos
                    self.andando = True



    def teleportar(self, y, x):
        self.frame = 0
        self.andando = False
        self.pos_matriz = (y, x)
        xi, yi = get_posicao_na_matriz(x, y)
        self.rect.center = (xi, yi)

    def atualizar_movimento(self, cenario):
        if (not self.andando):
            return

        velocidade = 2
        proxima_pos_x = self.proxima_pos[0]
        proxima_pos_y = self.proxima_pos[1]

        vx = 0
        vy = 0

        if (self.rect.centerx < proxima_pos_x):
            vx = 1
        elif (self.rect.centerx > proxima_pos_x):
            vx = -1

        if (self.rect.centery < proxima_pos_y):
            vy = 1
        elif (self.rect.centery > proxima_pos_y):
            vy = -1

        self.rect.move_ip(vx * velocidade, vy * velocidade)
        self.rect = self.rect.clamp(SCREENRECT)

        if (self.rect.center == self.proxima_pos):

            if cenario == 1 and (self.pos_matriz == (10, 6) or self.pos_matriz == (10, 7)):  # testando portas
                self.proximocenario = 0
                self.teleportar(3, 9)
                return

            if cenario == 2 and self.pos_matriz[0] == 10:  # testando portas
                self.proximocenario = 0
                self.teleportar(5, 12)
                return

            if cenario == 0 and self.pos_matriz == (3, 10):  # testando portas
                self.proximocenario = 1
                self.teleportar(9, 7)
                return

            if cenario == 0 and self.pos_matriz == (5, 13):  # testando portas
                self.proximocenario = 2
                self.teleportar(9, 7)
                return

            self.andando = False
            self.image = self.images[0]
