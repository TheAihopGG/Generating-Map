import pygame


BLACK : tuple = (0, 0, 0)
WHITE : tuple = (255, 255, 255)
RED   : tuple = (255, 0, 0)
BLUE  : tuple = (0, 0, 255)


class Node2D:
    def __init__(self, screen, x : int = 0, y : int = 0, scale : int = 1.0) -> None:
        self.screen = screen
        self.next = None
        self.x : int = x
        self.y : int = y
        self.color : tuple = BLACK
        self.size : float = scale
        self.scale : float = scale
        self.angle : float = 0
        self.image : pygame.Surface = pygame.Surface((self.size * self.scale, self.size * self.scale), pygame.SRCALPHA, 32)
        self.rect : pygame.Rect = pygame.Rect(self.x, self.y, self.size * self.scale, self.size * self.scale)
        
    def draw(self) -> None:
        self.screen.blit(self.image, (self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y, self.size * self.scale, self.size * self.scale)

    def _process(self) -> None:
        pass
    
    def update_data(self) -> None:
        self.image = pygame.Surface((self.size * self.scale, self.size * self.scale), pygame.SRCALPHA, 32)

        
# Фигуры
class Shape(pygame.sprite.Sprite, Node2D):
    def __init__(self, screen, x = 0, y = 0, scale = 1):
        pygame.sprite.Sprite.__init__(self)  # Инициализация спрайта
        Node2D.__init__(self, screen, x, y, scale)  # Инициализация Node2D
        self.contour_thickness : int = 0 # заполнить фигуруs
        
class Square(Shape):    
    def __init__(self, screen, x=0, y=0, scale=1):
        super().__init__(screen, x, y, scale)
        self.border_radius = 0
        
    def draw(self) -> None:
        super().draw()
        pygame.draw.rect(self.image, self.color, (0, 0, self.size * self.scale, self.size * self.scale), self.contour_thickness, self.border_radius)

class Circle(Shape):
    def draw(self) -> None:
        super().draw()
        pygame.draw.circle(self.image, self.color, (self.size * self.scale // 2, self.size * self.scale // 2), self.size * self.scale // 2, self.contour_thickness)


# Картинки
class Sprite(pygame.sprite.Sprite, Node2D):
    def __init__(self, image_path, screen, x : int = 0, y : int = 0, scale : float = 1.0):
        pygame.sprite.Sprite.__init__(self)  # Инициализация спрайта
        Node2D.__init__(self, screen, x, y, scale)  # Инициализация Node2D

        # Загружаем изображение
        self.image = pygame.image.load(image_path).convert_alpha()
        
        # Масштаб
        self.image = pygame.transform.scale(
            self.image,
            (int(self.image.get_width() * self.scale),
            int(self.image.get_height() * self.scale))
        )

        # Вращение
        self.image = pygame.transform.rotate(self.image, -self.angle)

    def draw(self) -> None:
        self.screen.blit(self.image, (self.x, self.y))
