import pygame
import random
import os
import sys
# from Map import *
# from pygame_init import *

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
# horizontal_borders = pygame.sprite.Group()
# vertical_borders = pygame.sprite.Group()


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


class Explosion_Box(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(all_sprites)
        self.image = pygame.Surface((50, 50),
                                    pygame.SRCALPHA, 32)
        self.rect = pygame.Rect(pos[0], pos[1], 10, 10)

    def attak(self, poss, way):
        if way == "up":
            self.rect = pygame.Rect(poss[0], poss[1] - 10, 20, 30)
            pygame.sprite.spritecollide(self, box_sprites, True)

        elif way == "down":
            self.rect = pygame.Rect(poss[0], poss[1] + 10, 20, 30)
            pygame.sprite.spritecollide(self, box_sprites, True)

        elif way == "left":
            self.rect = pygame.Rect(poss[0] - 10, poss[1], 30, 20)
            pygame.sprite.spritecollide(self, box_sprites, True)

        elif way == "right":
            self.rect = pygame.Rect(poss[0] + 10, poss[1], 30, 20)
            pygame.sprite.spritecollide(self, box_sprites, True)


class Play_plaer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)

        # self.image = load_image(picture_name)
        # self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        # self.mask = pygame.mask.from_surface(self.image)
        # self.rect.x = 500
        # self.rect.y = 500

        self.counter = 20
        self.life_count = 5
        self.speed = 1
        self.counter_at = 10
        self.x = 500
        self.y = 400
        self.way_at = "left"
        self.way_c_go = None
        self.clock = pygame.time.Clock()
        self.image = pygame.Surface((20, 20),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (10, 10), 10)
        self.rect = pygame.Rect(self.x, self.y, 10, 10)

    def attack(self):
        # проверяется в каком направлении (self.way_at) последний раз двигался игрок
        if self.way_at == "right":
            for i in self.vrag_pos:
                if self.x + 50 >= i[0] and self.x <= i[0] and self.y - 50 <= i[1] and self.y + 50 >= i[1]:
                    self.vrag_pos[0][-1] -= 1

        elif self.way_at == "left":
            for i in self.vrag_pos:
                if self.x - 50 <= i[0] and self.x >= i[0] and self.y - 50 <= i[1] and self.y + 50 >= i[1]:
                    self.vrag_pos[0][-1] -= 1

        elif self.way_at == "up":
            for i in self.vrag_pos:
                if self.x + 50 >= i[0] and self.y - 50 <= i[1] and self.x - 50 <= i[0] and self.y >= i[1]:
                    self.vrag_pos[0][-1] -= 1

        elif self.way_at == "down":
            for i in self.vrag_pos:
                if self.x + 50 >= i[0] and self.y + 50 >= i[1] and self.x - 50 <= i[0] and self.y <= i[1]:
                    self.vrag_pos[0][-1] -= 1

    def update(self, vrag_pos):
        # все данные о враге
        # [x, y, скорость, жизни]
        self.vrag_pos = vrag_pos

        keyboard = pygame.key.get_pressed()

        if keyboard[pygame.K_a]:
            self.way_at = "left"
            if self.x == 0:
                self.x = 1009
            else:
                self.x -= self.speed
                self.rect = self.rect.move(-1, 0)
                if pygame.sprite.spritecollideany(self, wall_sprites):
                    self.rect = self.rect.move(1, 0)

        if keyboard[pygame.K_d]:
            self.way_at = "right"
            if self.x == 1010:
                self.x = 1
            else:
                self.x += self.speed
                self.rect = self.rect.move(11, 0)
                if pygame.sprite.spritecollideany(self, wall_sprites):
                    self.rect = self.rect.move(-11, 0)
                else:
                    self.rect = self.rect.move(-10, 0)

        if keyboard[pygame.K_w]:
            self.way_at = "up"
            if self.y == 0:
                self.y = 709
            else:
                self.y -= self.speed
                self.rect = self.rect.move(0, -1)
                if pygame.sprite.spritecollideany(self, wall_sprites):
                    self.rect = self.rect.move(0, 1)

        if keyboard[pygame.K_s]:
            self.way_at = "down"
            if self.y == 710:
                self.y = 1
            else:
                self.y += self.speed
                self.rect = self.rect.move(0, 11)
                if pygame.sprite.spritecollideany(self, wall_sprites):
                    self.rect = self.rect.move(0, -11)
                else:
                    self.rect = self.rect.move(0, -10)

        # вызывается функция атаки если нажат пробел
        if keyboard[pygame.K_SPACE]:
            # если счётчик self.counter_at больше или равен 10, тогда
            # тогда вызывается self.attack()
            if self.counter_at >= 10:
                self.attack()
                explosion_box.attak((self.rect.x, self.rect.y), self.way_at)
                self.counter_at = 0
        if self.counter_at < 10:
            self.counter_at += 0.1

        self.clock.tick(100)

        return self.x, self.y, self.vrag_pos[0]


