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



# class Point1:
#     def __init__(self, *args):
#         self.__coords = args
#     # дандер метод __len__ позволяет узнавать количество объектов экземпляра класса
#     # без него при вызове функции len(<экземпляр_класса>) будет возбуждено исключение TypeError
#     def __len__(self):
#         return len(self.__coords)
#
#
# class Point2:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __len__(self):
#         return self.x ** 2 + self.y ** 2
#
#     def __bool__(self):
#         return self.x == self.y
#
#
# p1 = Point1(1,2,3,4)
# print(len(p1))
#
# p2 = Point2(10,10)
# print(len(p2))
# if p2:
#     print('1')
# else:
#     print('2')
#
# p3 = Point2(12,13)
# if p3:
#     print(1)
# else:
#     print(2)


#======================================================================================================================


# class Test:
#     my_attribute = 2 # атрибут класса является общим для всех его экземпляров
#
#     def __init__(self):
#         my_property = 4 # свойство экземпляра является индивидуальным для каждого экземпляра
#
#     def meth(self):
#         # для доступа к атрибутам класса внутри метода можно использовать как ссылку на класс так и на его экземпляр
#         print('test.my_attribute ->', Test.my_attribute)
#         print('self.my_attribute ->', self.my_attribute)
#
#     def set_bound(self):
#         print('значение атрибута класса my_attribute:', getattr(Test, 'my_attribute'),
#               '\nсловарь свойств экземпляра класса:', self.__dict__)
#         # при присваивании значения атрибуту класса через экземпляр класса self,
#         # оператор присваивания создаёт свойство с таким же именем для экземпляра класса
#         self.my_attribute = 11
#         # если использовать ссылку на класс то значение присвоится атрибуту класса
#         # и никакого свойства экземпляра создано не будет
#         # Test.my_attribute = 12
#         print('значение атрибута класса my_attribute:', getattr(Test, 'my_attribute'),
#               '\nсловарь свойств экземпляра класса:', self.__dict__)
#
#
#
#
#
# t1 = Test()
# t1.meth()
#
# t1.set_bound()


#======================================================================================================================

# class Test:
#     def __init__(self, value: int):
#         self.value = value
#
#     @classmethod
#     def __verify_data(cls, other):
#         if not isinstance(other, (int, Test)):
#             raise TypeError('Операнд справа должен иметь тип int или Test')
#         return other if isinstance(other, int) else other.value
#     def __eq__(self, other):
#         """Обрабатывает оператор == и ( != если не переопределён дандер метод __ne__ )"""
#         right_operand_value = self.__verify_data(other)
#         # при вызове != интерпритатор подставит not к результату сравнения ( если не переопределён дандер метод __ne__ )
#         return self.value == right_operand_value
#
#     def __lt__(self, other):
#         """Обрабатывает оператор < и ( > если не переопределён дандер метод __gt__ )"""
#         right_operand_value = self.__verify_data(other)
#         # при вызове > интерпритатор подставит not к результату сравнения ( если не переопределён дандер метод __gt__ )
#         return self.value < right_operand_value
#
#     def __le__(self, other):
#         """Обрабатывает оператор <= и ( => если не переопределён дандер метод __ge__ )"""
#         right_operand_value = self.__verify_data(other)
#         # при вызове => интерпритатор подставит not к результату сравнения ( если не переопределён дандер метод __ge__ )
#         return self.value <= right_operand_value
#
# t1 = Test(20)
# t2 = Test(20)
# # по умолчанию при сравнении экземпляров класса, сравниваются id объектов
# # но если переопределить дандер метод __eq__ можно указать свою логику сравнения
# print(t1 == t2)
# print(t1 != t2)
# print(t1 < t2)
# print(t1 > t2)
# print(t1 <= t2)
# print(t1 >= t2)


#======================================================================================================================

