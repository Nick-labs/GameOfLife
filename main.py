import pygame
from pygame import K_SPACE

from settings import *


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Game of Life')
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.board = Board(16, 12)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                keys = pygame.key.get_pressed()
                # if keys[K_SPACE]:
                # self.screen = pygame.display.set_mode(WINDOW_SIZE)

                self.screen.fill(BLACK)

                self.board.draw(self.screen)

                pygame.display.update()


class Board:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def draw(self, screen):
        width, height = screen.get_size()

        step = min(width // self.w, height // self.h)

        for x in range(1, self.w):
            pygame.draw.line(screen, WHITE, (x * step, 0), (x * step, height))

        for y in range(1, self.h):
            pygame.draw.line(screen, WHITE, (0, y * step), (width, y * step))


if __name__ == '__main__':
    app = App()
    app.run()
