import turtle

screen = turtle.Screen()
screen.screensize(600, 600)

pen = turtle.Turtle()
pen.shape('square')
pen.up()

def up():
    # ycor - get coordinate, sety - set new coordinate
    y = pen.ycor()
    pen.sety(y+10)

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

screen.mainloop()
