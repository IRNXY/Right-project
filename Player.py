from config import *

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