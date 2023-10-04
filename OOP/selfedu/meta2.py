# реализация мета класса в виде функции
def create_class_point(name, base, attrs: dict):
    attrs.update({
        'MAX_COORD': 100,
        'MIN_COORD': 0
    })
    return type(name, base, attrs)


# реализация мета класса в виде класса
class CreateClassPoint(type):
    def __new__(cls, name, base, attrs: dict):
        attrs.update({
            'MAX_COORD': 100,
            'MIN_COORD': 0
        })
        return type.__new__(cls, name, base, attrs)

    # def __init__(cls, name, base, attrs: dict):
    #     super().__init__(name, base, attrs)
    #     cls.MAX_COORD = 100
    #     cls.MIN_COORD = 0


class Point1(metaclass=create_class_point):
    def get_coords(self):
        return 0, 0


class Point2(metaclass=CreateClassPoint):
    def get_coords(self):
        return 0, 0


p1 = Point1()
print(p1.MAX_COORD)
print(p1.get_coords())

p2 = Point2()
print(p2.MAX_COORD)
print(p2.get_coords())
