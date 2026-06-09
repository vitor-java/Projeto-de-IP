import pygame, sys

class Jogo:
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption('Chaves & Chapolin')
        self.clock = pygame.time.Clock()
        self.rodando = True
    
    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False
    
    def executar(self):
        while self.rodando:
            self.processar_eventos()
            pygame.display.update()
            self.clock.tick(60)
    
        pygame.quit()
        sys.exit()

jogo = Jogo()
jogo.executar()