# class DefenedVector:
#     def __init__(self, value):
#         self.__value = value
#
#     def __enter__(self):
#         print('clas DefenedVector def __enter__')
#         # при открытии менеджера контекста делаем поверхностную копию переданого объекта
#         # и присваиваем её в свойство экземпляра класса __temporary,
#         # возвращаем __temporary он попадёт в алиас as defened.
#         # Тем самым мы защищаем изначальный объект т.к. будем работать внутри менеджера контекста с его копией.
#         self.__temporary = self.__value[:]
#         return self.__temporary
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('class DefenedVector def __exit__:', exc_type, exc_val)
#         # при выходе из менеджера контекста проверяем, если небыло никаких исключений то
#         # поэлементно копируем обратно в изначальный объект __value изменённый __temporary
#         # за счёт оператора [:]
#         if exc_type is None:
#             self.__value[:] = self.__temporary
#         return False
#
#
# v1 = [1, 2, 3]
# v2 = [2, 3]
#
# try:
#     # за счёт кастомного менеджера контекста при возникновении исключения список v1 не был изменён частично
#     with DefenedVector(v1) as defened:
#         for i in range(len(defened)):
#             defened[i] += v2[i]
# except IndexError as exc:
#     print(exc)
#
# print('v1:', v1)
#
# try:
#     # при возникновении исключения список v1 был изменён частично
#     for i in range(len(v1)):
#         v1[i] += v2[i]
# except IndexError as exc:
#     print(exc)
#
# print('v1:', v1)


#======================================================================================================================


# Дата классы позволяют определять типизированные атрибуты в которые будут помещены данные
# ниже приведён пример использования дата класса, функция возвращает дата класс
# и появляется возможность обращаться к его атрибутам через точку, при этом IDE посвечивает тип объекта,
# вместо возврата простого словаря и обращения по ключам в которых содержится неизвестный тип данных.

# from dataclasses import dataclass
# @dataclass
# class A:
#     x: int
#     y: str
#     z: dict
#
#
# class B:
#     x = 1
#     y = 'qwe'
#     z = {1: 'a'}
#
#     def with_dataclass(self) -> A:
#         return A(
#             x=self.x,
#             y=self.y,
#             z=self.z,
#         )
#
#     def without_dataclass(self) -> dict:
#         return dict(
#             x=self.x,
#             y=self.y,
#             z=self.z,
#         )
#
#
# b1 = B()
#
# b = b1.with_dataclass()
# print(b.x, b.y, b.z)
#
# b2 = b1.without_dataclass()
# print(b2['x'], b2['y'], b2['z'])

#======================================================================================================================


# from pprint import pprint
# from dataclasses import dataclass
#
# class Thing:
#     def __init__(self, name, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def __repr__(self):
#         print('repr')
#         return f'{self.__class__.__name__}({self.__dict__})'
#
# @dataclass
# class ThingData:
#     name: str
#     weight: int
#     price: float
#
# t = Thing("Учебник по питону", 100, 2100.10)
# print(t)
#
# # Так же в датаклассах уже реализованы дандер методы __init__, __repr__, __eq__ и т.д.
# td1 = ThingData("Учебник по питону", 100, 2100.10)
# # за счёт __repr__ дата классы отображают атрибуты объекта а не адрес в памяти
# print(td1)
#
# td2 = ThingData("Учебник по питону", 100, 2100.10)
# # за счёт __eq__ дата классы сравниваются по значениям атрибутов
# print(f'{td1 == td2 = }')
#
# print('\n\n\n')
# pprint(ThingData.__dict__)


#======================================================================================================================

