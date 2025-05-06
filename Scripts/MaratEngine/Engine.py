import pygame
from .utils.Node import Node2D


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


class Loop:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("My Game")

        self.fps = 60
        self.height = 648
        self.width = 1152
        self.running = True
        self.bg_color = BLACK

        self.head: Node2D | None = None
        self.tail: Node2D | None = None

        self.update_screen_size(self.width, self.height)
        self.clock = pygame.time.Clock()

        self.mouse_button_pressed = [False, False, False]

    def _process(self):
        self.clock.tick(self.fps)

        # Рендеринг
        self.screen.fill(self.bg_color)

        self.draw()

        # после отрисовки всего, переворачиваем экран
        pygame.display.flip()

    def draw(self) -> None:
        current: Node2D | None = self.head
        while current is not None:
            current.draw()
            current._process()
            current = current.next

    def is_empty(self):
        return not self.tail

    def add_child(self, node: Node2D) -> Node2D:

        # Если стэк пуст
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            if self.tail:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            else:
                assert self.tail

        return node

    def remove_child(self, node: Node2D) -> None:
        prev_node: Node2D = node.prev
        next_node: Node2D = node.next

        if node == self.head:
            self.head = next_node

        if node == self.tail:
            self.tail = prev_node

        # 1 -> (2) -> 3
        if prev_node:
            # 1 -> 3
            prev_node.next = next_node
        if next_node:
            # 1 <- 3
            next_node.prev = prev_node

    def get_stack(self) -> list[Node2D]:
        array: list[Node2D] = []
        current: Node2D | None = self.head
        while current is not None:
            array.append(current)
            current = current.next
        return array

    def __str__(self) -> str:
        """Выводит стек в виде строки (для наглядности)"""
        elements: list[str] = []
        current: Node2D | None = self.head
        while current is not None:
            elements.append(str(current))
            current = current.next

        return " -> ".join(reversed(elements)) if elements else "Пустой стек"

    def update_screen_size(self, width: int, height: int) -> None:
        self.height = height
        self.width = width
        self.screen = pygame.display.set_mode((self.width, self.height))
