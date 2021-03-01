from config import *
from pygame_init import *
# from pygame_init import map_obj


GREEN = (0, 255, 0)

class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        # загружаем картинку ящика
        self.image = pygame.image.load(
            os.path.join(img_folder, 'Spooky Ectoplasm.png')).convert()
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.image.set_colorkey(pygame.Color('black'))
        # self.image = pygame.Surface((70, 70))
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.player_x, self.player_y = map_obj.cord_pl()
        self.x = x * ZOOM
        self.y = y * ZOOM
        self.rect.center = (self.x, self.y)
        self.speed = 3

    def update(self):
        self.player_x, self.player_y = map_obj.cord_pl()
        x_max = self.player_x - self.x
        y_max = self.player_y - self.y
        max_speed = max([abs(x_max), abs(y_max)])
        if max_speed != 0:
            self.speed_x = self.speed * x_max / max_speed
            self.speed_y = self.speed * y_max / max_speed

            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.x = self.rect.x // ZOOM
            self.y = self.rect.y // ZOOM