import pygame as pg

from classes.utils import carregar_sprite


class Gif:
    def __init__(self):
        self.frames = [
            carregar_sprite(f"gato/exp{i}.png", 980, 770)
            for i in range(20)
        ]

        self.ta_tocando = False
        self.frame = 0
        self.proximo_frame = 0
        self.pode_teleportar = False

    def iniciar(self):
        self.ta_tocando = True
        self.frame = 0
        self.pode_teleportar = False
        self.proximo_frame = pg.time.get_ticks()

    def atualizar(self):
        if not self.ta_tocando:
            return

        frame = pg.time.get_ticks()

        if frame >= self.proximo_frame:
            self.proximo_frame = frame + 40   # 25 FPS
            self.frame += 1

            if self.frame >= len(self.frames):
                self.frame = 19
                self.pode_teleportar = True
                self.ta_tocando = False

    def desenhar(self, tela):
        if self.ta_tocando:
            tela.blit(self.frames[self.frame], (0, 0))