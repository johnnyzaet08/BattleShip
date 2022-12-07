import pygame

class Cuadro(pygame.sprite.Sprite):

    def __init__(self, posx, posy, nombre):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("Imagenes/" + nombre + ".png")
        self.rect = self.image.get_rect()

        self.rect.top = posy
        self.rect.left = posx
    
    def draw(self, window):
        window.blit(self.image, self.rect)
    
