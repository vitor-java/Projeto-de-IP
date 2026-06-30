class matrizlogica:
    def __init__(self, nome, linhas=5, colunas=5):
        self.nome = nome
        self.linhas = linhas
        self.colunas = colunas
        #Inicializa a matriz
        self.dados = [[False for _ in range(colunas)] for _ in range(linhas)]

    def alterar_linha(self, linha, valor: bool):
        for i in range(self.colunas) :
            self.dados[linha][i] = valor

    def alterar_coluna(self, coluna, valor: bool):
        for i in range(self.linhas) :
            self.dados[i][coluna] = valor

    def exibir(self):
        #Para testar a matriz
        print(f"--- {self.nome} ---")
        for linha in self.dados:
            linha_visual = [1 if elemento else 0 for elemento in linha]
            print(linha_visual)
        print()

    def alterar_elemento(self, linha, coluna, valor: bool):
        if 0 <= linha < self.linhas and 0 <= coluna < self.colunas:
            self.dados[linha][coluna] = valor
            print(f"[{self.nome}] Elemento na posição ({linha}, {coluna}) alterado para {valor}.")

cenarios = {}

def get_posicao_na_matriz(pos_x, pos_y):
    pos_x *= 70
    pos_x += 35
    pos_y *= 70
    return (pos_x, pos_y) #Formato: coluna, linha

def checar_colisao(linha, coluna, cenario):
    return cenarios[cenario][linha][coluna]

#Formata os valores do set para valores em elementos da matriz:
def converter_set_para_matriz(colisoes, matriz):
    for colisao in colisoes:
        if (colisao[0] == "*"):
            matriz.alterar_coluna(colisao[1], True)
        elif (colisao[1] == "*"):
            matriz.alterar_linha(colisao[0], True)
        else:
            matriz.alterar_elemento(colisao[0], colisao[1], True)

#Inicia as colisoes dos 3 cenarios:
def iniciar_cenarios() :
    #Inicia as colisoes do cenario 0
    cenario_0 = {
    (1, "*"),
    (2, 1), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9),
    (3, 1), (3, 4), (3, 5),
    (4, 1), (4, 5), (4, 10), (4, 11), (4, 12),
    (5, 1), (5, 5),
    (6, 1), (6, 4), (6, 5), (6, 6),
    (7, 1), (7, 4), (7, 5), (7, 6), (7, 12),
    (8, 1), (8, 3), (8, 13),
    (9, 1), (9, 13), (6,13),
    (10, 11), (10, 12), (4, 13),
    ("*", 0)
    }

    #Inicia as colisoes do cenario 1
    cenario_1 = {
        (5, 3), (5, 4), (6, 3), (6, 4), (2, "*"),
        (3, 0), (3, 1), (3, 2), (3, 3), (3, 5),
        (3, 7), (3, 8), (3, 9), (4, 10), (4, 11), (5, 11),
        (6, 12), (7, 13),
        (10, 0), (10, 1), (10, 2), (10, 3), (10, 4), (10, 5),
        (10, 8), (10, 9), (10, 10), (10, 11), (10, 12), (10, 13),
        ("*", 13), (9,12)
    }

    #Inicia as colisoes do cenario 2
    cenario_2 = {
        (1, "*"),
        (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
        (3, 1), (3, 2), (3, 3), (3, 7), (3, 8), (3, 10),
        (4, 7), (4, 8), (4, 9), (4, 11), (4, 12),
        (5, 11),
        (6, 12),
        (8, 12),
        (9, 12),
        (10, 12),
        (10, 11),
        (9, 1), (8, 1), (7, 2), (6, 3), (5, 3), (4, 3),
        (6, 6), (6, 7), (6, 8),
        (7, 6), (7, 7), (7, 8),
        (8, 6), (8, 7), (8, 8),

        ("*", 0),
        ("*", 13)
    }
    
    matriz_cenario_0 = matrizlogica("Cenário 0", 11, 14)
    matriz_cenario_1 = matrizlogica("Cenário 0", 11, 14)
    matriz_cenario_2 = matrizlogica("Cenário 0", 11, 14)
    
    converter_set_para_matriz(cenario_0, matriz_cenario_0)
    converter_set_para_matriz(cenario_1, matriz_cenario_1)
    converter_set_para_matriz(cenario_2, matriz_cenario_2)

    cenarios[0] = matriz_cenario_0.dados
    cenarios[1] = matriz_cenario_1.dados
    cenarios[2] = matriz_cenario_2.dados