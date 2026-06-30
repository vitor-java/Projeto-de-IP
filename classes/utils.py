import pygame as pg
import os

SCREENRECT = pg.Rect(0, 0, 980, 770)

# Volta uma pasta para achar a raiz do projeto (onde está a pasta 'data')
main_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_image(file):
    file = os.path.join(main_dir, "data", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit(f'Erro ao carregar "{file}" {pg.get_error()}')
    return surface.convert_alpha()

def carregar_sprite(nome, largura=70, altura=140, flip= False):
    img = pg.transform.scale(load_image(nome), (largura, altura))
    if (flip) :
        img = pg.transform.flip(img, True, False)
    return img