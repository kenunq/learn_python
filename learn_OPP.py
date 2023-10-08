# принято, что название классов пишутся с большой буквы

# class Dog():
#     '''простая модель собаки'''
#     #функции внутри класса принято называть методами
#     #метод __init__ срабатывает при создании класса
#     def __init__(self, name, age):
#         self.name = name
#         self.age = 'Возраст: ' + str(age) + ' лет.'
#         print('Экземпляр класса создан')
#
#     def sit(self):
#         print(self.name.title() + " сел.")
#
#     def jump(self):
#         print(self.name.title() + " прыгнул.")
#
#     def voice(self):
#         print(self.name.title() + " гавкнул.")
#
# shobaka = Dog("KIKI", 5)
# print(shobaka.name, shobaka.age)
#
# shobaka2 = Dog("KUKU", 7)
# print(shobaka2.name, shobaka2.age)
#
# shobaka2.sit()
# shobaka.jump()
# shobaka.voice()



# class Car():
#     def __init__(self, company, model, year):
#         self.company = company
#         self.model = model
#         self.year = year
#         self.probeg = 0
#         print('Экземпляр машины создан')
#
#     def decription_car(self):
#         '''Возвращаем описание автомобиля'''
#         description: str = self.company + ' ' + self.model + ' ' + str(self.year)
#         return description.title()
#
#     def read_probeg(self):
#         '''Выводим пробег автомобиля'''
#         print('Пробег этого автомобиля составляет: ' + str(self.probeg) + ' км.')
#
#     def set_probeg(self, km):
#         '''Устанавливаем значение на одометре'''
#         if km >= self.probeg:
#             self.probeg = km
#         else:
#             print('Не надо скручивать пробег')
#     def increment_probeg(self, km):
#         '''Увеличиваем показания одометра на заданную величину'''
#         self.probeg += km
#
#
#
# merc = Car("Mercedes", 'cls', 2019)
# print(merc.decription_car())
# merc.read_probeg()
# merc.set_probeg(20)
# merc.set_probeg(1)
# merc.read_probeg()
# merc.increment_probeg(5)
# merc.read_probeg()
#
# # определяем вспомогательный класс
# class Battery():
#     '''Простая модель аккумулятора для электромобиля'''
#     def __init__(self, battery=100):
#         self.battery = battery
#
#     def description_battery(self):
#         '''Выводит информацию о мощности батареи'''
#         print('Этот автомобиль имеет батарею мощностью ' + str(self.battery) + ' Киловат')
#
# #наследование
# class Electric_Car(Car):
#     '''Аспекты для электромобиля'''
#
#     def __init__(self, company, model, year):
#         # функция super() позволяет связать родителя и ребёнка
#         # после связывания дочерний класс получает все атрибуты родительского класса
#         super().__init__(company, model, year)
#         # создаём экземпляр класса Battery внутри класса Electric_Car
#         # атрибут battery равен классу Battery
#         self.battery = Battery()
#
#     # изменяем метод с названием как у родительского под ребёнка
#     def description_name(self):
#         '''Переопределение родительского метода'''
#         desc = str(self.year) + ' ' + self.model
#         return desc.title()
#
# tesla = Electric_Car("Tesla", "Model x", 2020)
# print(tesla.description_name())
# tesla.increment_probeg(10)
# tesla.read_probeg()

#======================================================================================================================

