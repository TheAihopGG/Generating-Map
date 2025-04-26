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
        self.add_child(self.cubic)

        self.add_child(PingPong(self.screen, 200, 100, 1.5))

        self.add_child(Sprite("Assets/town.png", self.screen, 200, 200, 4))
    
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
            self.add_child(PingPong(self.screen, mouse_position[0], mouse_position[1], 1.5))

        elif not mouse_pressed[0]:
            self.mouse_button_pressed[0] = False

        # Правая кнопка мыши
        if mouse_pressed[2] and not self.mouse_button_pressed[2]:
            self.mouse_button_pressed[2] = True
            
            self.add_child(
                    Sprite(
                        "Assets/town.png", self.screen, 
                        mouse_position[0] - 8*4, mouse_position[1] - 8*4, 
                        4, random.randint(-3, 3)
                    )
                )

        elif not mouse_pressed[2]:
            self.mouse_button_pressed[2] = False


class PingPong(Circle):    
    def __init__(self, screen, x = 0, y = 0, scale = 1):
        super().__init__(screen, x, y, scale)
        self.vec : list = [1, 1]

        self.color = YELLOW
        self.contour_thickness = 1
    
    def _process(self) -> None:
        if self.x >= 1152:
            self.vec[0] = -1
        if self.x <= 0:
            self.vec[0] = 1

        if self.y >= 648:
            self.vec[1] = -1
        if self.y <= 0:
            self.vec[1] = 1

        self.x += self.vec[0] * 5
        self.y += self.vec[1] * 5


if __name__ == "__main__":
    game : Game = Game()
    print(game)
    game._process()