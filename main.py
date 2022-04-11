import pygame as pg
from pygame.draw import rect, circle, polygon

W = 700
H = 1000
# создаю объект окна программы
screen = pg.display.set_mode((W, H))  # 640pх - ширина и 480px - высота
clock = pg.time.Clock()  # добавление задержки в главный цикл

img = pg.image.load('car.png').convert_alpha()

img_rect = img.get_rect()
clone = img
clone_rect = img_rect

clone_rect.center = W // 2, H // 2

angle = 0
size = 1
car_x = 0



finished = False  # флаг, который отвечает за работу программы
while not finished:  # пока игра не окончена
    clock.tick(30)  # частота обновления 30 кадров в секунду
    # отслеживаю события (нажатия кнопок)
    for event in pg.event.get():  # для каждого события в списке событий
        if event.type == pg.QUIT:  # если нажали на крестик
            finished = True

    keys = pg.key.get_pressed()
    if keys[pg.K_e]:
        angle += 10
        car_x += 10
        clone = pg.transform.rotozoom(img, angle, size)
    if keys[pg.K_q]:
        angle -= 10
        clone = pg.transform.rotozoom(img, angle, size)
    if keys[pg.K_m]:
        size *= 1.1
        clone = pg.transform.rotozoom(img, angle, size)
    if keys[pg.K_n]:
        size /= 1.1
        clone = pg.transform.rotozoom(img, angle, size)
    if keys[pg.K_h]:
        clone = pg.transform.flip(img, True, False)
    if keys[pg.K_g]:
        clone = pg.transform.flip(img, False, True)

    clone_rect = clone.get_rect()
    clone_rect.center = W // 2, H // 2

    screen.fill((255, 255, 255))
    screen.blit(clone, clone_rect)
    rect(screen, (255, 0, 0), img_rect, 1)

    pg.display.update()