# class Person:
#     name = 'Ivan'
#     age = 18
#
# print(Person.name, Person.age)
#
# # Узнать какие есть атрибуты в классе с помощью __dict__
# print(Person.__dict__)
#
# # Получить значение у атрибута name в классе Person
# # третим аргументом передаётся число/строка которая  вернётся если искомый атрибут не найден
# # print(getattr(Person, 'name', 'не нашёл 1')) # --> Ivan
# # print(getattr(Person, 'nAMe', 'не нашёл 2')) # -> не нашёл 2
#
#
# Person.name = "Yariq"
# print(Person.name)
#
# # можно создать атрибут в классе
# Person.x = 100
# print(Person.x)
#
# # Установить новое значение для атрибута 'x' в классе Person
# setattr(Person, "x", 200)
# print(Person.x)
#
# # Так же можно и создать новый атрибут
# setattr(Person, 'y', 201)
# print(Person.y)
#
# # Удаление атрибута
# del Person.x
# print(getattr(Person, 'x', 'не нашёл x'))
#
# delattr(Person, 'y')
# print(getattr(Person, 'y', 'не нашёл y'))

#======================================================================================================================

# class Car:
#     model = "BMW"
#     engine = 1.6
#
#     @staticmethod
#     def drive():
#         print('Lets go')
#
#
# car1 = Car()
# car1.model = 'Lada'
#
# print(car1.__dict__) # можно посмотреть атрибуты у экземпляра класса
# print(Car.__dict__)
#
# #Вызов метода у класса
# Car.drive()
# getattr(Car, 'drive')()
#
# #Вызов метода у экземпляра класса с помощью установки декоратора @staticmethod
# car1.drive()
# getattr(car1, "drive")()


#======================================================================================================================

# class Cat:
#
#     def __init__(self, name, breed, age, color):
#         print(f"Hello new object is {self, name, breed, age, color}")
#         self.name = name
#         self.bred = breed
#         self.age = age
#         self.color = color
#
# cat1 = Cat("Maw", "Egypet", 3, 'gray')

#======================================================================================================================

#Моносостояние для всех экземпляров

# class Cat:
#
#     __shared_attr = {
#         'breed': 'Pers',
#         'color': 'Black'
#     }
#
#     def __init__(self):
#         # присвоив словарь с дефолтными атрибутами в self.__dict__ применяем атрибуты в словаре ко всем экземплярам класса
#         # и даже при изменении атрибута он изменится у всех экземпляров
#         self.__dict__ = Cat.__shared_attr
#         self.age = 12
#     def qwe(self):
#         print(123)
#
# d = Cat()
# b = Cat()
#
# b.breed = 'Egypet'
#
# print(d.breed, d.color)
# print(b.breed, b.color)
# print(b.__dict__)

#======================================================================================================================

#Инкапсуляция
# Публичные, Приватные, Защищённые атрибуты и методы

# Публичные - без нижних подчёркиваний в начале
# Защищённые - с одним подчёркиванием в начале (говорит о том что атрибут не стоит использовать вне класса)
# Приватные - с двумя подчёркиваниями в начале (запрещает использовать вне класса, ошибка - AttributeError)

# class BankAccount:
#     def __init__(self, name, balance, passport):
#         self.name = name
#         self.__name = name
#         self.__balance = balance
#         self.__passport = passport
#
#     def __print_data(self):
#         print(self.__name, self.__balance, self.__passport)
#
# person = BankAccount('Ivan', 4231, 234154352134)
# print(dir(person))
# person._BankAccount__passport = 31231
# print(person.__dict__) # -> {'name': 'Ivan', '_BankAccount__name': 'Ivan', '_BankAccount__balance': 4231, '_BankAccount__passport': 234154352134}
# print(person._BankAccount__passport)

#======================================================================================================================

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#
#     @property # -> превращает метод в свойство по умолчанию getter
#     def my_balance(self):
#         print('getter')
#         return self.__balance
#
#     #методы getter, setter, deleter называются одним имененм
#     @my_balance.setter
#     def my_balance(self, value):
#         print('setter')
#         if isinstance(value, (int,float)):
#             self.__balance = value
#         else:
#             raise ValueError('Значение должно быть числом')
#
#     @my_balance.deleter
#     def my_balance(self):
#         print('deleter')
#         del self.__balance
#
#
# person = BankAccount('Kiril', 140)
# print(person.my_balance)
# person.my_balance  = 500
# print(person.my_balance)
# del person.my_balance
# # print(person.my_balance)


