# вот так начинаються комментарии
import turtle # импортируем библиотеку

window = turtle.Screen() # здесь мы создаем окно
window.title("First programm") # здесь мы устанавливаем название для окна

pen = turtle.Turtle()  # создаем наш объект, ручка
pen.shape('square') # arrow, circle, dot, square, turtle
pen.color("green") # указываем цвет
pen.width(5) # указать ширину линии
pen.speed(1) # задаем скорость от 0 до 10
pen.penup() # поднять ручку (не рисовать)
pen.goto(-250, 250)
pen.pendown() # опустить (начать рисовать)
pen.goto(250, 250)

# pen.begin_fill()
# pen.fillcolor("red")
# pen.forward(100) # идти вперед
# pen.right(90) # повернуться направо на 90 градусов
# pen.forward(100)
# pen.right(90)
# pen.forward(100)
# pen.right(90)
# pen.forward(100)
# pen.end_fill()

dog = turtle.Turtle()
dog.goto(-250, 250)
dog.goto(-250, -250)
dog.home()
dog.hideturtle()
dog.penup()
dog.forward(200)
dog.showturtle()
distance = dog.distance(pen) # расстояние между собакой и pen
print(distance) # напечатать в консоли код
dog.write(distance)

window.mainloop() # чтобы окно не закрывалось
