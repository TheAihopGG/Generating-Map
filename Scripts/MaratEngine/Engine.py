import pygame
from MaratEngine.utils.Node import *


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

        self.top : Node = None


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
        current : Node = self.top
        while current is not None:
            current.draw()
            current._process()
            current = current.next

    def is_empty(self):
        return self.top is None
    
    def add_child(self, node : Node) -> Node:
        node.next = self.top
        self.top = node
   
    def remove_child(self, node : Node) -> bool:
        if self.is_empty():
            return False # Элемент не найден (стек пуст)
        
        if self.top == node:
            self.top = self.top.next  
            return True  # Элемент найден (элемент самый последний)
        
        current = self.top
        while current.next is not None:
            if current.next == node:
                # "Вырезаем" элемент из связного списка
                current.next = current.next.next  
                return True # Элемент найден (нашли)
            current = current.next
        
        return False  # Элемент не найден (такого нет)

    def get_stack(self) -> list[Node]:
        array : list = []
        current : Node = self.top
        while current is not None:
            array.append(current)
            current = current.next
        return array

    def __str__(self) -> str:
        """Выводит стек в виде строки (для наглядности)"""
        elements : list[Node] = []
        current : Node = self.top
        while current is not None:
            elements.append(str(current))
            current = current.next

        return " -> ".join(reversed(elements)) if elements else "Пустой стек"

    def update_screen_size(self, width : int, height : int) -> None:
        self.HEIGHT : int = height
        self.WIDTH  : int = width
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))