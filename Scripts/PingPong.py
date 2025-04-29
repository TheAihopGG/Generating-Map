import pygame
import random
from MaratEngine.Engine import *
from MaratEngine.utils.Node import *


class Game(Loop):
    def __init__(self) -> None:
        super().__init__()

        self.cubic : Square = Square(self.screen, 500, 300)
        self.cubic.color = RED
        self.cubic.size = 40
        self.cubic.border_radius = 8

        self.add_child(self.cubic)
    
    def _process(self) -> None:
        while self.running:
            for event in pygame.event.get():    
                if event.type == pygame.QUIT: 
                    self.running = False
            
            super()._process()
            self._input()
        
        pygame.quit()

    def _input(self) -> None:
        mouse_pressed : tuple = pygame.mouse.get_pressed()
        mouse_position : tuple = pygame.mouse.get_pos()
        
        self.cubic.x = mouse_position[0] - self.cubic.size / 2
        self.cubic.y = mouse_position[1] - self.cubic.size / 2

        # Левая кнопка мыши
        if mouse_pressed[0] and not self.mouse_button_pressed[0]:
            self.mouse_button_pressed[0] = True
            self.add_child(PingPong(self.screen, mouse_position[0], mouse_position[1], 40))

        elif not mouse_pressed[0]:
            self.mouse_button_pressed[0] = False

        # Правая кнопка мыши
        if mouse_pressed[2] and not self.mouse_button_pressed[2]:
            self.mouse_button_pressed[2] = True
            SCALE : int = 2
            self.add_child(Sprite("Assets/town.png", self.screen, mouse_position[0] - 8 * SCALE, mouse_position[1] - 8 * SCALE, SCALE))

        elif not mouse_pressed[2]:
            self.mouse_button_pressed[2] = False


class PingPong(Circle):    
    def __init__(self, screen, x = 0, y = 0, size = 1):
        super().__init__(screen, x, y, size)
        self.vec : list = [1, 1]
        self.color = WHITE
    
    def _process(self) -> None:
        if self.x >= game.WIDTH:
            self.vec[0] = -1
        if self.x <= 0:
            self.vec[0] = 1

        if self.y >= game.HEIGHT:
            self.vec[1] = -1
        if self.y <= 0:
            self.vec[1] = 1

        self.x += self.vec[0] * 5
        self.y += self.vec[1] * 5


if __name__ == "__main__":
    game : Game = Game()
    game._process()