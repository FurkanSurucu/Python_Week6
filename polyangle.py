'''
Developer: Furkan Sürücü
Purpose of Software: Reinforcement of learned python code and self-improvement
What does program do?:
Create a class named Triangle and Rectangle.
Create a subclass named Square inherited from Rectangle.
Create a subclass named Cube inherited from Square.
Create a subclass named Pyramid multiple inherited both from Triangle and Square.
Two dimensional classes (Triangle, Rectangle and Square) should have:
    its dimensions as attributes.(can be inherited from a superclass)
    methods which calculate its area and perimeter separately.
Three dimensional classes (Cube and Pyramid) should have:
    its dimensions as attributes which are inherited from a superclass
    its extra dimensions if there is. (hint: maybe for Pyramid)
    methods which calculate its volume and surface area separately. (surface area is optional, you may not do this)
'''
class Triangle:
    def __init__(self,a,b,c,h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def area(self):
        area_triangle = self.a * self.h / 2
        return f'Area: {area_triangle}'
    def perimeter(self):
        perimeter_triangle = self.a + self.b + self.c
        return f'Perimeter: {perimeter_triangle}'

class Rectangle:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        area_rectangle = self.a*self.b
        return f'Area : {area_rectangle}'
    def perimeter(self):
        perimeter_rectangle = (self.a + self.b) * 2
        return f'Perimeter : {perimeter_rectangle}'

class Square(Rectangle):
    def __init__(self,a):
        super().__init__(a,a)
    def area(self):
        area_square = self.a**2
        return f'Area : {area_square}'
    def perimeter(self):
        perimeter_square = self.a*4
        return f'Perimeter : {perimeter_square}'


class Cube(Square):
    def __init__(self, a):
        super().__init__(a)
    def area(self):
        area_cube = (self.a ** 2) * 6
        return f'Area: {area_cube}'
    def perimeter(self):
        perimeter_cube = self.a * 24
        return f'Perimeter: {perimeter_cube}'
    def volume(self):
        volume_cube = self.a ** 3
        return f'Volume: {volume_cube}'
class Pyramid(Triangle, Square):
    def __init__(self, a, b, c, h):
        super().__init__(a,b,c,h)

    def area(self):
        area_pyramid = self.a * (self.a + ((self.a ** 2) + 4 * (self.h ** 2)) ** 0.5)
        return f'Area : {area_pyramid}'
    def volume(self):
        volume_pyramid = ((self.a**2) * self.h)/3
        return f'Volume : {volume_pyramid}'



triangle = Triangle(5,12,13,12)
print(triangle.area(), triangle.perimeter())
print('-------------------')
rectangle = Rectangle(5,10)
print(rectangle.area(),rectangle.perimeter())
print('-------------------')
square = Square(5)
print(square.area(), square.perimeter())
print('-------------------')
cube = Cube(5)
print(cube.area(), cube.perimeter(), cube.volume())
print('-------------------')
piramit = Pyramid(5, 12, 13, 12)
print(piramit.area(), piramit.volume())
