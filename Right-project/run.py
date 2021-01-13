import pygame
import os
import sys
from Map_creat import *
from Player import *
from Explosion_box import *
from Screen import *


FPS = 60
MAP_X = 15
MAP_Y = 9
ZOOM = 60
WIDTH = MAP_X * ZOOM
HEIGHT = MAP_Y * ZOOM

pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
pygame.display.flip()

size = width, height = 1010, 710
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
pygame.init()
sprite = pygame.sprite.Sprite()
wall_sprites = pygame.sprite.Group()
box_sprites = pygame.sprite.Group()


def load_image(name, colorkey=None):
    # fullname = 'C:\\Users\\72556\\PycharmProjects\\pygame\\data\\' + name
    fullname = 'C:\\Users\\123\\Desktop\\minecraft\\Minecraft Tools Version 1.8\\Minecraft Tools\\minecraftPythonAPI\\data\\' + name
    # fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


# в этой функции я сам не всё понимаю, поэтому не могу тебе объяснить
# очень важно чтобы ты указала правильный путь к файлу
def start_screen():
    runing = True
    play = [200, 200, 190, 50]
    discr = [430, 200, 190, 50]
    intro_text = ["                                                                     ЗАСТАВКА"]
    fon = pygame.transform.scale(load_image('fon_better.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color("black"))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)
    pygame.draw.rect(screen, (0, 30, 160), (play[0], play[1], play[2], play[3]))
    pygame.draw.rect(screen, (0, 30, 160), (discr[0], discr[1], discr[2], discr[3]))
    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play[0] <= event.pos[0] and play[0] + play[2] >= event.pos[0] and \
                        play[1] <= event.pos[1] and play[1] + play[3] >= event.pos[1]:
                    runing = False

                elif discr[0] <= event.pos[0] and discr[0] + discr[2] >= event.pos[0] and \
                        discr[1] <= event.pos[1] and discr[1] + discr[3] >= event.pos[1]:
                    pass

        pygame.display.flip()
        clock.tick(60)


start_screen()

Mapp = Map('1.txt', 1, 0)
explosion_box = Explosion_Box((1000, 1000))
play_plaer = Play_plaer()
# a = [[100, 100, 1, 2], [200, 200, 1, 2], [200, 50, 1, 2]]
a = [[300, 300, 1, 2]]
for i in range(1, 2):
    exec("move_" + str(i) + "_enemy = Move_Enemy(" + str(a[i - 1]) + ")")
scr_men = Scr_men()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(pygame.Color('black'))
    all_sprites.draw(screen)
    in_f_v = play_plaer.update(a)
    a = []
    for i in range(1, 2):
        exec("end = move_" + str(i) + "_enemy.update(in_f_v[0], in_f_v[1], in_f_v[2])")
        a.append(end)
        if end == 1:
            run = False
    scr_men.update(move_1_enemy.lifes())
    pygame.display.update()
