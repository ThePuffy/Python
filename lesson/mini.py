import turtle

screen = turtle.Screen()
screen.title("Pirate Game")
screen.screensize(600, 600)
screen.bgpic('home.gif')
screen.addshape('ship.gif')
screen.addshape('core.gif')
screen.addshape('pirate.gif')
screen.addshape('pirate.gif')
screen.addshape('pirate.gif')

# Ядро чтобы стрелять по пиратам
core = turtle.Turtle()
core.hideturtle()
core.shape('core.gif')
core.up()

# Корабль - главный игрок
ship = turtle.Turtle()

ship.shape('ship.gif')
ship.up()

# Пираты - Мишень
pirate = turtle.Turtle()
pirate.shape('pirate.gif')
pirate.up()
pirate.goto(0 ,400)

pirate = turtle.Turtle()
pirate.shape('pirate.gif')
pirate.up()
pirate.goto(-280 ,400)

pirate = turtle.Turtle()
pirate.shape('pirate.gif')
pirate.up()
pirate.goto(280 ,400)



def up():
    y = ship.ycor() # get coordinate of y
    if y >= 490:
        pass
    else:
        ship.sety(y + 10) #set coordinate of y

def down():
    y = ship.ycor()
    if y <= -490:
        pass
    else:
        ship.sety(y - 10)

def left():
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
    if y >= 510:
        core.hideturtle()
    else:
        core.sety(y + 10)

while True:
    screen.listen()
    screen.onkeypress(up, "Up")  # This will call the up function if the "up" arrow key is pressed
    screen.onkeypress(down, "Down")
    screen.onkeypress(left, "Left")
    screen.onkeypress(right, "Right")
    screen.onkeypress(space, "space")

    if core.isvisible():
        move_core()
    screen.update()

screen.mainloop()

# Домашние Задание:
# Сделать пиратов(пиратов, пиратских короблей)
# Разобратся distance()