class Student():
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades

    def __str__(self):
        return f"name: {self.name}, surname: {self.surname}, grades: {self.grades}"

    def __repr__(self):
        return f"{self.name} {self.surname} {self.grades}"

    def average(self):
        summa = 0
        avglen = len(self.grades)
        for i in self.grades:
            summa = summa + i
        avg = summa/avglen
        return avg

numbers = [10, 12, 14, 16, 18, 20]
lenght = len(numbers)
numbers.sort()

if lenght % 2 == 0:
	median1 = numbers[lenght//2]
	median2 = numbers[lenght//2 - 1]
	median = (median1 + median2)/2
else:
	median = numbers[lenght//2]
print("Median is: " + str(median))



grades = [1, 2, 1, 3, 2, 1]
grades2 = [4, 5 ,4, 4, 5, 4]
s = Student(name="Vasya", surname="Pechkin", grades=grades)
s2 = Student(name="Valera", surname="Popov", grades=grades2)
print(s.average())

print([s, s2])

#Домашние Задание: 2021/11/08 - 2021/11/15
#возврощяет медиану/median
#---

#average = Средний/Средния

#average Speed = средния скорость