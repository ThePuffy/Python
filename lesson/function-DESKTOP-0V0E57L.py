def print_text():
    print("This is our function")

def add_number(a=5, b=4):
    return a+b

# a   b    c
# 3 + 3 = x
def make_math(a=None, b=3, c=7):
    if a ==None:
         pass
    elif b == None:
        pass
    elif c == None:
        pass

summa1 = add_number(12, 5)
summa2 = add_number(3, 2)
summa3 = add_number(8, 14)
summa4 = add_number(summa1, summa2)
summa5 = add_number(add_number(5, 7), add_number(1, 3))

print(summa1, summa2, summa3, summa4, summa5)

print(make_math(b=3, c=7))

# a + 5 = 12
a = 500
b = None
c = -765


def make_math(a=None, b=None, c=None):
    if a == None:
        result = c - b
    elif b == None:
        result = c - a
    elif c == None:
        result = a + b
    else:
        result = c
    return result

print(make_math(a, b, c))


# 1. Напишите функцию, которая принимает два параметра числовых, возвращает результат умножения этих параметров.

def multiply(a1, b1):
    return a1 * b1

print(multiply(2, 5))

# 3. Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start»
# до величины «end» включительно.
# Если пользователь задаст первое число большее чем второе, просто поменяйте их местами

hub1 = int(input("Input a random number: "))
hub2 = int(input("Input a random number: "))

def hub(start, end):
    if start < end:
        for i in range(start, end):
            if i % 2 == 0:
                print(i)  
# Доделать! 4/8/2021
