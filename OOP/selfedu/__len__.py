class Point1:
    def __init__(self, *args):
        self.__coords = args
    
    # дандер метод __len__ позволяет узнавать количество объектов экземпляра класса
    # без него при вызове функции len(<экземпляр_класса>) будет возбуждено исключение TypeError
    def __len__(self):
        return len(self.__coords)


class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __len__(self):
        print('__len__')
        return self.x * self.x + self.y * self.y
    
    # дандер метод __bool__ позволяет переопределять поведение по умолчанию
    def __bool__(self):
        print('__bool__')
        return self.x == self.y


p1 = Point1(1, 2, 3)
print(len(p1))

p2 = Point2(10, 10)
if p2:
    print('Объект p2 даёт True')
else:
    print('Объект p2 даёт False')

p3 = Point2(5, 10)
if p3:
    print('Объект p3 даёт True')
else:
    print('Объект p3 даёт False')