#======================================================================================================================


# class Square:
#     def __init__(self,s):
#         self.__side = s
#         self.__area = None
#
#     @property
#     def side(self):
#         return self.__side
#
#     @side.setter
#     def side(self, value):
#         self.__side = value
#         self.__area = None
#
#     @property
#     def area(self):
#         if self.__area == None:
#             print('calculate area')
#             self.__area = self.__side ** 2
#         return self.__area
#
# b1 = Square(5)
# print(b1.side)
# print(b1.area)
# b1.side = 15
# print(b1.side)
# print(b1.area)

#======================================================================================================================

# # Пространство имён класса
#
# x = 1
# y = 2
# z = 3
#
# class Xyz:
#     x = 10
#     y = 20
#     z = 30
#
#     def info(self):
#         # по дефолту имена переменных ищатся в глобальном пространстве
#         # если указать self либо название класса, то поиск будет идти внутри класса
#         print('Global', x, y, z)
#         print('Local', Xyz.x, self.y, Xyz.z)
#
#     @property
#     def get_xyz(self):
#         print('Global', x, y, z)
#         print('Local', Xyz.x, self.y, Xyz.z)
#
#     @classmethod
#     def info_class(cls):
#         print(cls.x, cls.y, cls.z)
#
#     @staticmethod
#     def info_static():
#         print(Xyz.x, Xyz.y, Xyz.z)
#
#     def increase_x(self):
#         self.x += 2
#
#     def increase_local_x(self):
#         Xyz.x += 2
#
# pr1 = Xyz()
# pr1.info()
# print()
# pr1.get_xyz
# print()
# pr1.info_class()
# print()
# pr1.info_static()
# print()
# pr1.increase_x()
# print(pr1.x)
# print()
# pr1.increase_local_x()
# print(pr1.x)

#======================================================================================================================


# Магические методы __str__ и __repr__ служат для того что бы объекты были более наглядны
# например без маг методов print(Экземпляр класса) выдаст: <__main__.Lion object at 0x0000018684AC5130>
# с магическим методом print(Экземпляр класса) выдаст то что вы укажете в return

# class Lion:
#
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'The object Lion - {self.name}'
#
#     def __str__(self):
#         return f'Lion - {self.name}'
#
# q = Lion("Akar")
# print(q)


#======================================================================================================================

# Магические методы

# | Оператор | Метод оператора           |
# | x + y    | __add__(self, other)      |
# | x - y    | __sub__(self, other)      |
# | x * y    | __mul__(self, other)      |
# | x / y    | __truediv__(self, other)  |
# | x // y   | __floordiv__(self, other) |
# | x % y    | __mod__(self, other)      |

# | Оператор | Метод оператора            |
# | x += y   | __iadd__(self, other)      |
# | x -= y   | __isub__(self, other)      |
# | x *= y   | __imul__(self, other)      |
# | x /= y   | __itruediv__(self, other)  |
# | x //= y  | __ifloordiv__(self, other) |
# | x %= y   | __imod__(self, other)      |

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def __add__(self, other): # метод, когда экземпляр класса при мат. операции находится слева
#         #число слева это self число справа это other
#         print('вызов __add__')
#         if isinstance(other, BankAccount):
#             print('условие if isinstance(other, BankAccount): выполнено')
#             return other.balance + self.balance
#         if isinstance(other, (int, float)):
#             print('условие if isinstance(other, (int, float)): выполнено')
#             return self.balance + other
#
#     def __radd__(self, other):
#         print('вызов __radd__')
#         return self + other
#
#
# ba1 = BankAccount('Bob', 200)
# print(ba1.balance + 100)
#
# print(ba1 + 100) # Если не создаём маг. метод __add__ получаем ошибку TypeError
#
# # при вызове в таком порядке сначало вызывается __radd__ который меняет местами аргументы, затем вызывается __add__
# print(100 + ba1) # Если не создаём маг. метод __radd__ получаем ошибку TypeError
#
# ba2 = BankAccount('Ivan', 400)
# print(ba1+ba2)


