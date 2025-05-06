from __future__ import annotations
import pygame
import os


BLACK: tuple = (0, 0, 0)
WHITE: tuple = (255, 255, 255)
RED: tuple = (255, 0, 0)
BLUE: tuple = (0, 0, 255)


class Node2D:
    def __init__(
        self,
        screen: pygame.Surface,
        x=0,
        y=0,
        size=1,
    ) -> None:
        self.screen = screen
        self.prev: Node2D | None = None
        self.next: Node2D | None = None
        self.x: int = x
        self.y: int = y
        self.color: tuple = BLACK
        self.size: int = size

    def draw(self) -> None:
        pass

    def _process(self) -> None:
        pass


# Фигуры
class Shape(Node2D):
    def __init__(
        self,
        screen,
        x=0,
        y=0,
        size=1,
    ) -> None:
        Node2D.__init__(
            self,
            screen=screen,
            x=x,
            y=y,
            size=size,
        )  # Инициализация Node2D
        self.contour_thickness: int = 0  # заполнить фигуруs


class Square(Shape):
    def __init__(
        self,
        screen,
        x=0,
        y=0,
        size=1,
    ) -> None:
        super().__init__(screen, x, y, size)
        self.border_radius = 0

    def draw(self) -> None:
        pygame.draw.rect(
            self.screen,
            self.color,
            (
                self.x,
                self.y,
                self.size,
                self.size,
            ),
            self.contour_thickness,
            self.border_radius,
        )


class Circle(Shape):
    def draw(self) -> None:
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.size // 2,
            self.contour_thickness,
        )


# Текст
class Label(Node2D):
    def __init__(
        self,
        screen: pygame.Surface,
        text="",
        x=0,
        y=0,
        size=1,
    ):
        super().__init__(screen=screen, x=x, y=y, size=size)
        self.font = pygame.font.Font(None, size)
        self.text: str = text

    def _process(self) -> None:
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(topleft=(self.x, self.y))
        self.screen.blit(text_surface, text_rect)


# Картинки
class Sprite(pygame.sprite.Sprite, Node2D):
    def __init__(
        self,
        screen: pygame.Surface,
        image_path: str,
        x=0,
        y=0,
        size=1.0,
    ):
        pygame.sprite.Sprite.__init__(self)  # Инициализация спрайта
        Node2D.__init__(self, screen, x, y, size)  # Инициализация Node2D
        # Загружаем изображение
        self.image = pygame.image.load(image_path).convert_alpha()

        # Масштаб
        self.image = pygame.transform.scale(
            self.image,
            (
                int(self.image.get_width() * self.size),
                int(self.image.get_height() * self.size),
            ),
        )

        # Вращение
        self.angle = 0.0
        self.image = pygame.transform.rotate(self.image, -self.angle)

    def draw(self) -> None:
        self.screen.blit(self.image, (self.x, self.y))
