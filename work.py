from pygame_init import *
from config import *
from Ghost import Ghost

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
# xg, yg = map_obj.cord_pl()
# print(xg, yg)


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
        # keyboard = pygame.key.get_pressed()
        time = randint(0, 50)
        if time == 1:
            randomx = randint(0, 30)
            randomy = randint(0, 30)
            if randomx < 15 and randomy < 9:
                ghost = Ghost(randomx * -1, randomy * -1)
            elif randomx < 15 and randomy >= 9:
                ghost = Ghost(randomx * -1, randomy)
            elif randomx >= 15 and randomy < 9:
                ghost = Ghost(randomx, randomy * -1)
            else:
                ghost = Ghost(randomx, randomy)
            all_sprites.add(ghost)
            ghost_sprites.add(ghost)
        # if keyboard[pygame.K_SPACE]:
        #     Way = Shortest_way((17, 13), (27, 13))
        #     for i in Way.way:
        #         # print(i)
        #         x, y = i
        #         wall = Wall(ZOOM * (x - 15), ZOOM * (y - 9))
        #         # добовляем объект Wall к списку спрайтов стен
        #         wall_sprites.add(wall)
        #         # добовляем объект Wall к общему списку всех спрайтов
        #         all_sprites.add(wall)

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

    # проверяем стены
    hits = pygame.sprite.spritecollide(map_obj.player, wall_sprites, False)
    # проверяем ящики
    hits2 = pygame.sprite.spritecollide(map_obj.player, box_sprites, False)

    # удар по ящикам
    if hits2 and 8 > map_obj.player.picture_frame > 1:
        for hit in hits2:
            explosion = Explosion(hit.x, hit.y)
            all_sprites.add(explosion)
            hit.kill()

    if hits or hits2:
        map_obj.player.rect.x -= map_obj.player.speedx
        map_obj.player.rect.y -= map_obj.player.speedy

    # проверяем пересечение с ghost
    hits3 = pygame.sprite.spritecollide(map_obj.player, ghost_sprites, False)
    if hits3:
        print('>>>>>>>>>>>', map_obj.player.live)
        map_obj.player.live -= 0.01
        if 8 > map_obj.player.picture_frame > 1:
            for hit in hits3:
                explosion = Explosion(hit.rect.x, hit.rect.y)
                all_sprites.add(explosion)
                hit.kill()
        # self.kill()
        # surprise = randint(0, 90)
        # if surprise <= 10:
        #     coin = Coin(self.x, self.y)
        #     coins_sprites.add(coin)
        #     coin.add(all_sprites)
        # elif 25 >= surprise < 20:
        #     spirit = Ghost(self.x, self.y)
        #     # print(i.rect.center)
        #     mobs_sprites.add(spirit)
        #     all_sprites.add(spirit)
        # else:
        #     Map.sprite_player.player.rect.x -= Map.sprite_player.player.speedx
        #     Map.sprite_player.player.rect.y -= Map.sprite_player.player.speedy
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
    # draw_text(screen, str(score), 18, WIDTH / 2, 10)
    draw_shield_bar(screen, 130, 85, map_obj.player.live)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
