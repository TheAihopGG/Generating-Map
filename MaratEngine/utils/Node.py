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

class Cubic(Node):
    def _draw(self) -> None:
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.size, self.size))


class Ball(Node):    
    def __init__(self, screen, x = 0, y = 0, color = RED, size = 10):
        super().__init__(screen, x, y, color, size)
        self.vec = [1, 1]

    def _draw(self) -> None:
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size)

    def _process(self) -> None:
        self.ping_pong_XD()
    
    def ping_pong_XD(self) -> None:
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
