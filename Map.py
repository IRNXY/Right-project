import os
import pygame

# размер карты в символах
MAP_X = 15
MAP_Y = 9
# масштаб единицы карты (клетки)
ZOOM = 60
# задаём размер окна
WIDTH = MAP_X * ZOOM
HEIGHT = MAP_Y * ZOOM

# создаём группы спрайтов
all_sprites = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()
box_sprites = pygame.sprite.Group()

class Wall(pygame.sprite.Sprite):
    # передаём координаты объекта на карте
    def __init__(self, x, y):
        # наследуем встроенный класс Sprite
        pygame.sprite.Sprite.__init__(self)
        # путь к файлу где находится программа
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        # загружаем картинку стены
        self.image = pygame.image.load(os.path.join(img_folder, 'wall.jpg')).convert()
        self.rect = self.image.get_rect()
        # указываем координаты верхнкго левого угла
        self.rect.topleft = (x, y)

    def update(self):
        pass

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

    def update(self):
        pass

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

        self.open_file(file_name)
        self.sprites_map()

    # отрисовка спрайтов на карте
    def sprites_map(self):
        for y in range(MAP_Y):
            for x in range(MAP_X):
                # print(x, y, self.string[y + MAP_Y * self.room_y][x + MAP_X * self.room_x])
                if self.string[y + MAP_Y * self.room_y][x + MAP_X * self.room_x] == '#':
                    # предаём координаты объекта с учётом сдвига по комнатам
                    wall = Wall(ZOOM * x, ZOOM * y)
                    # добовляем объект Wall к списку спрайтов стен
                    wall_sprites.add(wall)
                    # добовляем объект Wall к общему списку всех спрайтов
                    all_sprites.add(wall)
                elif self.string[y + MAP_Y * self.room_y][x + MAP_X * self.room_x] == '&':
                    # предаём координаты объекта с учётом сдвига по комнатам
                    box = Box(ZOOM * x, ZOOM * y)
                    # добовляем объект Box к списку спрайтов стен
                    wall_sprites.add(box)
                    # добовляем объект Box к общему списку всех спрайтов
                    all_sprites.add(box)

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