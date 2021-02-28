from pygame_init import *
from config import *

FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
pygame.display.flip()
# pygame.mixer.music.load('возможно во время игры.ogg')
# pygame.mixer.music.play()

start = Start_screen()


# menu_obj = Menu()
# all_sprites.add(menu_obj)


# вызываем объект Map
# Mapp = Map(file_name='1.txt', room_x=1, room_y=1)
# Mapp.change_map(-20, 30)

# a = mobs_sprites()

running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        keyboard = pygame.key.get_pressed()

        if keyboard[pygame.K_SPACE]:
            Way = Shortest_way((17, 13), (27, 13))
            for i in Way.way:
                # print(i)
                x, y = i
                wall = Wall(ZOOM * (x - 15), ZOOM * (y - 9))
                # добовляем объект Wall к списку спрайтов стен
                wall_sprites.add(wall)
                # добовляем объект Wall к общему списку всех спрайтов
                all_sprites.add(wall)

        #     for i in box_sprites:
        #         explosion = Explosion(i.rect.center)
        #         all_sprites.add(explosion)
        #         i.kill()
        #         surprise = randint(0, 90)
        #         if surprise <= 10:
        #             coin = Coin(i.rect.center)
        #             coins_sprites.add(coin)
        #             coin.add(all_sprites)
        #         elif 25 >= surprise < 20:
        #             spirit = Mob_Spirit(i.rect.center)
        #             # print(i.rect.center)
        #             mobs_sprites.add(spirit)
        #             all_sprites.add(spirit)

        if event.type == pygame.QUIT:
            running = False
    # map_obj.enemy
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
