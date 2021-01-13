import os
from config import *


class Start_screen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        fon = pygame.image.load(os.path.join(img_folder, 'dark background.png'))
        fon = pygame.transform.scale(fon, (MAP_X * ZOOM, MAP_Y * ZOOM))

        intro_text = ["                                                                 ЗАСТАВКА"]
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 70

        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color("white"))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)

        runing = True
        pygame.display.flip()
        while runing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    runing = False
                # clock.tick(60)

