# 4. Написать функцию, которая принимает 4 параметра (стороны прямоугольника) и возвращает его площадь. Если прямоугольник является квадратом - вывести сообщение, что это квадрат.
#
# par1 = int(input("Enter a Parameter: "))
# par2 = int(input("Enter a Parameter: "))
# par3 = int(input("Enter a Parameter: "))
# par4 = int(input("Enter a Parameter: "))
#
# parameter = par1 + par2 + par3 + par4
#
# if par1 != par2 or par3 != par4:
#     print(f"The given Area({parameter}) is an Rectangle")
# elif par1 == par2 or par3 == par4:
#     print("The given Area is a Square")
#
# 2. Дописать функцию из задачи №1 так, чтобы пользователь мог указывать сколько угодно параметров, и результатом работы функции будет умножение всех параметров

loop = int(input("Enter how many times you will Enter the Area: "))
if loop <= 0:
    print("Enter a number bigger than 0")

save = []
calculate = 0

while calculate < loop:
    parameter = int(input("Enter an Area here: "))
    calculate = calculate + 1
    save.append(parameter)
print(save)

def multiply(save):
    saveing = 1
    for i in save:
        saveing = saveing * i
    return saveing
function = multiply(save)
print(function)



