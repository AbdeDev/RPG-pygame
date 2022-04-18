#reimportation de pygame et set_caption pour qu'il soit reconnu#
import pygame
import pytmx
import pyscroll
from pygame.display import set_caption, update

from player import Player
#declaration de jeu#
#note a moi meme = crée une classe implique la creation d'un parametre (init) sauf lorsque nous n'y mettre que des donnée et aucune methode#
class Game:
#creation de la fenetre de jeu#
    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Escape forest")
        
        #chercher la carte(format tmx)#
        tmx_data = pytmx.util_pygame.load_pygame('map.tmx')
        #extraire la carte( format tmx)#
        map_data = pyscroll.data.TiledMapData(tmx_data)
        #charger les different calque de la map#
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data,self.screen.get_size())
        #cree le zoom adequat(le suspense de la carte)#
        map_layer.zoom = 2

        #generer le player a partir du ficher player(le placer sur la map)#
        player_position = tmx_data.get_object_by_name("debut")
        self.player = Player(player_position.x, player_position.y)
        
        #liste contenant les rectangles de colision(au niveau de la map)#
        self.walls = []
        for obj in tmx_data.objects:
            if obj.type == "collision":
                self.walls.append(pygame.Rect(obj.x, obj.y, obj.width, obj.height))
        
        #cree le groupe de calque pour former la map et declarer la superposition du perso#
        self.groupe = pyscroll.PyscrollGroup(map_layer=map_layer,default_layer=3)
        #rajouter le joueur#
        self.groupe.add(self.player)
        
        #fonction/methode qui permet de deplacer le joueur grace au touche#
    def handle_input(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[pygame.K_DOWN]:
            self.player.move_down()
            self.player.change_animation('down')
        elif pressed[pygame.K_LEFT]:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[pygame.K_RIGHT]:
            self.player.move_right()
            self.player.change_animation('right')
    
    #methode/fonction qui va actualiser tout le groupe de la map et agira avec la collision du joueur)
    def update(self):
        self.groupe.update()
        #verification de la collision#
        for sprite in self.groupe.sprites():
            #le sprite contenant la proprieté feetdoit entrer en collision avec un element de la liste (walls) valeur superieur a -1
            if sprite.feet.collidelist(self.walls) > -1:
                #la methode pour revenir a la position avant le deplacement(colision)#
                sprite.move.back()


#fonction/methode qui permet de lancer le jeu#
    def run(self):
        #definir les fps pour rendre le jeu moins speed#
        clock = pygame.time.Clock()
        #boucles qui permet de rester dans le jeu#
        running = True
        while running:
            #memoriser la position du joueur#
            self.player.save_location()
            #enclencher le deplacement#
            self.handle_input()
            #actualiser le groupe#
            self.update()
            #camera qui suit le joueur tout le temps#
            self.groupe.center(self.player.rect)
            #dessiner le groupe de calque pour former la map# 
            self.groupe.draw(self.screen)
            #actualiser le jeu #
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    running = False
            #rappel de la variable qui contient maintenant une methode et qui nous met a 60fps)#
            clock.tick(60)
            #module nous permettant de quitter#
        pygame.QUIT()