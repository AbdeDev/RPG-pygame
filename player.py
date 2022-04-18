#reinporter les modules#
import pygame
from pygame import image
#crée la class du joueur#
class Player(pygame.sprite.Sprite):
    #fonction/methode initiale du joueur#
    def __init__(self, X, Y):
        super().__init__()
        self.sprite_sheet = pygame.image.load('player.png')
        #se servir de la fonction crée si dessous#
        self.image = self.get_image(0, 0)
        #enlever le fond(perso)#
        self.image.set_colorkey([0,0,0])
        #definir sa position(perso)#
        self.rect = self.image.get_rect()
        #palcer le joueur(perso)#
        self.position = [X, Y]
        #regard du joueur en fonction de la direction(perso)#
        self.images ={
            'down': self.get_image(0, 0),
            'left': self.get_image(0, 32),
            'right': self.get_image(0, 64),
            'up': self.get_image(0, 96)
        }
        #collision et position au niveau du joueur(collision)#
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
       
        #vitesse de deplacement du perso#
        self.speed = 2

     #fonction/methode pour definir la position du joueur avant deplacement (old_position) et(collision)#
    def save_location(self): self.old_position = self.position.copy()
    
    #methode/fonction qui change l'animation(perso)#
    def change_animation(self,name): 
        self.image = self.images[name]
        self.image.set_colorkey((0, 0, 0))

        #methode/fonction qui permet le deplacement sur la map(vitesse,direction perso)#
    def move_right(self): self.position[0] +=self.speed
    def move_left(self): self.position[0] -=self.speed
    def move_up(self): self.position[1] -=self.speed
    def move_down(self): self.position[1] +=self.speed 
    #methode/fonction qui met a jour le sprite du joueur#
    def update(self):
        self.rect.topleft = self.position
        #positioner les pieds du joueurs en fonction des rectangles de collision#
        self.feet.midbottom = self.rect.midbottom

    #methode/fonction pour se replacer en cas de collision#
    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom
      
#donner les coordonée de l'image(trouver l'image dans les fichers)#
#fonction/methode qui me donne l'image#
    def get_image(self, X, Y):
        #definition de la taille de l'image#
        image = pygame.Surface([32, 32])
        #extraction d'une partie des images(extraction du background pour pouvoir l'utiliser)#
        image.blit(self.sprite_sheet,(0,0),(X, Y, 32 , 32))
        return image