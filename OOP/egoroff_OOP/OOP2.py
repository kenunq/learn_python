class Car:
    model = 'BMW'
    engine = 1.6

    @staticmethod
    def drive():
        print('Lets Go')



car1 = Car()
car1.model = 'Lada'

print(car1.__dict__) # можно посмотреть атрибуты у экземпляра класса
print(Car.__dict__)

Car.drive() # вызов метода у класса
getattr(Car, 'drive')()

car1.drive() # вызов метода у экземпляра класса с помощью установки декоратора @staticmethod
getattr(car1, 'drive')()
