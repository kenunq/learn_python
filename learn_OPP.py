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

# Пространство имён класса

x = 1
y = 2
z = 3

class Xyz:
    x = 10
    y = 20
    z = 30

    def info(self):
        # по дефолту имена переменных ищатся в глобальном пространстве
        # если указать self либо название класса, то поиск будет идти внутри класса
        print('Global', x, y, z)
        print('Local', Xyz.x, self.y, Xyz.z)

    @property
    def get_xyz(self):
        print('Global', x, y, z)
        print('Local', Xyz.x, self.y, Xyz.z)

    @classmethod
    def info_class(cls):
        print(cls.x, cls.y, cls.z)

    @staticmethod
    def info_static():
        print(Xyz.x, Xyz.y, Xyz.z)

    def increase_x(self):
        self.x += 2

    def increase_local_x(self):
        Xyz.x += 2

pr1 = Xyz()
pr1.info()
print()
pr1.get_xyz
print()
pr1.info_class()
print()
pr1.info_static()
print()
pr1.increase_x()
print(pr1.x)
print()
pr1.increase_local_x()
print(pr1.x)

#======================================================================================================================







