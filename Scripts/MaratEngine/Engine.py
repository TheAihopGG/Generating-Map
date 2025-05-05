import pygame
from .utils.Node import Node2D


BLACK  : tuple = (0, 0, 0)
WHITE  : tuple = (255, 255, 255)
RED    : tuple = (255, 0, 0)
BLUE   : tuple = (0, 0, 255)
YELLOW : tuple = (255, 255, 0)
GREEN  : tuple = (0, 255, 0)

class Loop:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("My Game")

        self.FPS      : int = 60
        self.HEIGHT   : int = 648
        self.WIDTH    : int = 1152
        self.running  : bool = True
        self.BG_COLOR : tuple = BLACK

        self.head : Node2D = None
        self.tail : Node2D = None

        self.update_screen_size(self.WIDTH, self.HEIGHT)
        self.clock = pygame.time.Clock()
        
        self.mouse_button_pressed : list = [False, False, False]

    def _process(self):
        self.clock.tick(self.FPS)

        # Рендеринг
        self.screen.fill(self.BG_COLOR)
        
        self.draw()

        # после отрисовки всего, переворачиваем экран
        pygame.display.flip()

        
    def draw(self) -> None:
        current : Node2D = self.head
        while current is not None:
            current.draw()
            current._process()
            current = current.next

    def is_empty(self):
        return self.tail is None
    
    def add_child(self, node : Node2D) -> Node2D:

        # Если стэк пуст
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        return node
   
    def remove_child(self, node : Node2D) -> None:
        prev_node : Node2D = node.prev
        next_node : Node2D = node.next

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
        array : list = []
        current : Node2D = self.head
        while current is not None:
            array.append(current)
            current = current.next
        return array

    def __str__(self) -> str:
        """Выводит стек в виде строки (для наглядности)"""
        elements : list[Node2D] = []
        current : Node2D = self.head
        while current is not None:
            elements.append(str(current))
            current = current.next

        return " -> ".join(reversed(elements)) if elements else "Пустой стек"

    def update_screen_size(self, width : int, height : int) -> None:
        self.HEIGHT : int = height
        self.WIDTH  : int = width
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))