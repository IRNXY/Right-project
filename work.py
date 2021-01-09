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
screen.fill(pygame.Color("black"))
clock = pygame.time.Clock()
pygame.display.flip()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
# player_img = pygame.image.load(os.path.join(img_folder, ))


class Map:
    def __init__(self, room1, room2):
        pygame.sprite.Sprite.__init__(self)
        # self.image = player_img
        # self.rect = self.image.get_rect()
        # self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.string = []
        self.room1 = room1
        self.room2 = room2

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

    def draw(self):

        # print('1111111')
        for x in range(MAP_X):
            for y in range(MAP_Y):
                self.image = pygame.image.load(os.path.join(img_folder, self.tile_images[self.symbols[x + MAP_X * self.room1][y + MAP_Y * self.room2]]))
                self.rect = self.image.get_rect()
                self.rect.center = (WIDTH / 2, HEIGHT / 2)
                pygame.draw.rect(screen, pygame.image.load(
                    os.path.join(img_folder, self.image),
                    ((ZOOM * x, ZOOM * y), (ZOOM * (x + 1), ZOOM * (y + 1))),
                    0))

        #     pygame.draw.line(screen, pygame.Color('red'), (x* 98, 0), (x * 98, 1078), 1)
        #     print(x, x* 98)
        #
        # pygame.draw.line(screen, pygame.Color('red'), (1469, 0), (1469, 1077), 1)
        pygame.display.flip()

Mapp = Map(1, 1)
Mapp.open_file('1.txt')
Mapp.draw()
all_sprites = pygame.sprite.Group()
all_sprites.add(Mapp)

running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()