#======================================================================================================================

# Магические методы __eq__, __hash__

# class Point:
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return isinstance(other, Point) and self.x == other.x and self.y == other.y
#
#     def __hash__(self):
#         return hash((self.x, self.y))
#
#
# p1 = Point(1,2)
# p2 = Point(1,2)
# p3 = Point(3,4)
#
# # до переопределения метода __eq__ сравнение шло по id объектов и работал метод __hash__
# # после переопределения метода __eq__ сравнение идёт по значениям объектов и не работает метод __hash__
# print(id(p1), id(p2))
# print(p1 == p2)
#
# # после переопределения метода __hash__ он заработает
# print(hash(p1) == hash(p2), hash(p2) == hash(p3))



#======================================================================================================================
#
# # Магический метод __bool__
#
# class Point:
#
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y
#
#
#     def __len__(self):
#         print('call __len__')
#         return abs(self.x - self.y)
#
#     def __bool__(self):
#         print('call __bool__')
#         return self.x != 0 or self.y != 0
#
#
# p1 = Point(1,2)
# print(len(p1))
#
# p2 = Point(0, 0)
# print(bool(p1), bool(p2))


#======================================================================================================================

# Полиморфизм это возможность обработки разных объектов
# путём использования метода с одним и тем же названием
# в разных классах

# class Rectangle:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def __str__(self):
#         return f'Reactangle {self.a}x{self.b}='
#
#     def get_area(self):
#         return self.a * self.b
#
# class Square:
#
#     def __init__(self, a):
#         self.a = a
#
#     def __str__(self):
#         return f'Square {self.a}**2='
#
#     def get_area(self):
#         return self.a**2
#
# class Circle:
#     def __init__(self, r):
#         self.r = r
#
#     def __str__(self):
#         return f'Circle 3.14 * {self.r} ** 2='
#
#     def get_area(self):
#         return 3.14 * self.r ** 2
#
# rect1 = Rectangle(3,5)
# rect2 = Rectangle(10,20)
#
# sq1 = Square(5)
# sq2 = Square(10)
#
# cir1 = Circle(4)
# cir2 = Circle(5)
#
# figures = [rect1,rect2,sq1,sq2,cir1,cir2]
# for i in figures:
#     print(i.get_area()) #используется одно и тоже название функции, но по факту используются разные функции


#======================================================================================================================

# Магические методы __getitem__, __setitem__, __delitem__

# class Vector:
#
#     def __init__(self, *args):
#         self.values = list(args)
#
#     def __repr__(self):
#         return str(self.values)
#
#     def __getitem__(self, item):
#         print('get index', item)
#         if item < len(self.values):
#             return self.values[item]
#         else:
#             print('Индекс вышел за границы листа')
#
#     def __setitem__(self, key, value):
#         print('get index', key)
#         if key < len(self.values):
#             self.values[key] = value
#         elif key > len(self.values):
#             diff = key - (len(self.values)-1)
#             self.values.extend(['-'] * diff)
#             self.values[key] = value
#         else:
#             raise IndexError("Индекс вышел за границы листа")
#
#     def __delitem__(self, index):
#         print('del index:', index)
#         if index < len(self.values):
#             del self.values[index]
#         else:
#             raise IndexError('Индекс вышел за границы коллекции')
#
# v1 = Vector(5,4,6,6,7,3)
# print(v1[1])
#
# v1[10] = 10
# print(v1)
#
# del v1[1]
# print(v1)


#======================================================================================================================

# Наследование

