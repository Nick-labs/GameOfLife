import pygame
from pygame import K_SPACE
import numpy as np

from settings import *


class App:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Game of Life')
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.board = Board(self.screen, 64, 48)

    def run(self):
        running = True
        pause = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                pygame.mouse.get_pos()

                keys = pygame.key.get_pressed()
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                    self.board.change_state(*pygame.mouse.get_pos())

                if event.type == pygame.KEYDOWN and keys[K_SPACE]:
                    pause = not pause

            if not pause:
                self.board.do_step()

            self.screen.fill(WHITE)
            self.board.draw()

            pygame.display.update()
            self.clock.tick(FPS)


class Board:
    def __init__(self, screen, w, h):
        self.w = w
        self.h = h
        self.screen = screen
        self.width, self.height = screen.get_size()
        self.step = min(self.width // self.w, self.height // self.h)
        self.arr = np.zeros((h, w))

    def draw(self):
        for y in range(self.h):
            for x in range(self.w):
                if self.arr[y, x]:
                    pygame.draw.rect(self.screen, GREEN, (x * self.step, y * self.step, self.step, self.step))

        for x in range(1, self.w):
            pygame.draw.line(self.screen, BLACK, (x * self.step, 0), (x * self.step, self.height))

        for y in range(1, self.h):
            pygame.draw.line(self.screen, BLACK, (0, y * self.step), (self.width, y * self.step))

    def change_state(self, x, y):
        nx = x // self.step
        ny = y // self.step
        self.arr[ny, nx] = 0 if self.arr[ny, nx] else 1

    def get_arr(self):
        return self.arr

    def do_step(self):
        f_arr = self.arr.copy()
        self.arr = (np.roll(self.arr, 1) + np.roll(self.arr, -1) +
                    np.roll(self.arr, 1, axis=0) + np.roll(self.arr, -1, axis=0) +
                    np.roll(np.roll(self.arr, 1, axis=0), 1) + np.roll(np.roll(self.arr, -1, axis=0), 1) +
                    np.roll(np.roll(self.arr, 1, axis=0), -1) + np.roll(np.roll(self.arr, -1, axis=0), -1))

        for i in range(self.arr.shape[1]):
            for j in range(self.arr.shape[0]):
                if self.arr[j, i] == born_if:
                    self.arr[j, i] = 1
                elif self.arr[j, i] == still_alive_if and f_arr[j, i] == 1:
                    self.arr[j, i] = 1
                else:
                    self.arr[j, i] = 0


if __name__ == '__main__':
    app = App()
    app.run()

# shift
# roll
