import turtle
import random

screen = turtle.Screen()
screen.title("Caribbean Hunt")
screen.screensize(1000, 1000)
screen.bgpic('home.gif')
screen.addshape('start_btn.gif')
screen.addshape('life.gif')
screen.addshape('coin.gif')
screen.addshape('chest_gold.gif')

btn = turtle.Turtle()
btn.shape('start_btn.gif')
btn.hideturtle()
btn.up()
btn.goto(-18, 145)
btn.showturtle()

heart = 3

point = 0

def menu(x,y):
    btn.hideturtle()
while True:
    btn.onclick(menu)
    if btn.isvisible() == False:
        screen.bgpic('sea_fon_2.gif')
        break

screen.addshape('ship.gif')
screen.addshape('core.gif')
screen.addshape('pirate.gif')
screen.addshape('damage_pirate.gif')
screen.addshape('rock.gif')



# Ядро чтобы стрелять по пиратам
core = turtle.Turtle()
core.hideturtle()
core.shape('core.gif')
core.up()

# Корабль - главный игрок
ship = turtle.Turtle()
ship.shape('ship.gif')
ship.up()

# Пираты - враг
pirate1 = turtle.Turtle()
pirate1.shape('pirate.gif')
pirate1.up()
pirate1.goto(0 ,230)

pirate2 = turtle.Turtle()
pirate2.shape('pirate.gif')
pirate2.up()
pirate2.goto(-500 ,230)

pirate3 = turtle.Turtle()
pirate3.shape('pirate.gif')
pirate3.up()
pirate3.goto(500 ,230)

# Гора - Препяцтвие
stone = turtle.Turtle()
stone.shape('rock.gif')
stone.up()
stone.goto(random.randint(-300, 300), 350)

# Сундук - приз
chest = turtle.Turtle()
chest.shape('chest_gold.gif')
chest.up()
chest.hideturtle()
chest.goto(0, 230)

# Жизни
life = turtle.Turtle()
life.shape('life.gif')
life.up()
life.hideturtle()
life.goto(550, 600)
life.stamp()
life.goto(600, 600)
life.stamp()
life.goto(650, 600)
life.stamp()
life.showturtle()

# Пойнты
coin = turtle.Turtle()
coin.shape('coin.gif')
coin.up()
coin.hideturtle()
coin.goto(-1000, 600)
coin.showturtle()

text = turtle.Turtle()
text.up()
text.hideturtle()
text.goto(-970, 580)

def up():
    y = ship.ycor() # get coordinate of y
    if y >= 270:
        pass
    else:
        ship.sety(y + 10) # set coordinate of y

def down():
    y = ship.ycor()
    if y <= -270: 
        pass
    else:
        ship.sety(y - 10)

def left( ):
    x = ship.xcor()
    if x <= -600:
        pass
    else:
        ship.setx(x - 10)

def right():
    x = ship.xcor()
    if x >= 600:
        pass
    else:
        ship.setx(x + 10)

def space():
    if core.isvisible():
        pass
    else:
        x_ship = ship.xcor()
        y_ship = ship.ycor()
        core.goto(x_ship, y_ship)
        core.showturtle()

def move_core():
    y = core.ycor()
    if y >= 300:
        core.hideturtle()
    else:
        core.sety(y + 10)

def move_pirate(pirate):
    y = pirate.ycor()
    if y < -400:
        pirate.hideturtle()
        pirate.goto(random.randint(-300, 300),350)
        pirate.shape('pirate.gif')
        pirate.showturtle()
    else:
        pirate.sety(y - 7.5)

def move_stone():
    y = stone.ycor()
    if y < -400:
        rand_x = random.randint(-300, 300)
        rand_y = 350
        stone.hideturtle()
        if pirate1.distance(rand_x, rand_y) > 30:
            stone.goto(random.randint(-300, 300), 350)
            stone.showturtle()
    else:
        stone.sety(y - 10)

def move_chest():
    y = chest.ycor()
    if y < -400:
        rand_x = random.randint(-300, 300)
        rand_y = 350
        chest.hideturtle()
        if point == 10:
            chest.showturtle()



while True:
    screen.listen()
    screen.onkeypress(up, "Up")  # This will call the up function if the "up" arrow key is pressed
    screen.onkeypress(down, "Down")
    screen.onkeypress(left, "Left")
    screen.onkeypress(right, "Right")
    screen.onkeypress(space, "space")
    move_pirate(pirate1)
    move_pirate(pirate2)
    move_pirate(pirate3)
    move_stone()
    text.clear()
    text.write(f"{point}", font=('Arial', 30, 'normal'))

    #if points == 500:

      #  chest.showturtle()

    if core.isvisible():
        move_core()
        if core.distance(pirate1) <= 50:
            pirate1.shape('damage_pirate.gif')
            point = point + 1
        if core.distance(pirate2) <= 50:
            pirate2.shape('damage_pirate.gif')
            point = point + 1
        if core.distance(pirate3) <= 50:
            pirate3.shape('damage_pirate.gif')
            point = point + 1
        if chest.distance(ship) <= 50:
            chest.hideturtle()
            screen.bgpic('home_menu.gif')
    screen.update()
    if pirate1.distance(ship) <= 100:
        pirate1.goto(random.randint(-300, 300),350)
        life.clearstamps(1)
        heart = heart - 1
    if pirate2.distance(ship) <= 100:
        pirate2.goto(random.randint(-300, 300),350)
        life.clearstamps(1)
        heart = heart - 1
    if pirate3.distance(ship) <= 100:
        pirate3.goto(random.randint(-300, 300),350)
        life.clearstamps(1)
        heart = heart - 1
    if ship.distance(stone) <= 85:
        stone.goto(random.randint(-300, 300), 350)
        life.clearstamps(1)
        heart = heart - 1
    if heart == 0:
        break

core.hideturtle()
stone.hideturtle()
pirate1.hideturtle()
pirate2.hideturtle()
pirate3.hideturtle()
ship.hideturtle()
life.hideturtle()

screen.bgpic('game_over.gif')
screen.title('GAME OVER')

screen.mainloop()

# Домашние Задание
# Надо доделать сундук(как корабль)