# parent
# class Human:
#
#     def can_walk(self):
#         print('Я умею ходить')
#
#     def can_breathe(self):
#         print('Я могу дышать')
#
# #класс доктор наследуется от класса человек и принимает все его методы
#
# class Doctor(Human):
#
#     def can_cure(self):
#         print("Я могу лечить")
#
# # класс ортопед наследуется от родительского класса доктор, а тот в свою очередь от класса человек
# #ортопед возьмет методы у обоих классов выше по иерархии
# class Ortoped(Doctor):
#
#     def can_cure_bones(self):
#         print('Я могу лечить травмы костей')

#Класс архитектор наследуется от класса человек, и принимает все его методы
# class Architector(Human):
#
#     def can_build(self):
#         print('Я могу строить')
#
#
# doc1 = Doctor()
# # doc1.can_walk()
# # doc1.can_breathe()
# # doc1.can_cure()
#
# ort = Ortoped()
# # ort.can_walk()
# # ort.can_cure()
# # ort.can_breathe()
# # ort.can_cure_bones()
#
# arc = Architector()
# # arc.can_walk()
# # arc.can_breathe()
# # arc.can_build()
#
# # с помощью функции issubclass проверяем является ли Doctor под классом Human
# print(issubclass(Doctor, Human)) # -> True
#
# # с помощью функции isinstance проверяем является ли doc1 экземпляром класса Doctor
# print(isinstance(doc1, Doctor)) # -> True
#
# print(isinstance(doc1, Human)) # -> True

#======================================================================================================================

# Переопределение Overriding

# class Human:
#     my_name = 'Aleksey2'
#
#     def __init__(self, name):
#         print('init Human')
#         self.name = name
#
#     def can_walk(self):
#         print('Я могу ходить')
#
#     def can_breathe(self):
#         print('Я могу дышать')
#
#     def combo(self): # методы можно вызывать внутри другого метода
#         self.can_walk()
#         self.can_breathe()
#
# class Doctor(Human):
#     name = 'Ivan2'
#
#     # переопределением называется создание в subclass метода с таким же названием как в родительском классе
#     # после данной манипуляции класс Doctor при вызове метода будет использовать переопределенный метод
#     def can_breathe(self):
#         print('Доктор может дышать')
#
#     # переопределив маг. метод __str__ у класса Doctor, экземпляр doc стал возвращать название класса и своё имя
#     def __str__(self):
#         return f'Doctor {self.name}'
#
#
# hum = Human('Adam')
# doc = Doctor('Ivan')
#
# print()
#
# hum.can_breathe()
# print(hum.name)
# print(hum.my_name)
# print(hum)
#
# print()
#
# doc.can_breathe()
# print(doc.name)
# print(doc.my_name)
# print(doc)

#======================================================================================================================

# Наследование, Расширение класса

# class Person:
#
#     def breathe(self):
#         print('Человек дышит')
#
#     def sleep(self):
#         print('Человек спит')
#
#     def combo(self):
#         self.breathe()
#         # проверить присутствует ли атрибут walk в данном классе Person
#         if hasattr(self, 'walk'):
#             self.walk()
#         self.sleep()
#         if hasattr(self, 'age'):
#             print(self.age)
#
#
# class Doctor(Person):
#
#     age = 28
#
#     def breathe(self):
#         print('Доктор дышит')
#
#     def walk(self):
#         print('Доктор ходит')
#
#     def sleep(self):
#         print('Доктор спит')
#
# p = Person()
# p.combo()
# print('-' * 15)
#
# d = Doctor()
# d.combo()


#======================================================================================================================

# Множественное наследование

