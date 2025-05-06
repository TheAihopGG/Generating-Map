from __future__ import annotations
import pygame
from typing import Final
from math import sqrt
from random import random
from MaratEngine.Engine import *
from MaratEngine.utils.Node import *


class Game(Loop):
    def __init__(self) -> None:
        super().__init__()
        pygame.display.set_caption("Evolution")
        self.update_screen_size(600, 600)

        self.FORCE: Final = 0.5
        self.SIZE_PARTICLE: Final = 4
        LEN_PARTICLES: Final = 100

        self.yellow_group: list = self.add_group(LEN_PARTICLES, YELLOW)
        self.red_group: list = self.add_group(LEN_PARTICLES, RED)
        self.green_group: list = self.add_group(LEN_PARTICLES, GREEN)
        self.blue_group: list = self.add_group(LEN_PARTICLES, BLUE)
        self.white_group: list = self.add_group(LEN_PARTICLES, WHITE)

        self.groups: list[list] = [
            self.yellow_group,
            self.red_group,
            self.green_group,
            self.blue_group,
            self.white_group,
        ]

        self.actions: list = [random() * 2 - 1 for _ in range(len(self.groups) ** 2)]
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
                self.apply_rules(
                    group1,
                    group2,
                    self.actions[i * self.groups.__len__() + j],
                )

    def rule_bird(self) -> None:
        self.apply_rules(
            self.green_group,
            self.green_group,
            -0.32,
        )
        self.apply_rules(
            self.green_group,
            self.red_group,
            -0.17,
        )
        self.apply_rules(
            self.green_group,
            self.yellow_group,
            0.34,
        )

        self.apply_rules(
            self.red_group,
            self.red_group,
            -0.1,
        )
        self.apply_rules(
            self.red_group,
            self.green_group,
            -0.34,
        )

        self.apply_rules(
            self.yellow_group,
            self.yellow_group,
            0.15,
        )
        self.apply_rules(
            self.yellow_group,
            self.green_group,
            -0.2,
        )

    def rule_bounds(self) -> None:
        self.apply_rules(
            self.yellow_group,
            self.yellow_group,
            -0.2,
        )
        self.apply_rules(
            self.green_group,
            self.yellow_group,
            -0.6,
        )
        self.apply_rules(
            self.red_group,
            self.green_group,
            -0.2,
        )

    def add_group(self, score: int, color: tuple[int, int, int]) -> list[Particle]:
        group: list[Particle] = []

        for i in range(score):
            new_particle: Particle = Particle(
                self.screen,
                self.random_pos(),
                self.random_pos(),
                self.SIZE_PARTICLE,
            )
            new_particle.color = color
            self.add_child(new_particle)
            group.append(new_particle)

        return group

    def random_pos(self) -> float:
        return random() * (self.width - 100) + 50

    def apply_rules(
        self,
        group1: list[Particle],
        group2: list[Particle],
        g: float,
    ) -> None:
        for particle1 in group1:
            # сила притяжения
            velocity = [0.0, 0.0]

            for particle2 in group2:
                if particle1 == particle2:
                    continue

                # векторы - стороны
                dx: int = particle1.x - particle2.x
                dy: int = particle1.y - particle2.y

                # вычисляем их гиаптинузу
                dist_sq: float = sqrt(dx * dx + dy * dy)

                if 0 < dist_sq < 80:
                    # сила притяжения
                    f: float = g / dist_sq

                    # прибавляем притяжение к 2 измерениям
                    velocity[0] += f * dx
                    velocity[1] += f * dy

            # движение
            particle1.x += (particle1.velocity[0] + velocity[0]) * self.FORCE
            particle1.y += (particle1.velocity[1] + velocity[1]) * self.FORCE


class Particle(Square):
    def __init__(self, screen, x=0, y=0, scale=1) -> None:
        super().__init__(screen, x, y, scale)
        self.velocity: list = [0.0, 0.0]

    def _process(self) -> None:
        if self.x < 0 or self.x > game.width:
            self.x = max(0, min(game.width - self.size, self.x))

        if self.y < 0 or self.y > game.height:
            self.y = max(0, min(game.height - self.size, self.y))


if __name__ == "__main__":
    game = Game()
    game._process()
