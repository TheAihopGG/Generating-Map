import pygame
import random
from MaratEngine.Engine import *
from MaratEngine.utils.Node import *


class Game(Loop):
    def __init__(self) -> None:
        super().__init__()

        self.TILE_SIZE : int = 32

        self.level = [
            "####################################",
            "#                                  #",
            "#                                  #",
            "#                                  #",
            "#            ##                    #",
            "#                                  #",
            "##                                 #",
            "#                                  #",
            "#                   ###            #",
            "#                                  #",
            "#                                  #",
            "#      ###                         #",
            "#                                  #",
            "#   ###########                    #",
            "#                                  #",
            "#                #                 #",
            "#                   ##             #",
            "#                                  #",
            "#                            ###   #",
            "####################################"
       ]
        self.load_tile_map()

        self.player : Player = Player(self.screen, 320, 320)
        self.player.size = 16
        self.add_child(self.player)
    
    def _process(self) -> None:
        while self.running:
            for event in pygame.event.get():    
                if event.type == pygame.QUIT: 
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.move_direction = -1

                    if event.key == pygame.K_RIGHT:
                        self.player.move_direction = 1

                    if event.key == pygame.K_UP:
                        self.player.jump = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                        self.player.move_direction = 0

                    if event.key == pygame.K_UP:
                        self.player.jump = False   

            super()._process()
        
        pygame.quit()


    def load_tile_map(self) -> None:

        for y, row in enumerate(self.level): 
            for x, col in enumerate(row):
                if col == "#":
                    tile : Square = Square(self.screen, x * self.TILE_SIZE, y * self.TILE_SIZE)
                    tile.size = self.TILE_SIZE
                    tile.color = GREEN
                    self.add_child(tile)
                        
class Player(Circle):
    def __init__(self, screen, x=0, y=0, scale=1):
        super().__init__(screen, x, y, scale)
        self.JUMP_POWER = 100
        self.GRAVITY = 2
        self.move_direction : int = 0
        self.jump : bool = False
        self.is_on_floor : bool = False 
    
    def _process(self):
        if self.move_direction:
            self.x += self.move_direction * 5

        if self.jump and self.is_on_floor:
            self.is_on_floor = False
            self.y += -self.JUMP_POWER

        if not self.is_on_floor:
            self.y += self.GRAVITY

        row = int((self.y - game.TILE_SIZE / 2) // game.TILE_SIZE) + 1
        col = self.x // game.TILE_SIZE

        self.is_on_floor = game.level[row][col] == "#"

if __name__ == "__main__":
    game : Game = Game()
    game._process()