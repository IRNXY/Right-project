import pygame

status_game = 'screen'


# размер карты в символах
MAP_X = 15
MAP_Y = 9
# масштаб единицы карты (клетки)
ZOOM = 60
# задаём размер окна
WIDTH = MAP_X * ZOOM
HEIGHT = MAP_Y * ZOOM
screen = pygame.display.set_mode((WIDTH, HEIGHT))


# создаём группы спрайтов
all_sprites = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()
box_sprites = pygame.sprite.Group()
mobs_sprites = pygame.sprite.Group()
swords_sprites = pygame.sprite.Group()
explosion_sprites = pygame.sprite.Group()
coins_sprites = pygame.sprite.Group()