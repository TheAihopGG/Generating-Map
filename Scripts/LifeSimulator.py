import pygame
from math import sqrt
from random import random
from MaratEngine.Engine import *
from MaratEngine.utils.Node import *


class Game(Loop):
    def __init__(self) -> None:
        super().__init__()
        pygame.display.set_caption("Evolution")
        self.update_screen_size(600, 600)

        self.yellow_group : list = self.add_group(100, YELLOW)
        self.red_group : list = self.add_group(100, RED)
        self.green_group : list = self.add_group(100, GREEN)
        self.blue_group : list = self.add_group(100, BLUE)

        self.groups : list[list] = [self.yellow_group, self.red_group, self.green_group, self.blue_group]

        self.actions : list = [(random() - 0.5) * 2 for i in range(self.groups.__len__() ** 2)]
        print(" > Значения притяжения для рандома: ", self.actions)

    def _process(self) -> None:
        while self.running:
            for event in pygame.event.get():    
                if event.type == pygame.QUIT: 
                    self.running = False
            
            super()._process()
            
            self.rule_random()
        
        pygame.quit()

    def rule_random(self):
        for i, group1 in enumerate(self.groups):
            for j, group2 in enumerate(self.groups):
                self.apply_rules(group1, group2, self.actions[i * self.groups.__len__() + j])

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
            
            particle1.velocity[0] *= 0.4
            particle1.velocity[1] *= 0.4

            # ускорение скорости
            particle1.velocity[0] += velocity_x
            particle1.velocity[1] += velocity_y 
            


class Particle(Square):
    def __init__(self, screen, x = 0, y = 0, scale = 1):
        super().__init__(screen, x, y, scale)
        self.velocity : list = [0.0, 0.0]
        self.contour_thickness = 1
        self.scale = 0.8

        self.border_radius = 2 # Только для Square

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