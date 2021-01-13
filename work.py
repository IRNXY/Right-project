# импортируем файл с картой
from Map import *
from pygame_init import *

FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
pygame.display.flip()


class Start_screen(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        game_folder = os.path.dirname(__file__)
        img_folder = os.path.join(game_folder, 'img')
        fon = pygame.image.load(os.path.join(img_folder, 'fon_better.jpg'))
        fon = pygame.transform.scale(fon, (MAP_X * ZOOM, MAP_Y * ZOOM))

        # runing = True
        # play = [200, 200, 190, 50]
        # discr = [430, 200, 190, 50]
        intro_text = ["                                                                   ЗАСТАВКА"]
        # # fon.set_colorkey(pygame.Color('black'))
        #
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 30)
        text_coord = 70
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color("black"))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        # # pygame.draw.rect(screen, (0, 30, 160),
        # #                  (play[0], play[1], play[2], play[3]))
        # # pygame.draw.rect(screen, (0, 30, 160),
        # #                  (discr[0], discr[1], discr[2], discr[3]))
        runing = True
        pygame.display.flip()
        while runing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    # sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    Map(file_name='1.txt', room_x=1, room_y=1)
                    runing = False

                    # if play[0] <= event.pos[0] and play[0] + play[2] >= \
                    #         event.pos[0] and \
                    #         play[1] <= event.pos[1] and play[1] + play[3] >= \
                    #         event.pos[1]:
                    #     runing = False
                    #
                    #     elif discr[0] <= event.pos[0] and discr[0] + discr[2] >= \
                    #             event.pos[0] and \
                    #             discr[1] <= event.pos[1] and discr[1] + discr[3] >= \
                    #             event.pos[1]:
                    #         pass


                # clock.tick(60)


start = Start_screen()

# вызываем объект Map
# Mapp = Map(file_name='1.txt', room_x=1, room_y=1)
# Mapp.change_map(-20, 30)

running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        keyboard = pygame.key.get_pressed()
        #
        if keyboard[pygame.K_SPACE]:
            for i in box_sprites:
                explosion = Explosion(i.rect.center)
                all_sprites.add(explosion)
                i.kill()
                surprise = randint(0, 90)
                if surprise <= 10:
                    coin = Coin(i.rect.center)
                    coins_sprites.add(coin)
                    coin.add(all_sprites)
                elif 35 >= surprise < 20:
                    spirit = Mob_Spirit(i.rect.center)
                    mobs_sprites.add(spirit)
                    all_sprites.add(spirit)

        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()
    # проверка не ударид ли игрок ящик
    # score = 0
    # hits = pygame.sprite.groupcollide(mobs_sprites, swords_sprites, True, True)
    # for hit in hits:
    #     # radius в mob
    #     score += 50 - hit.radius
    #     # воспроизведение звука
    #     # random.choice(expl_sounds).play()
    #     explosion = Explosion(hit.rect.center)
    #     all_sprites.add(explosion)

    # Рендеринг
    screen.fill(pygame.Color('black'))
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
