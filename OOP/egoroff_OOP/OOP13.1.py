from OOP13 import Rectangle, Square, Circle

rect1 = Rectangle(3, 4)
rect2 = Rectangle(12, 5)

sq1 = Square(5)
sq2 = Square(7)

circle1 = Circle(3)
circle2 = Circle(2)

figures = [rect1, rect2, sq1, sq2, circle1, circle2]

for figure in figures:
    print(figure, figure.get_area())
