from run import *


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
                if self.string[y + MAP_Y * self.room_y][
                    x + MAP_X * self.room_x] == '&':
                    # предаём координаты объекта с учётом сдвига по комнатам
                    box = Box(ZOOM * x, ZOOM * y)
                    # добовляем объект Box к списку спрайтов стен
                    box_sprites.add(box)
                    wall_sprites.add(box)
                    # добовляем объект Box к общему списку всех спрайтов
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
