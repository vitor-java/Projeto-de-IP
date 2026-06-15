cenarios = {
    0: {
        (10, 11), (10, 12), (9, 13), (8, 13), (7, 13),
        (6, 13), (5, 13), (4, 12), (4, 11), (4, 10),
        (3, 10), (2, 9), (2, 8), (2, 6), (2, 7),
        (4, 5), (5, 5), (6, 5), (6, 6), (7, 5),
        (7, 6), (6, 4), (7, 3), (8, 3), (6, 3),
        (5, 3), (4, 3), (3, 3), (2, 3), (2, 5),
        (3, 4), (1, "*"), ("*", 1)
    }
}

def get_posicao_na_matriz(pos_x, pos_y):
    pos_x *= 70
    pos_x += 35
    pos_y *= 70
    return (pos_x, pos_y)

def checar_colisao(y, x, cenario):
    colisoes = cenarios[cenario]
    if (y, x) in colisoes:
        return False
    if (y, "*") in colisoes:
        return False
    if ("*", x) in colisoes:
        return False
    return True