# Переопределение Overriding

class Human:

    my_name = 'Adam2'

    def __init__(self, name) -> None:
        print('initialization class Human')
        self.name = name

    def can_walk(self):
        print('Я могу ходить')

    def can_breathe(self):
        print('Я могу дышать')

    def combo(self): # методы можно вызывать внутри другого метода
        self.can_walk()
        self.can_breathe()

class Doctor(Human):

    my_name = 'Ivan2'

    # переопределением называется создание в subclass метода с таким же названием как в родительском классе
    # после данной манипуляции класс Doctor при вызове метода будет использовать переопределенный метод
    def can_breathe(self):
        print('Доктор может дышать')

    # переопределив маг. метод __str__ у класса Doctor, экземпляр doc стал возвращать название класса и своё имя
    def __str__(self) -> str:
        return f"Doctor {self.name}"

hum = Human('Adam')
doc = Doctor('Ivan')

print()

hum.can_breathe()
print(hum.name)
print(hum.my_name)
print(hum)

print()

doc.can_breathe()
print(doc.name)
print(doc.my_name)
print(doc)

print()

hum.combo()

print()

doc.combo()
