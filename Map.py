import os
from config import *
from pygame_init import *
from Player import Player
from random import randint

# # размер карты в символах
# MAP_X = 15
# MAP_Y = 9
# # масштаб единицы карты (клетки)
# ZOOM = 60
# # задаём размер окна
# WIDTH = MAP_X * ZOOM
# HEIGHT = MAP_Y * ZOOM

class Wall(pygame.sprite.Sprite):
    # передаём координаты объекта на карте
    def __init__(self, x, y):
        # наследуем встроенный класс Sprite
        pygame.sprite.Sprite.__init__(self)
        # путь к файлу где находится программа
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        # загружаем картинку стены
        self.image = pygame.image.load(
            os.path.join(img_folder, 'wall.jpg')).convert()
        self.rect = self.image.get_rect()
        # указываем координаты верхнкго левого угла
        self.rect.topleft = (x, y)

    def update(self):
        pass



def draw_shield_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    GREEN = (0, 255, 0)
    WHITE = (255, 255, 255)
    fill = (pct / 10) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        # загружаем картинку монетки
        self.image = pygame.image.load(
            os.path.join(img_folder, 'Coin.png')).convert()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.image.set_colorkey(pygame.Color('white'))
        self.rect = self.image.get_rect()
        self.rect.topright = (x, y)

    def update(self):
        pass

lg = []
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
img1 = pygame.image.load(os.path.join(img_folder, 'monster.png'))
img2 = pygame.transform.scale(img1, (80, 80))

# player_img = pygame.image.load(os.path.join(img_folder, 'images.jpg')).convert()
for i in range(9):
    filename = 'explosion0{}.png'.format(i)
    # img = pygame.image.load(os.path.join(img_folder, filename)).convert()
    img = pygame.image.load(os.path.join(img_folder, filename))
    img.set_colorkey(pygame.Color('black'))
    img_lg = pygame.transform.scale(img, (90, 90))
    lg.append(img_lg)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.image = lg[self.frame]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            # print(self.frame, len(lg))
            if self.frame == len(lg):
                self.kill()
                self.image = img2

            else:
                center = self.rect.center
                self.image = lg[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


class Map:
    # передаём имя файла с txt картой, координаты комнаты по х и по у
    def __init__(self, file_name, room_x, room_y):
        # наследуем встроенный класс Sprite
        pygame.sprite.Sprite.__init__(self)
        # список для хранения txt карты
        self.string = []
        self.room_x = room_x
        self.room_y = room_y


        # значение символов карты
        self.symbols = {
            '@': 'player',
            '#': 'wall',
            '.': 'cell',
            '&': 'box',
            'x': 'monster',
            ' ': 'nothing'
        }
        # картинки
        self.tile_images = {
            'wall': 'wall.jpg',
            'cell': 'cell.jpg',
            'box': 'box.jpg',
            'monster': 'monster.jpg',
            'player': 'images.jpg',
            'nothing': 'nothing.jpg'
        }

        # self.start_screen()
        self.open_file(file_name)
        self.sprites_map()
        # self.sprite_player(5, 7)
        self.player = Player(5, 7)
        all_sprites.add(self.player)
        print('>>>>>>>>>>', self.player)


    # отрисовка спрайтов на карте
    def sprites_map(self):
        for y in range(MAP_Y):
            for x in range(MAP_X):
                # print(x, y, self.string[y + MAP_Y * self.room_y][x + MAP_X * self.room_x])
                if self.string[y + MAP_Y * self.room_y][
                    x + MAP_X * self.room_x] == '#':
                    # предаём координаты объекта с учётом сдвига по комнатам
                    self.wall = Wall(ZOOM * x, ZOOM * y)
                    # добовляем объект Wall к списку спрайтов стен
                    wall_sprites.add(self.wall)
                    # добовляем объект Wall к общему списку всех спрайтов
                    all_sprites.add(self.wall)

                if self.string[y + MAP_Y * self.room_y][
                    x + MAP_X * self.room_x] == '&':
                    # предаём координаты объекта с учётом сдвига по комнатам
                    self.box = Box(ZOOM * x, ZOOM * y)
                    # добовляем объект Box к списку спрайтов стен
                    box_sprites.add(self.box)
                    # добовляем объект Box к общему списку всех спрайтов
                    all_sprites.add(self.box)

                if self.string[y + MAP_Y * self.room_y][
                    x + MAP_X * self.room_x] == 'c':
                    # предаём координаты объекта с учётом сдвига по комнатам
                    self.coin = Coin(ZOOM * x, ZOOM * y)
                    # добовляем объект Box к списку спрайтов стен
                    coins_sprites.add(self.coin)
                    # добовляем объект Box к общему списку всех спрайтов
                    all_sprites.add(self.coin)

                # if self.string[y + MAP_Y * self.room_y][
                #     x + MAP_X * self.room_x] == 'x':
                #     self.enemy = Move_Enemy(y + MAP_Y * self.room_y, x + MAP_X * self.room_x)
                #     all_sprites.add(self.enemy)
                #     mobs_sprites.add(self.enemy)


                # if self.string[y + MAP_Y * self.room_y][
                #     x + MAP_X * self.room_x] == '@':
                #     self.plaer = Play_plaer(y + MAP_Y * self.room_y, x + MAP_X * self.room_x)
                #     all_sprites.add(self.plaer)


    # def sprite_ghost(self, x, y):
    #     ghost = Ghost(self.cord_pl(), x, y)
    #     all_sprites.add(ghost)


    def cord_pl(self):
        return [self.player.rect.x // ZOOM, self.player.rect.y // ZOOM]


    # читаем файл с txt картой
    def open_file(self, filename):
        count = -1
        with open(filename, 'r') as mapFile:
            string1 = [line.strip('\n') for line in mapFile]
            for line in string1:
                self.string.append([])
                count += 1
                for i in line:
                    self.string[count].append(i)

    def change_map(self, x, y):
        all_sprites.remove()
        wall_sprites.remove()
        box_sprites.remove()
        mobs_sprites.remove()
        swords_sprites.remove()
        explosion_sprites.remove()
        coins_sprites.remove()

        if x < 0 < y:
            Map(file_name='1.txt', room_x=0, room_y=1)

        elif x > 0 < y:
            Map(file_name='1.txt', room_x=2, room_y=1)

        elif x < 0 > y:
            Map(file_name='1.txt', room_x=1, room_y=2)

        elif x > 0 < y:
            Mapp = Map(file_name='1.txt', room_x=0, room_y=1)

class Box(pygame.sprite.Sprite):
    # передаём координаты объекта на карте
    def __init__(self, x, y):
        # наследуем встроенный класс Sprite
        pygame.sprite.Sprite.__init__(self)
        # путь к файлу где находится программа
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        # загружаем картинку ящика
        self.image = pygame.image.load(
            os.path.join(img_folder, 'Box.jpg')).convert()
        self.rect = self.image.get_rect()
        # указываем координаты верхнкго левого угла
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y

    def update(self):
        pass

class Game_over(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        game_over = pygame.image.load(
            os.path.join(img_folder, 'fon_better.jpg'))
        game_over = pygame.transform.scale(game_over,
                                           (MAP_X * ZOOM, MAP_Y * ZOOM))
        # self.rect = self.image.get_rect()
        # self.rect.center = center

    def update(self):
        pass
