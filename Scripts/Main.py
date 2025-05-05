import pygame
import math
import random
from MaratEngine.Engine import *
from MaratEngine.utils.Node import *


class Game(Loop):
    def __init__(self) -> None:
        super().__init__()

        self.add_child(Sprite(self.screen, "Assets/rf-fiz-ng.jpg", 0, 0, 0.8))

        self.cubic : Square = Square(self.screen, 500, 300)
        self.cubic.color = RED
        self.cubic.size = 20
        self.cubic.border_radius = 4

        self.add_child(self.cubic)

        self.TOWNS        : list[str] = ["Moscow", "Perm", "Ekaterinburg"]
        self.player_towns : list[Town] = [None] * self.TOWNS.__len__()
        self.current_town : int = 0
    
    def _process(self) -> None:
        while self.running:
            for event in pygame.event.get():    
                if event.type == pygame.QUIT: 
                    self.running = False
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        self.current_town = 0

                    if event.key == pygame.K_2:
                        self.current_town = 1
                        
                    if event.key == pygame.K_3:
                        self.current_town = 2
            
            super()._process()
            
            self._input()
        
        pygame.quit()

    def distances(self) -> None:
        for town1 in self.player_towns:
            for town2 in self.player_towns:
                if (town1 == town2) or (town1 is None) or (town2 is None):
                    continue
                
                vector = [town2.x - town1.x, town2.y - town1.y]
                distance = math.sqrt(vector[0] ** 2 + vector[1] ** 2)

                normalized_vector : list = [0, 0]
                if distance:
                    normalized_vector = [vector[0] / distance, vector[1] / distance]

                angle_rad = math.atan2(normalized_vector[0], normalized_vector[1])

                angle_deg = math.degrees(angle_rad)

                print(town1.name, town2.name, angle_deg, distance)
                
        print()


    def _input(self) -> None:
        mouse_pressed : tuple = pygame.mouse.get_pressed()
        mouse_position : tuple = pygame.mouse.get_pos()

        if self.player_towns[0]: 
            self.distances()


        SCALE : int = 2
        pos : list = [mouse_position[0] - 8 * SCALE, mouse_position[1] - 8 * SCALE]
        
        self.cubic.x = mouse_position[0] - self.cubic.size / 2
        self.cubic.y = mouse_position[1] - self.cubic.size / 2


        # Левая кнопка мыши
        if mouse_pressed[0] and not self.mouse_button_pressed[0]:
            self.mouse_button_pressed[0] = True
            
            self.player_towns[self.current_town] = Town(self.screen, self.TOWNS[self.current_town], x=pos[0], y=pos[1], size=SCALE)
            self.add_child(self.player_towns[self.current_town])

        elif not mouse_pressed[0]:
            self.mouse_button_pressed[0] = False


class Town(Sprite):
    def __init__(self, screen, name_town : str, image_path = "Assets/town.png", x = 0, y = 0, size = 1):
        super().__init__(screen, image_path, x, y, size)
        self.name = name_town
        name_town : Label = Label(self.screen, name_town, x, y + 32, 20)
        name_town.color = BLACK
        game.add_child(name_town)
    


if __name__ == "__main__":
    game : Game = Game()
    game._process()