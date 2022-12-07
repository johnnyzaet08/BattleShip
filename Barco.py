import pygame

class Barco(pygame.sprite.Sprite):

    def __init__(self, posx, posy, tipo, cuadros):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Imagenes/" + str(tipo) + ".png")
        self.rect = self.image.get_rect()
        
        self.cruadros = cuadros

        self.rect.top = posy
        self.rect.left = posx
    
    def set_Image(self, tipo, cuadros):
        self.image = pygame.image.load("Imagenes/" + str(tipo) + ".png")
        self.cruadros = cuadros

    
    def draw(self, window):
        window.blit(self.image, self.rect)