# from dataclasses import dataclass, field, InitVar
# # декоратор может принимать параметры:
# # frozen=False(default)/True # делает атрибуты класса неизменяемыми (read only, только для чтения)
# @dataclass
# class ThingData2:
#     # если необходимо наоборт исключить из __repr__ атрибут, тогда указываем repr=False в функции field
#     # если необходимо исключить атрибут при сравнии с помощью __eq__, тогда указываем compare=False в функции field
#     made_in: str = field(repr=False, compare=False)
#
#     # если необходимо указать дефолтное значение при использовании функции field, тогда указываем default=<значение>
#     company: str = field(default='Tech Industries')
#
#     # по умолчанию изменяемые типы данных нельзя указывать в датаклассе
#     # для этого необходимо использовать специальную функцию field (если необходимо получить пустой список)
#     # либо указывать их в дандер методе __post_init__ (если необходимо получить заполненный список
#     tech_params: list = field(default_factory=list)
#
#     # tech_params2 указан в атрибутах только для того чтобы __repr__ отображал этот атрибут при принте
#     tech_params2: list = field(init=False) # не передавать атрибут tech_params2 в __init__ класса ThingData2
#
#     #атрибуты дата класса могут принимать значения по умолчанию
#     name: str = 'Notebook'
#     weight: int = 100
#     price: float = 20000.90
#
#     #при анторирование с помощью InitVar , атрибут автоматически попадает в метод __post_init__
#     in_store: InitVar[bool] = True
#
#     #срабатывает после обычного __init__
#     def __post_init__(self, *args, **kwargs):
#         print("def __post_init__", args, kwargs)
#         self.tech_params2 = [1,2]
#
# td3 = ThingData2(made_in="China", name='Macbook', price=12000.90)
# print(td3)
#
#
# td4 = ThingData2(made_in='China', name='Lenovo', price=8999.99)
# print(td4)

#======================================================================================================================

# class Point1:
#     MAX_COORD = 100
#     MIN_COORD = 0
#
# # динамическое создание класса с использованием метакласса
# Point2 = type('Point2', (), {'X': 5, 'Y': 6})
# print(Point1, Point2)
# p2 = Point2()
# print(p2.X)
#
# # динамическое создание класса который наследуется от классов Point и Point2
# Point3 = type('Point3', (Point1, Point2), {})
# print(Point3.MAX_COORD, Point3.X)
#
# # динамическое создание класса с методами
# def method1(self):
#     self.new_propety = 1
#     return self.__dict__
# Point4 = type("Point4", (Point1, Point2), {'method1': method1, 'method2': lambda self: self.MAX_COORD})
# print(Point4().method1(), Point4().method2())

#======================================================================================================================


# # реализация мета класса в виде функции
# def create_class_point(name: str, bases: tuple, attrs: dict):
#     attrs.update({
#         'MAX_COORD': 100,
#         'MIN_COORD': 0
#     })
#     return type(name, bases, attrs)
#
# # реализация мета класса в виде класса
# class CreateClassPoint(type):
#
#     def __new__(cls, name, base, attrs: dict):
#         attrs.update({
#             'MAX_COORD': 100,
#             'MIN_COORD': 0
#         })
#         return type.__new__(cls, name, base, attrs)
#
#
# class Point1(metaclass=create_class_point):
#     def get_coords(self):
#         return 0, 0
#
# class Point2(metaclass=CreateClassPoint):
#     def get_coords(self):
#         return 0,0
#
# p1 = Point1()
# print(p1.MAX_COORD)
# print(p1.get_coords())
#
# p2 = Point2()
# print(p2.MAX_COORD)
# print(p2.get_coords())

#======================================================================================================================

# Множественное наследование

# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__() # Для того, чтобы отработал иницилизатор в классе MixinLog
#
#         print('class goods __init__', Goods.mro())
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f'{self.name}, {self.weight}, {self.price}')
#
#
# class Mixinlog:
#
#     def __init__(self):
#         super().__init__() # Для того, чтобы отработал иницилизатор в классе MixinLog2
#         print("class MixinLog def __init__", Mixinlog.mro())
#         self.id = 152973
#
#     def save_sell_log(self):
#         print(f'{self.id}, товар был продан 12:00')
#
# class Mixinlog2:
#     def __init__(self):
#         print('class MixinLog2 def __init__', Mixinlog2.mro())
#         self.id = 923432
#
#     def save_sell_log2(self):
#         print(f'{self.id}: товар был продан в 13:00 часов')
#
#
# class NoteBook(Goods, Mixinlog, Mixinlog2):
#     pass
#
# n1 = NoteBook('qwe', 100, 1000)
# n1.print_info()
# n1.save_sell_log()
# n1.save_sell_log2()

