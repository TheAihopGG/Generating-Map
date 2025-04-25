import pygame


BLACK : tuple = (0, 0, 0)
WHITE : tuple = (255, 255, 255)
RED   : tuple = (255, 0, 0)
BLUE  : tuple = (0, 0, 255)


class Node:
    def __init__(self) -> None:
        pass

class Node2D(Node):
    def __init__(self, screen, x : int = 0, y : float = 0, scale : float = 1.0) -> None:
        self.screen = screen
        self.next = None
        self.x : float = x
        self.y : float = y
        self.scale : float = scale

    def draw() -> None:
        pass

    def _process(self) -> None:
        pass



# Фигуры

class Shapes(Node2D):
    def __init__(self, screen, x = 0, y = 0, scale = 1):
        super().__init__(screen, x, y, scale)
        self.size : float = 10 * self.scale
        self.color : tuple = WHITE
        self.contour_thickness : int = 0
        
class Square(Shapes):    
    def __init__(self, screen, x = 0, y = 0, scale = 1):
        super().__init__(screen, x, y, scale)
        self.border_radius = 0
        
    def draw(self) -> None:
        pygame.draw.rect(
            self.screen, self.color, 
            (float(self.x), float(self.y), self.size * self.scale, self.size * self.scale), 
            self.contour_thickness, self.border_radius)

class Circle(Shapes):
    def draw(self) -> None:
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.size * self.scale, self.contour_thickness)

class Triangle(Shapes):
    def draw(self) -> None:
        height = ((3 ** 0.5) / 2) * (self.size * self.scale)  # Высота треугольника
        self.points = [
            (self.x, self.y - height * 2/3),  # Верхняя вершина
            (self.x - (self.size * self.scale) / 2, self.y + height / 3),  # Левая нижняя
            (self.x + (self.size * self.scale) / 2, self.y + height / 3)  # Правая нижняя
        ]
        if not self.contour_thickness:
            pygame.draw.polygon(self.screen, self.color, self.points)
        pygame.draw.aalines(self.screen, self.color, True, self.points)


# Картинки

class Sprite(pygame.sprite.Sprite, Node2D):
    def __init__(self, image_path, screen, x : float = 0, y : float = 0, scale : float = 1.0, angle : float = 0.0):
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
        self.angle : float = angle
        self.image = pygame.transform.rotate(self.image, -self.angle)

        # Получаем прямоугольник изображения
        self.surface = self.image.get_rect()
        self.surface.x = x
        self.surface.y = y
        
    def draw(self) -> None:
        self.surface.x = self.x
        self.surface.y = self.y
        self.screen.blit(self.image, self.surface)