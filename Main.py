import pygame
from MaratEngine.Engine import *
from MaratEngine.utils.Node import *


class Game(Loop):
    def __init__(self) -> None:
        super().__init__()

        self.cubic : Cubic = Cubic(self.screen, 500, 300, RED, 50)
        self.add_child(self.cubic)
        self.ball = Ball(self.screen, 200, 100, BLUE, 15)
        self.add_child(self.ball)
        
    
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
        mouse_position : list = pygame.mouse.get_pos()
        
        self.cubic.x = mouse_position[0] - self.cubic.size / 2
        self.cubic.y = mouse_position[1] - self.cubic.size / 2

        if mouse_pressed[0] and not self.pressed[0]:
            self.pressed[0] = True
            self.ball = Ball(self.screen, mouse_position[0], mouse_position[1], BLUE, 15)
            self.add_child(self.ball)
        elif not mouse_pressed[0]:
            self.pressed[0] = False

    
game : Game = Game()
game._process()