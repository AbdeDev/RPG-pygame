#import des modules#
import pygame
from pygame.display import set_caption

from game import Game
#lier le ficher main et le ficher game#
if __name__=='__main__':
    pygame.init()
    game = Game()
    game.run()
