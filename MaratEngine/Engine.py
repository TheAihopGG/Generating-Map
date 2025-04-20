import pygame
from MaratEngine.utils.Node import *


BLACK : int = (0, 0, 0)
WHITE : int = (255, 255, 255)
RED   : int = (255, 0, 0)
BLUE  : int = (0, 0, 255)

class Loop:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("My Game")

        self.FPS     : int = 60
        self.HEIGHT  : int = 648
        self.WIDTH   : int = 1152
        self.running : bool = True
        
        self.top : Node = None

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()
        
        self.pressed : list = [False, False, False]

    def _process(self):
        self.clock.tick(self.FPS)

        # Рендеринг
        self.screen.fill(BLACK)
        
        self._draw()

        # после отрисовки всего, переворачиваем экран
        pygame.display.flip()

        
    def _draw(self) -> None:
        current : Node = self.top
        while current is not None:
            current._draw()
            current._process()
            current = current.next
    
    def is_empty(self):
        return self.top is None
    
    def add_child(self, node) -> Node:
        node.next = self.top
        self.top = node
   
    def get_stack(self) -> list[Node]:
        array : list = []
        current : Node = self.top
        while current is not None:
            array.append(current)
            current = current.next
        return array
