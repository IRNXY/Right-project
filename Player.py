import pygame
import random
from config import *
import os
#
# WIDTH = 480
# HEIGHT = 600
# FPS = 60

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# # Создаем игру и окно
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# clock = pygame.time.Clock()
#


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        game_folder = os.path.dirname(__file__)
        self.img_folder = os.path.join(game_folder, 'img')
        self.images = [[], []]
        self.picture_frame = 8
        self.direction_frame = 0
        # загружаем картинки
        for i in range(9):
            filenameL = '2D_KNIGHT__Attack_L_00{}.png'.format(i)
            filenameR = '2D_KNIGHT__Attack_R_00{}.png'.format(i)
            self.images[0].append(pygame.image.load(os.path.join(self.img_folder, filenameL)).convert())
            self.images[1].append(pygame.image.load(os.path.join(self.img_folder, filenameR)).convert())

        self.image = self.images[self.direction_frame][self.picture_frame]
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.image.set_colorkey(pygame.Color('white'))
        # self.image = pygame.Surface((50, 40))
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.centerx = x * ZOOM
        self.rect.bottom = y * ZOOM
        # self.rect.centerx = x * ZOOM + ZOOM // 2
        # self.rect.bottom = y * ZOOM + ZOOM // 2
        self.speedx = 0
        self.speedy = 0
        self.direction = 'left'


    def update(self):
        if self.picture_frame < 8:
            self.picture_frame += 1
            self.image = self.images[self.direction_frame][self.picture_frame]
            self.image = pygame.transform.scale(self.image, (80, 80))

        self.speedx = 0
        self.speedy = 0
        keyboard = pygame.key.get_pressed()
        if keyboard[pygame.K_a]:
            self.direction_frame = 0
            self.image = self.images[self.direction_frame][self.picture_frame]
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.speedx = -2
        if keyboard[pygame.K_d]:
            self.direction_frame = 1
            self.image = self.images[self.direction_frame][self.picture_frame]
            self.image = pygame.transform.scale(self.image, (80, 80))
            self.speedx = 2
        if keyboard[pygame.K_s]:
            self.speedy = 2
        if keyboard[pygame.K_w]:
            self.speedy = -2
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        hits = pygame.sprite.spritecollide(self, wall_sprites, False)
        hits2 = pygame.sprite.spritecollide(self, box_sprites, False)
        if hits or hits2:
            self.rect.x -= self.speedx
            self.rect.y -= self.speedy

        keyboard = pygame.key.get_pressed()
        if keyboard[pygame.K_q]:
            self.picture_frame = -1

