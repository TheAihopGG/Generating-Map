import pygame
from MaratEngine.Engine import *
from MaratEngine.utils.Node import *


class Game(Loop):
    def __init__(self) -> None:
        super().__init__()

    def _process(self) -> None:
        while self.running:
            for event in pygame.event.get():    
                if event.type == pygame.QUIT: 
                    self.running = False
            
            super()._process()
        
        pygame.quit()

if __name__ == "__main__":
    game : Game = Game()
    game._process()