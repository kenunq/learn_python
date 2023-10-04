# Классы

# Принято что название класса пишется с большой буквы

# class Dog():
#     '''Простая модель собаки'''
#     # функции внутри класса называются методами
#     # метод __init__ срабатывает когда создаётся экземпляр класса
#     def __init__(self, name, age):
#         '''Инициализируем атрибуты имя и возраст'''
#         self.name = name
#         self.age = 'Возраст: ' + str(age) + ' Лет'
#         print('Экземпляр собаки создан.')

#     def sit(self):
#         '''Собака будет садиться по команде'''
#         print(self.name.title() + ' сел')

#     def jump(self):
#         '''Собака будет прыгать по команде'''
#         print(self.name.title() + ' сделал прыжок')

#     def gav(self):
#         '''Собака будет гавкать по команде'''
#         print(self.name.title() + ' Гав-Гав')

# первый объект dog1
# dog1 = Dog('Topik', 5)
# print(dog1.name, dog1.age)

# второй объект my_dog2
# dog2 = Dog('Nick', 7)
# print(dog2.name, dog2.age)

# методы класса
# dog1.sit()
# dog2.jump()
# dog2.gav()



# Классы и экземпляры
class Car():
    '''Класс по созданию автомобиля'''

    def __init__(self, company, model, year):
        '''Здесь происходит инициализация атрибутов автомобиля'''
        self.company = company
        self.model = model
        self.year = year
        self.odometer_reading = 0 # атрибут по умолчанию равен 0
        print('Экземпляр автомобиля создан')

    def description_name(self):
        '''Возвращаем описание автомобиля'''
        desc =  str(self.year) + ' ' + self.company + ' ' + self.model
        return desc.title()

    def read_odometer(self):
        '''Выводим пробег автомобиля'''
        print('Пробег этого авто составляет: ' + str(self.odometer_reading) + 'км')

    def update_odometer(self, km):
        '''Устанавливаем значение на одометре'''
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print('Не стоит скручивать пробег!')

    def increment_odometer(self, km):
        '''Увеличиваем показания одометра на заданную величину'''
        if km >= 0:
            self.odometer_reading += km

# car1 = Car('audi', 'a4', 2017)
# print(car1.description_name()) # читаем описание класса
# car1.update_odometer(5) # значение по заводу
# car1.increment_odometer(120) # пробег который прошла машина
# car1.read_odometer() # метод считывания данных

# определяем вспомогательный класс
class Battery():
    '''Простая модель аккумулятора для электромобиля'''
    def __init__(self, battery=100):
        self.battery = battery

    def description_battery(self):
        '''Выводит информацию о мощности батареи'''
        print('Этот автомобиль имеет батарею мощностью ' + str(self.battery) + ' Киловат')

# Наследование
# в скобках указываем наследуемый класс
class Electric_Car(Car):
    '''Аспекты для электромобиля'''
    # перечисляем все параметры родителя
    def __init__(self, company, model, year):
        '''Инициализация атрибутов класса родителя'''
        # функция super() позволяет связать родителя и ребёнка
        # после связывания дочерний класс получает все атрибуты родительского класса
        super().__init__(company, model, year)
        # создаём экземпляр класса Battery внутри класса Electric_Car
        # атрибут battery равен классу Battery
        self.battery = Battery()

    # изменяем метод с названием как у родительского под ребёнка
    def description_name(self):
        '''Переопределение родительского метода'''
        desc = str(self.year) + ' ' + self.model
        return desc.title()

tesla = Electric_Car('tesla', 's', 2018)
# print(tesla.description_name()) # вызываем метод из класса Electric_Car
# с помощью атрибута battery внутри класса Electric_Car вызываем метод description_battery внутри класса Battery
# tesla.battery.description_battery()
