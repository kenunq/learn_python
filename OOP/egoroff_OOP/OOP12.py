# Магический метод __bool__

class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __len__(self):
        print('call __len__')
        return abs(self.x - self.y)

    # можно переопределить метод __bool__
    def __bool__(self):
        print('call __bool__')
        return self.x != 0 or self.y != 0

p1 = Point(1, 2)
p2 = Point(0, 0)
print(bool(p1), bool(p2))