import pygame as pg
import pymunk.pygame_util

from random import randrange
pymunk.pygame_util.positive_y_is_up = False

#Настройки PyGame
RES = WIDTH, HEIGHT = 900, 600
FPS = 60

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

#переменные Pymunk
space = pymunk.Space()
space.gravity = 0, 8000

#платформа
segment_shape = pymunk.Segment(space.static_body, (1, HEIGHT), (WIDTH, HEIGHT), 26)
space.add(segment_shape)
segment_shape.elasticity = 0.4
segment_shape.friction = 1.0

#segment_shape = pymunk.Segment(space.static_body, (1, HEIGHT), (WIDTH, HEIGHT), 26)
#space.add(segment_shape)
#segment_shape.elasticity = 0.4
#segment_shape.friction = 1.0

segment_shape = pymunk.Segment(space.static_body, (1, 200), (200, 200), 26)
space.add(segment_shape)
segment_shape.elasticity = 0.4
segment_shape.friction = 1.0



#квадратики
def create_square(space, pos):
    square_mass, square_size = 1, (60, 60)
    square_moment = pymunk.moment_for_box(square_mass, square_size)
    square_body = pymunk.Body(square_mass, square_moment)
    square_body.position = pos
    square_shape = pymunk.Poly.create_box(square_body, square_size)
    square_shape.elasticity = 0.8
    square_shape.friction = 1.0
    square_shape.color = [randrange(256) for i in range(4)]
    space.add(square_body, square_shape)

while True:
    surface.fill(pg.Color('black'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        # спавн мячиков
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button == 1:
                create_square(space, i.pos)
                print(i.pos)

    space.step(1 / FPS)
    space.debug_draw(draw_options)

    print('end')

    # Домашние Задание: 2022/1/24 - 2022/1/31
    # Найти игру на сайте https://python-scripts.com/?s=snake про Спрайты (обéкт которые имеет анимацию)
    pg.display.flip()
    clock.tick(FPS)
