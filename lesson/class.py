
class Rectangle:
    def __init__(self, widht, height):
        self.widht = widht
        self.height = height

    def peri(self):
        perimeter = self.widht + self.widht + self.height + self.height
        return perimeter

    def area(self):
        areas = self.widht * self.height
        return areas

    def __str__(self):
        return f"widht: {self.widht}, height: {self.height}"

    def  __repr__(self):
        return f"{self.widht} {self.height}"

    def square(self):
        if self.widht == self.height:
            is_square = True
        else:
            is_square = False
        return is_square

r = Rectangle(widht=10, height=5)
r2 = Rectangle(widht=7, height=5)
print([r, r2])
print(r2.peri())
print(r2.area())
print(r2.square())

class Cat:
    def __init__(self, color, name, breed):
        self.color = color
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"Name: {self.name}, breed: {self.breed}, color: {self.color}"

    def __repr__(self):
        return self.breed

    def jump(self, distance):
        print(f'Cat {self.name} is jumping on distance {distance}')


cat = Cat(color='grey', name='Barsic', breed='Britian')
cat2 = Cat(color='black', name='Jack', breed='German' )
list_cats = [cat, cat2]
print(list_cats)