# class Doctor:
#
#     def can_cure(self):
#         print('Я доктор, я умею лечить')
#
#     def can_build(self):
#         print('Я доктор, я тоже умею строить')
#
# class Builder:
#
#     def can_build(self):
#         print('Я строитель, я умею строить')
#
# # порядок родительских классов имеет значение
# # при вызове can_build пайтон сначало пойдёт в Doctor
# # и если найдёт там can_build то не пойдёт во второй класс Builder
# class Person(Doctor, Builder):
#     pass
#
#     # def can_build(self):
#     #     print('Я человек, я тоже умею строить')
#
#
# class Person2(Builder, Doctor):
#     pass
#
#     # def can_build(self):
#     #     print('Я человек, я тоже умею строить')
#
# print('Person порядок поиска:', Person.__mro__) # порядок поиска в родительских классах при вызове класса Person
# print('Person2 порядок поиска:', Person2.__mro__)
#
# p = Person()
# p.can_cure()
# p.can_build()
# print('-'*25)
# p2 = Person2()
# p2.can_cure()
# p2.can_build()


#======================================================================================================================

# import random
#
# class BingoCage:
#
#     def __init__(self, items):
#         self._items = items
#         random.shuffle(self._items)
#
#     def pick(self):
#         try:
#             return self._items.pop()
#         except IndexError:
#             raise LookupError('Pick from empty BingoCage')
#
#     # определение дандер метода __call__ в классе позволяет делать экземпляр класса вызываемым объектом
#     def __call__(self):
#         print('class BingoCage def __call__')
#         print(self._items)
#         return self.pick()
#
#
# bc = BingoCage([1,2,3,4,5,6,7,8,9,0])
# print(bc())
# print(bc())
# print(bc())


#======================================================================================================================

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)
#
#     # определение дандер методов __getitem__, __setitem__, __delitem__
#     # позволяет обращатся к экземпляру класса как к последовательности по индексу с помощью квадратных скобок
#     def __getitem__(self, item):
#         if 0 <= item < len(self.marks):
#             return self.marks[item]
#         raise IndexError('Неверный индекс')
#
#     def __setitem__(self, item, value):
#         if not isinstance(value, int) or item < 0:
#             raise TypeError("Индекс должен быть целым положительным числом")
#         if item >= len(self.marks):
#             offset = item + 1 - len(self.marks)
#             self.marks += [None] * offset
#         self.marks[item] = value
#
#     def __delitem__(self, item):
#         if not isinstance(item, int):
#             raise TypeError("Индекс должен быть целым положительным числом")
#         del self.marks[item]
#
#
# s1 = Student("ivan", [1,2,3,4,5,6,7,8,9])
# print(s1[0])
#
# s1[0] = 0
# print(s1[0])
# del s1[0]
# print(s1[0])


#======================================================================================================================

# class Point1:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
# class Point2:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y
#
#     # переопределение дандер метода __hash__ позволяет определять хэш на основе свойств экземпляра класса
#     def __hash__(self):
#         return hash((self.x, self.y))
#
#
# p1 = Point1(1, 2)
# p2 = Point1(1, 2)
# print(p1 == p2, hash(p1) == hash(p2), hash(p1), hash(p2))
#
# p1 = Point2(1, 2)
# p2 = Point2(1, 2)
# print(p1 == p2, hash(p1) == hash(p2), hash(p1), hash(p2))


#======================================================================================================================

# class Range:
#     def __init__(self, start=0, stop=None, step=1):
#         if not stop:
#             self.start = 0
#             self.stop - stop
#         else:
#             self.start = start
#             self.stop = stop
#         if step == 0:
#             raise ValueError(f'{self.__class__.__name__}() arg 3 must not be zero')
#         self.step = step
#
#     def __iter__(self):
#         self.value = self.start - self.step
#         return self
#
#     def __next__(self):
#         if self.value + self.step < self.stop:
#             self.value += self.step
#             return self.value
#         raise StopIteration
#
#     def __repr__(self):
#         return f'{self.__class__.__name__}({self.start}, {self.stop}{", " + str(self.step) if self.step > 1 else ""})'
#
#
# print(Range(2,11,3))
# print(list(Range(2,11,3)))
#
#
# print(range(2, 11, 3))
# print(list(range(2, 11, 3)))
# r = Range(2, 11, 3)
# r = iter(r)
# print(next(r))
# print(next(r))
# print(next(r))



#======================================================================================================================






