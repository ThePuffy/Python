import turtle

screen = turtle.Screen()
screen.screensize(600, 600)
screen.title('MiniGame')
screen.addshape('ship7.gif')
screen.bgpic('home.gif')

screen.addshape('pirate1.gif')

projectiles = turtle.Turtle()
projectiles.color('white')
projectiles.shape('square')
projectiles.shapesize(0.5, 1)
projectiles.penup()
projectiles.goto(500, -500)


screen.addshape('pirate1.gif')

pirate = turtle.Turtle()
pirate.shape('pirate1.gif')
pirate.up()
pirate.goto(-500 ,350)

screen.addshape('pirate1.gif')

pirate = turtle.Turtle()
pirate.shape('pirate1.gif')
pirate.up()
pirate.goto(500 ,0)

pen = turtle.Turtle()
pen.shape('ship7.gif')
pen.up()





def up():
    # ycor - get coordinate, sety - set new coordinate
    y = pen.ycor()
    pen.sety(y + 10)

def down():
    y = pen.ycor()
    pen.sety(y - 10)

def left():
    x = pen.xcor()
    pen.setx(x - 10)

def right():
    x = pen.xcor()
    pen.setx(x + 10)

while True:
    screen.listen()
    screen.onkeypress(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
    screen.onkeypress(down, "Down")
    screen.onkeypress(left, "Left")
    screen.onkeypress(right, "Right")
    screen.update()
Screen.mainloop()

