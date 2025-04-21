import pygame


BLACK : int = (0, 0, 0)
WHITE : int = (255, 255, 255)
RED   : int = (255, 0, 0)
BLUE  : int = (0, 0, 255)

class Node:
    def __init__(self, screen, x : int = 0, y : float = 0, scale : float = 1.0) -> None:
        self.screen = screen
        self.next = None
        self.x : int = x
        self.y : int = y

    def _draw() -> None:
        pass

    def _process(self) -> None:
        pass


class Shapes(Node):
    def __init__(self, screen, x = 0, y = 0, scale = 1):
        super().__init__(screen, x, y, scale)
        self.size : float = 10 * scale
        self.color : tuple = WHITE
        
class Square(Shapes):
    def _draw(self) -> None:
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.size, self.size))

class Circle(Shapes):    
    def _draw(self) -> None:
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size)


class Sprite(pygame.sprite.Sprite, Node):
    def __init__(self, image_path, screen, x : int = 0, y : float = 0, scale : float = 1.0):
        pygame.sprite.Sprite.__init__(self)  # Инициализация спрайта
        Node.__init__(self, screen, x, y, scale)  # Инициализация Node

        # Загружаем изображение
        self.image = pygame.image.load(image_path).convert_alpha()
        
        # Масштаб
        self.image = pygame.transform.scale(
            self.image,
            (int(self.image.get_width() * scale),
            int(self.image.get_height() * scale))
        )

        # Получаем прямоугольник изображения
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def _draw(self) -> None:
        self.screen.blit(self.image, self.rect)