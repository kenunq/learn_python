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

class Car:
    model = "BMW"
    engine = 1.6

    @staticmethod
    def drive():
        print('Lets go')


car1 = Car()
car1.model = 'Lada'

print(car1.__dict__) # можно посмотреть атрибуты у экземпляра класса
print(Car.__dict__)

#Вызов метода у класса
Car.drive()
getattr(Car, 'drive')()

#Вызов метода у экземпляра класса с помощью установки декоратора @staticmethod
car1.drive()
getattr(car1, "drive")()


#======================================================================================================================














