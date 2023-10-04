class Point1:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # переопределение дандер метода __hash__ позволяет определять хэш на основе свойств экземпляра класса
    def __hash__(self):
        return hash((self.x, self.y))


p1 = Point1(1, 2)
p2 = Point1(1, 2)
print(p1 == p2, hash(p1) == hash(p2), hash(p1), hash(p2))

p1 = Point2(1, 2)
p2 = Point2(1, 2)
print(p1 == p2, hash(p1) == hash(p2), hash(p1), hash(p2))
