class Point1:
    MAX_COORD = 100
    MIN_COORD = 0


# динамическое создание класса с использованием метакласса
Point2 = type('Point2', (), {'X': 5, 'Y': 6})
print(Point1, Point2)


# динамическое создание класса который наследуется от классов Point и Point2
Point3 = type('Point3', (Point1, Point2), {})
print(Point3.MAX_COORD, Point3.Y, Point3.mro())


# динамическое создание класса с методами
def method1(self):
    self.new_property = 'Hello'
    return self.__dict__
Point4 = type('Point4', (Point1, Point2), {'method1': method1, 'method2': lambda self: self.MAX_COORD})
print(Point4().method1(), Point4().method2())
