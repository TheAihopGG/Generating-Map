import pygame


BLACK : int = (0, 0, 0)
WHITE : int = (255, 255, 255)
RED   : int = (255, 0, 0)
BLUE  : int = (0, 0, 255)

class Node:
    def __init__(self, screen, x : int = 0, y : float = 0, color : tuple = RED, size : float = 10) -> None:
        self.screen = screen
        self.next = None
        self.x : int = x
        self.y : int = y
        self.color : tuple = color
        self.size : float = size

    def _draw() -> None:
        pass

    def _process(self) -> None:
        pass

class Square(Node):
    def _draw(self) -> None:
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.size, self.size))


class Circle(Node):    
    def _draw(self) -> None:
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size)
        