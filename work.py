import pygame
import os

# map_x = 15
# map_y = 9
# zoom = 90
# screen_x = map_x * zoom
# screen_y = map_y * zoom
# filename = '1.txt'
# count = -1
# string = []
# room1 = 0
# room2 = 0
#
# # player = None
#
# symbols = {
#     '@': 'player',
#     '#': 'wall',
#     '.': 'cell',
#     '&': 'box',
#     'x': 'monster',
#     ' ': 'nothing'
# }
# tile_images = {
#     'wall': 'white',
#     'cell': 'green',
#     'box': 'blue',
#     'monster': 'red',
#     'player': 'red',
#     'nothing': 'black'
# }
#
# colors = ['black', 'white', 'blue', 'red']

FPS = 60
MAP_X = 15
MAP_Y = 9
ZOOM = 60
WIDTH = MAP_X * ZOOM
HEIGHT = MAP_Y * ZOOM

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
# screen.fill(pygame.Color("black"))
clock = pygame.time.Clock()
pygame.display.flip()



class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((50, 40))
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        self.image = pygame.image.load(os.path.join(img_folder, 'wall.jpg')).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        pass

class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((50, 40))
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        self.image = pygame.image.load(
            os.path.join(img_folder, 'Box.jpg')).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        pass

class Map:
    def __init__(self, file_name, room_x, room_y):
        pygame.sprite.Sprite.__init__(self)
        # self.image = player_img
        # self.rect = self.image.get_rect()
        # self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.string = []
        self.room_x = room_x
        self.room_y = room_y

        # player = None

        self.symbols = {
            '@': 'player',
            '#': 'wall',
            '.': 'cell',
            '&': 'box',
            'x': 'monster',
            ' ': 'nothing'
        }
        self.tile_images = {
            'wall': 'wall.jpg',
            'cell': 'cell.jpg',
            'box': 'box.jpg',
            'monster': 'monster.jpg',
            'player': 'images.jpg',
            'nothing': 'nothing.jpg'
        }
        self.open_file(file_name)
        # print(self.string)
        self.sprites_map()

    def sprites_map(self):
        for y in range(MAP_Y):
            for x in range(MAP_X):
                # print(x, y, self.string[y + MAP_Y * self.room_y][x + MAP_X * self.room_x])
                if self.string[y + MAP_Y * self.room_y][x + MAP_X * self.room_x] == '#':
                    wall = Wall(ZOOM * x, ZOOM * y)
                    wall_sprites.add(wall)
                    all_sprites.add(wall)
                    print('wall', x, y)
                elif self.string[y + MAP_Y * self.room_y][x + MAP_X * self.room_x] == '&':
                    box = Box(ZOOM * x, ZOOM * y)
                    wall_sprites.add(box)
                    all_sprites.add(box)

        # self.colors = ['black', 'white', 'blue', 'red']

    def open_file(self, filename):
        count = -1
        with open(filename, 'r') as mapFile:
            string1 = [line.strip('\n') for line in mapFile]
            for line in string1:
                self.string.append([])
                count += 1
                for i in line:
                    self.string[count].append(i)
        # print(string)

    # def draw(self):

        # print('1111111')
        # for x in range(MAP_X):
        #     for y in range(MAP_Y):
        #         print(x, y)
        #         if self.string[y][x] == '#':
        #             w = Wall(ZOOM * x, ZOOM * y)
                    # self.image = pygame.image.load(os.path.join(img_folder, self.symbols[self.tile_images[x + (MAP_X * self.room_x)][y + (MAP_Y * self.room_y)]]))
                    # pygame.draw.rect(screen, w.player_img,
                    #     ((ZOOM * x, ZOOM * y), (ZOOM * (x + 1), ZOOM * (y + 1))),
                    #     0))

        #     pygame.draw.line(screen, pygame.Color('red'), (x* 98, 0), (x * 98, 1078), 1)
        #     print(x, x* 98)
        #
        # pygame.draw.line(screen, pygame.Color('red'), (1469, 0), (1469, 1077), 1)
        # pygame.display.flip()

all_sprites = pygame.sprite.Group()
wall_sprites = pygame.sprite.Group()
box_sprites = pygame.sprite.Group()

Mapp = Map('1.txt', 1, 0)
# Mapp.open_file('1.txt')
# Mapp.draw()


# all_sprites.add()

running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()
    # Рендеринг
    screen.fill(pygame.Color('black'))
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