# т.к. класс Goods указан первым в списке наследования MRO,
# все переданные аргументы при создании экземпляра класса NoteBook
# попадут в метод __init__ класса Goods, и за счёт того что мы указали super().__init__()
# сначала вызовется метод __init__ у класса MixinLog, который является следующим по списку в MRO
# и т.к. в этом методе так же указан super().__init__() будет вызван метод __init__ у класса MixinLog2
# и как будет выполнен __init__ в MixinLog2, интерпритатор вернётся к __init__ в MixinLog выполнит его,
# и только потом вернётся к __init__ в Goods и так же выполнит его


#======================================================================================================================

# class Women:
#     def __init__(self):
#         print('class Women def __init__', self.Meta.ordering)
#
#     title = 'объект класса для поля title'
#     photo = 'объект класса для поля photo'
#     ordering = 'объект класса для поля ordering'
#
#     # за счёт вложенного класса можно определять отдельное пространство имён
#     # в котором можно создавать атрибуты с таким же именем как и в классе обёртке
#
#     class Meta: #при создании экземпляра класса Women, экземпляр класса Meta НЕ создаётся.
#         ordering = ['id']
#
# print(Women.ordering)
# print(Women.Meta.ordering)
#
# w = Women()
# print(w.ordering)
# print(w.Meta.ordering)

#======================================================================================================================

class Point3DWithProperty:


    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")


    # Если необходимо реализовывать много геттеров/сеттеров/делитеров
    # возможно стоит реализовать один класс дескриптор
    # для замены огромного количества проперти которые будут загромождать код
    @property
    def x(self):
        return self._x


    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self._x = coord


    @property
    def y(self):
        return self._y


    @x.setter
    def y(self, coord):
        self.verify_coord(coord)
        self._y = coord


    @property
    def z(self):
        return self._z


    @x.setter
    def z(self, coord):
        self.verify_coord(coord)
        self._z = coord


# Дескриптор данных, служит для получения/установки/удаления данных как замена property
class IntDescriptor:
    # self - Ссылка на экземпляр класса, то есть IntDescriptor()
    # owner - Ссылка на класс Point3DWithDescriptor
    # name - имя атрибута, то есть "x", "y", "z"
    def __set_name__(self, owner, name):
        """Вызывается при создании экземпляра класса IntDescriptor"""
        self.name = '_' + name

    # self - Ссылка на экземпляр класса, то есть IntDescriptor()
    # instance - Ссылка на экземпляр класса Point3DWithDescriptor
    # owner - Ссылка на класс Point3DWithDescriptor
    def __get__(self, instance, owner):
        """Вызывается в момент чтения значения"""
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)

    # self - Ссылка на экземпляр класса, то есть IntDescriptor()
    # instance - Ссылка на экземпляр класса Point3DWithDescriptor
    # value - Значение для присвоения
    def __set__(self, instance, value):
        """Вызывается в момент присваивания значения"""
        self.verify_coord(value)
        print(f'IntDescriptor __set__: {self.name} = {value}')
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")


class Point3DWithDescriptor:
    # при создании экземпляров дескриптора в нём появляются атрибуты "_x", "_y", "_z"
    x = IntDescriptor()
    y = IntDescriptor()
    z = IntDescriptor()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p1 = Point3DWithProperty(1, 2, 3)
print('Point3DWithProperty __dict__:', p1.__dict__)  # {'_x': 1, '_y': 2, '_z': 3}

p2 = Point3DWithDescriptor(1, 2, 3)
print('Point3DWithDescriptor __dict__:', p2.__dict__)  # {'_x': 1, '_y': 2, '_z': 3}
































