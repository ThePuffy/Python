from tkinter import * # Импортируем библиотеку
window = Tk() # Создаем новое окно
window.title("bob") # Добавляем заголовок окна
window.geometry('350x200')

lbl = Label(window, text="Click this button", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

txt = Entry(window,width=70)
txt.grid(column=30, row=40)
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
    lbl.configure(text="Button was clicked !!")

btn = Button(window, text="Click Me", bg="black", fg="white", height=4, width=10)
btn.grid(column=3, row=3)







window.mainloop() # Запускаем бесконечный цикл окна

#Домашние Задание
#Доделать Задание