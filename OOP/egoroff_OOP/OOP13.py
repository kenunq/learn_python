# Полиморфизм это возможность обработки разных объектов
# путём использования метода с одним и тем же названием
# в разных классах

class Rectangle:

    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __str__(self) -> str:
        return f"Rectangle {self.a}x{self.b} ="

    def get_area(self):
        return self.a * self.b

class Square:

    def __init__(self, a) -> None:
        self.a = a

    def __str__(self) -> str:
        return f"Square {self.a}x{self.a} ="

    def get_area(self):
        return self.a ** 2

class Circle:

    def __init__(self, r) -> None:
        self.r = r

    def __str__(self) -> str:
        return f"Circle radius {self.r} ="

    def get_area(self):
        return 3.14 * self.r ** 2
