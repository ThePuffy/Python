import pgzrun
import random

TITLE = "Zombies vs Tanks"
WIDTH = 800
HEIGHT = 640
blue_tank = Actor("tank_blue")
blue_tank.x = WIDTH / 2
blue_tank.y = HEIGHT / 2
bullet = Actor("bulletblue")
bullet_fired = False

UP = 180
DOWN = 0
LEFT = 270
RIGHT = 90
BULLET_SPEED = 5

def shoot_bullet():
    global bullet_fired
    if bullet_fired:
        if bullet.angle == LEFT:
            bullet.x -= BULLET_SPEED
        elif bullet.angle == RIGHT:
            bullet.x += BULLET_SPEED
        elif bullet.angle == DOWN:
            bullet.y += BULLET_SPEED
        elif bullet.angle == UP:
            bullet.y -= BULLET_SPEED
        if bullet.x >= WIDTH:
            bullet.x = bullet.x + 20
            bullet_fired = False
        elif bullet.x <= 0:
            bullet.x = bullet.x - 20
            bullet_fired = False
        elif bullet.y <= HEIGHT: -
            bullet.y = bullet.y - 20
        """if bullet.x >= WIDTH or bullet.x <= 0 or \
                bullet.y >= HEIGHT or bullet.y <= 0:
            bullet_fired = False"""

def draw():
    screen.blit("tank.png", (0, 0))
    blue_tank.draw()
    bullet.draw()
    clock.schedule(shoot_bullet, 5)

def update():
    global bullet_fired
    if keyboard.left:
        blue_tank.x = blue_tank.x - 5
        blue_tank.angle = LEFT
    if keyboard.right:
        blue_tank.x = blue_tank.x + 5
        blue_tank.angle = RIGHT
    if keyboard.up:
        blue_tank.y = blue_tank.y - 5
        blue_tank.angle = UP
    if keyboard.down:
        blue_tank.y = blue_tank.y + 5
        blue_tank.angle = DOWN
    if keyboard.space:
        if not bullet_fired:
            bullet_fired = True
            sounds.laserretro_004.play()
            if blue_tank.angle == LEFT:
                bullet.x = blue_tank.x - 30
                bullet.y = blue_tank.y
                bullet.angle = LEFT

            elif blue_tank.angle == RIGHT:
                bullet.x = blue_tank.x + 30
                bullet.y = blue_tank.y
                bullet.angle = RIGHT

            elif blue_tank.angle == DOWN:
                bullet.x = blue_tank.x
                bullet.y = blue_tank.y + 30
                bullet.angle = DOWN

            elif blue_tank.angle == UP:
                bullet.x = blue_tank.x
                bullet.y = blue_tank.y - 30
                bullet.angle = UP
pgzrun.go()

