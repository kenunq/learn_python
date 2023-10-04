# Магические методы __eq__, __hash__

class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, Point) and self.x == __o.x and self.y == __o.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))

p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

# до переопределения метода __eq__ сравнение шло по id объектов и работал метод __hash__
# после переопределения метода __eq__ сравнение идёт по значениям объектов и не работает метод __hash__
print(id(p1), id(p2))
print(p1 == p2)

# после переопределения метода __hash__ он заработает
print(hash(p1) == hash(p2), hash(p2) == hash(p3))
