from run import *


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
