from run import *


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
