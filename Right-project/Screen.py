from run import *


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
