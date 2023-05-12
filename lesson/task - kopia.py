
month = int(input("Ведити ваш месец рождения(ЧИСЛОМ): "))
name_months = ""
if month == 1:
    name_months = "Январь"
elif month == 2:
    name_months = "Февраль"
elif month == 3:
    name_months = "Март"
elif month == 4:
    name_months = "Апрель"
elif month == 5:
    name_months = "Май"
elif month == 6:
    name_months = "Июнь"
elif month == 7:
    name_months = "Июль"
elif month == 8:
    name_months = "Август"
elif month == 9:
    name_months = "Сентябрь"
elif month == 10:
    name_months = "Октябрь"
elif month == 11:
    name_months = "Ноябрь"
elif month == 12:
    name_months = "Декабрь"
else:
    print("Такого месица не существует")

print(f"Ты родился в {name_months}")

if month == 1 or month == 2 or month == 12:
    print("Зима")
elif month == 3 or month == 4 or month == 5:
    print("Весна")
elif month == 6 or month == 7 or month == 8:
    print("Лето")
elif month == 9 or month == 10 or month == 11:
    print("Осень")
else:
    print("Такого сезона не существует")

if month == 1 or month == 2 or month == 12:
    print("На улице идёт снег")
elif month == 3 or month == 4 or month == 5:
    print("На улице тает лёд")
elif month == 6 or month == 7 or month == 8:
    print("На улице тепло и расвитают цветы и фрукты")
elif month == 9 or month == 10 or month == 11:
    print("На улице холоднеет и листе падуют с деревьев")
else:
    print("Такой ассоциацой не существует")

# Домашние Задание 14/06/2021 - 16/06/2021:
# Доделать задание.
# -----
