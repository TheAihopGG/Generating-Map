import pygame
from random import random
from math import sqrt
from MaratEngine.Engine import *
from MaratEngine.utils.Node import *


class Game(Loop):
    def __init__(self) -> None:
        super().__init__()
        pygame.display.set_caption("Evolution")
        self.update_screen_size(600, 600)

        self.yellow_group : list = self.add_group(150, YELLOW)
        self.red_group : list = self.add_group(150, RED)
        self.green_group : list = self.add_group(150, GREEN)

        self.actions : list = [(random() - 0.5)*2 for i in range(9)]
        print(self.actions)        

    def _process(self) -> None:
        while self.running:
            for event in pygame.event.get():    
                if event.type == pygame.QUIT: 
                    self.running = False
            
            super()._process()
            
            self.rule_bird()
        
        pygame.quit()

    def rule_random(self):
        # Взаимодействие зелёных
        self.apply_rules(self.green_group, self.green_group, self.actions[0])
        self.apply_rules(self.green_group, self.red_group, self.actions[1])
        self.apply_rules(self.green_group, self.yellow_group, self.actions[2])

        # Взаимодействие красных
        self.apply_rules(self.red_group, self.red_group, self.actions[3])
        self.apply_rules(self.red_group, self.yellow_group, self.actions[4])
        self.apply_rules(self.red_group, self.green_group, self.actions[5])

        # Взаимодействие жёлтых
        self.apply_rules(self.yellow_group, self.yellow_group, self.actions[6])
        self.apply_rules(self.yellow_group, self.green_group, self.actions[7])
        self.apply_rules(self.yellow_group, self.red_group, self.actions[8])

    def rule_bird(self) -> None:
        self.apply_rules(self.green_group, self.green_group, -0.32)
        self.apply_rules(self.green_group, self.red_group, -0.17)
        self.apply_rules(self.green_group, self.yellow_group, 0.34)

        self.apply_rules(self.red_group, self.red_group, -0.1)
        self.apply_rules(self.red_group, self.green_group, -0.34)

        self.apply_rules(self.yellow_group, self.yellow_group, 0.15)
        self.apply_rules(self.yellow_group, self.green_group, -0.2)

    def rule_bounds(self) -> None:
        self.apply_rules(self.yellow_group, self.yellow_group, -0.2)
        self.apply_rules(self.green_group, self.yellow_group, -0.6)
        self.apply_rules(self.red_group, self.green_group, -0.2)

    def add_group(self, score, color) -> list[Node]:
        group : list = []
        for i in range(score):
            new_particle : Particle = Particle(self.screen, self.random_pos(), self.random_pos())
            new_particle.color = color
            self.add_child(new_particle)

            group.append(new_particle)
        return group

    
    def random_pos(self) -> int:
        return random() * (self.WIDTH - 100) + 50 

    def apply_rules(self, group1 : list, group2 : list, g : float) -> None:
        for particle1 in group1:
            # сила притяжения
            velocity_x, velocity_y = 0, 0
            
            for particle2 in group2:
                if particle1 == particle2:
                    continue

                # векторы - стороны
                dx : float = particle1.x - particle2.x
                dy : float = particle1.y - particle2.y

                # вычисляем их гиаптинузу
                dist_sq : float = sqrt(dx * dx + dy * dy)

                if 0 < dist_sq < 80:
                    # сила притяяжения
                    f : float = g / dist_sq
                    
                    # прибавляем притяжение к 2 измерениям
                    velocity_x += f * dx
                    velocity_y += f * dy

            # движение
            particle1.x += particle1.velocity[0]
            particle1.y += particle1.velocity[1]
            
            particle1.velocity[0] *= 0.5
            particle1.velocity[1] *= 0.5

            # ускорение скорости
            particle1.velocity[0] += velocity_x
            particle1.velocity[1] += velocity_y 
            


class Particle(Triangle):
    def __init__(self, screen, x = 0, y = 0, scale = 1):
        super().__init__(screen, x, y, scale)
        self.velocity : list = [0.0, 0.0]
        # self.contour_thickness = 1
        self.border_radius = 2
        self.scale = 2

    def _process(self) -> None:
        if self.x < 0 or self.x > game.WIDTH:
            self.velocity[0] *= -0.5
            self.x = max(0, min(game.WIDTH, self.x))

        if self.y < 0 or self.y > game.HEIGHT:
            self.velocity[1] *= -0.5
            self.y = max(0, min(game.HEIGHT, self.y))

if __name__ == "__main__":
    game : Game = Game()
    game._process()