class Move_Enemy(pygame.sprite.Sprite):
    def __init__(self, vrag_inf):
        super().__init__(all_sprites)

        # self.image = load_image("mountains.png")
        # self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        # self.mask = pygame.mask.from_surface(self.image)

        self.way_right = 0
        self.way_left = 0
        self.way_up = 0
        self.way_down = 0

        self.one = "none"

        self.vrag_inf = [vrag_inf]
        self.counter = 20
        self.life_count = 5
        self.image = pygame.Surface((20, 20),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("green"),
                           (10, 10), 10)
        self.rect = pygame.Rect(200, 50, 10, 10)

    def lifes(self):
        return self.life_count

    def update(self, x, y, inf):
        if inf[-1] <= 0:
            pygame.draw.circle(self.image, pygame.Color("white"),
                               (10, 10), 10)
            # self.rect = pygame.Rect(inf[0], inf[1], 10, 10)
            return [inf[0], inf[1], 0, inf[-1]]
        self.pl_x = x
        self.pl_y = y
        # если закончились жизни выходим
        if self.life_count <= 0:
            return 1
        self.rect.x = inf[0]
        self.rect.y = inf[1]
        self.speed_en = inf[2]
        # Вверх
        if abs(self.rect.x - self.pl_x) > abs(self.rect.y - self.pl_y) \
                and self.way_up == 0 and self.way_right == 0 and self.one == "none":
            if self.rect.y > self.pl_y:
                inf[1] = self.rect.y - self.speed_en
                self.rect = self.rect.move(0, -1)
                if pygame.sprite.spritecollideany(self, wall_sprites):
                    while pygame.sprite.spritecollideany(self, wall_sprites):
                        self.rect = self.rect.move(1, 0)
                        self.way_right += 1
                    self.rect = self.rect.move(-self.way_right, 0)
                    while pygame.sprite.spritecollideany(self, wall_sprites):
                        self.rect = self.rect.move(-1, 0)
                        self.way_left += 1
                    self.rect = self.rect.move(self.way_left, 0)

                    self.rect = self.rect.move(0, 1)
                    inf[1] = self.rect.y + self.speed_en
            # вниз
            else:
                inf[1] = self.rect.y + self.speed_en
                self.rect = self.rect.move(0, 10)
                if pygame.sprite.spritecollideany(self, wall_sprites):
                    while pygame.sprite.spritecollideany(self, wall_sprites):
                        self.rect = self.rect.move(1, 0)
                        self.way_right += 1
                    self.rect = self.rect.move(-self.way_right, 0)
                    while pygame.sprite.spritecollideany(self, wall_sprites):
                        self.rect = self.rect.move(-1, 0)
                        self.way_left += 1
                    self.rect = self.rect.move(self.way_left, 0)
                    self.rect = self.rect.move(0, -10)
                    inf[1] = self.rect.y - self.speed_en

                else:
                    self.rect = self.rect.move(0, -9)

            # влево
            if self.pl_y == self.rect.y:
                if self.rect.x > self.pl_x:
                    inf[0] = self.rect.x - self.speed_en
                    self.rect = self.rect.move(-1, 0)
                    if pygame.sprite.spritecollideany(self, wall_sprites):
                        while pygame.sprite.spritecollideany(self, wall_sprites):
                            self.rect = self.rect.move(0, -1)
                            self.way_up += 1
                        self.rect = self.rect.move(0, self.way_up)
                        while pygame.sprite.spritecollideany(self, wall_sprites):
                            self.rect = self.rect.move(0, 1)
                            self.way_down += 1
                        self.rect = self.rect.move(0, -self.way_down)

                        self.rect = self.rect.move(1, 0)
                        inf[0] = self.rect.x + self.speed_en
                # вправо
                else:
                    inf[0] = self.rect.x + self.speed_en
                    self.rect = self.rect.move(10, 0)
                    if pygame.sprite.spritecollideany(self, wall_sprites):
                        while pygame.sprite.spritecollideany(self, wall_sprites):
                            self.rect = self.rect.move(0, -1)
                            self.way_up += 1
                        self.rect = self.rect.move(0, self.way_up)
                        while pygame.sprite.spritecollideany(self, wall_sprites):
                            self.rect = self.rect.move(0, 1)
                            self.way_down += 1
                        self.rect = self.rect.move(0, -self.way_down)

                        self.rect = self.rect.move(-10, 0)
                        inf[0] = self.rect.x - self.speed_en

                    else:
                        self.rect = self.rect.move(-9, 0)

        elif abs(self.rect.x - self.pl_x) < abs(self.rect.y - self.pl_y) \
                and self.way_up == 0 and self.way_right == 0 and self.way_left == 0 and self.one == "none":
            if self.rect.x > self.pl_x:
                inf[0] = self.rect.x - self.speed_en
                self.rect = self.rect.move(-1, 0)
                if pygame.sprite.spritecollideany(self, wall_sprites):
                    while pygame.sprite.spritecollideany(self, wall_sprites):
                        self.rect = self.rect.move(0, -1)
                        self.way_up += 1
                    self.rect = self.rect.move(0, self.way_up)
                    while pygame.sprite.spritecollideany(self, wall_sprites):
                        self.rect = self.rect.move(0, 1)
                        self.way_down += 1
                    self.rect = self.rect.move(0, -self.way_down)

                    self.rect = self.rect.move(1, 0)
                    inf[0] = self.rect.x + self.speed_en

            else:
                inf[0] = self.rect.x + self.speed_en
                self.rect = self.rect.move(10, 0)
                if pygame.sprite.spritecollideany(self, wall_sprites):
                    while pygame.sprite.spritecollideany(self, wall_sprites):
                        self.rect = self.rect.move(0, -1)
                        self.way_up += 1
                    self.rect = self.rect.move(0, self.way_up)
                    while pygame.sprite.spritecollideany(self, wall_sprites):
                        self.rect = self.rect.move(0, 1)
                        self.way_down += 1
                    self.rect = self.rect.move(0, -self.way_down)

                    self.rect = self.rect.move(-10, 0)
                    inf[0] = self.rect.x - self.speed_en
                else:
                    self.rect = self.rect.move(-9, 0)

            if self.pl_x == self.rect.x:
                if self.rect.y > self.pl_y:
                    inf[1] = self.rect.y - self.speed_en
                    self.rect = self.rect.move(0, -10)
                    if pygame.sprite.spritecollideany(self, wall_sprites):
                        while pygame.sprite.spritecollideany(self, wall_sprites):
                            self.rect = self.rect.move(1, 0)
                            self.way_right += 1
                        self.rect = self.rect.move(-self.way_right, 0)
                        while pygame.sprite.spritecollideany(self, wall_sprites):
                            self.rect = self.rect.move(-1, 0)
                            self.way_left += 1
                        self.rect = self.rect.move(self.way_left, 0)

                        self.rect = self.rect.move(0, 10)
                        inf[1] = self.rect.y + self.speed_en
                    else:
                        self.rect = self.rect.move(0, 9)

                else:
                    inf[1] = self.rect.y + self.speed_en
                    self.rect = self.rect.move(0, 1)
                    if pygame.sprite.spritecollideany(self, wall_sprites):
                        while pygame.sprite.spritecollideany(self, wall_sprites):
                            self.rect = self.rect.move(1, 0)
                            self.way_right += 1
                        self.rect = self.rect.move(-self.way_right, 0)
                        while pygame.sprite.spritecollideany(self, wall_sprites):
                            self.rect = self.rect.move(-1, 0)
                            self.way_left += 1
                        self.rect = self.rect.move(self.way_left, 0)

                        self.rect = self.rect.move(0, -1)
                        inf[1] = self.rect.y - self.speed_en

        if self.one == "x" and self.rect.x != self.pl_x:
            if self.rect.x > self.pl_x:
                self.rect = self.rect.move(-1, 0)
                inf[0] = self.rect.x - 1
            elif self.rect.x < self.pl_x:
                self.rect = self.rect.move(1, 0)
                inf[0] = self.rect.x + 1

        elif self.one == "y" and self.rect.y != self.pl_y:
            if self.rect.y > self.pl_y:
                self.rect = self.rect.move(0, -1)
                inf[1] = self.rect.y - 1
            elif self.rect.y < self.pl_y:
                self.rect = self.rect.move(0, 1)
                inf[1] = self.rect.y + 1

        elif self.rect.x == self.pl_x and self.one != "none" or self.rect.y == self.pl_y and self.one != "none":
            self.one = "none"
            self.way_left = 0
            self.way_right = 0
            self.way_down = 0
            self.way_up = 0

        else:
            if self.way_right > self.way_left and self.way_left >= 0:
                self.rect = self.rect.move(-1, 0)
                inf[0] = self.rect.x - self.speed_en
                self.way_left -= 1
                if self.way_left == 0:
                    self.one = "y"

            elif self.way_right < self.way_left and self.way_right >= 0:
                self.rect = self.rect.move(1, 0)
                inf[0] = self.rect.x + self.speed_en
                self.way_right -= 1
                if self.way_right == 0:
                    self.one = "y"

            elif self.way_down > self.way_up and self.way_up >= 0:
                self.rect = self.rect.move(0, -1)
                inf[1] = self.rect.y - self.speed_en
                self.way_up -= 1
                if self.way_up == 0:
                    self.one = "x"

            elif self.way_down < self.way_up and self.way_down >= 0:
                self.rect = self.rect.move(0, 1)
                inf[1] = self.rect.y + self.speed_en
                self.way_down -= 1
                if self.way_down == 0:
                    self.one = "x"

            else:
                self.way_left = 0
                self.way_right = 0
                self.way_down = 0
                self.way_up = 0

        # self.counter - счётчик, чтобы враг мог ударить всего 5 раз
        if self.counter >= 20:
            # погрешность в координатах
            if self.rect.x + 1 >= self.pl_x >= self.rect.x - 1:
                if self.rect.y + 1 >= self.pl_y >= self.rect.y - 1:
                    self.life_count -= 1
                    self.counter = 0
        # иначе прибавляем к счётчику + 0.1
        else:
            self.counter += 0.1
        return [inf[0], inf[1], self.speed_en, inf[-1]]


class Scr_men(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(all_sprites)
        self.image = pygame.Surface((20, 20),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("black"),
                           (10, 10), 10)
        self.rect = pygame.Rect(200, 50, 10, 10)

    def update(self, life):
        pygame.draw.circle(screen, (0, 0, 110), (900, 600), 40)

        for i in range(1, 6):
            if life == i:
                for e in range(i):
                    pygame.draw.circle(screen, (200, 0, 50), (770 + 25 * e, 60), 12)


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
