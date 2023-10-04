class Person:
    name = 'Ivan'
    age  = 30

print(Person.name, Person.age)

# Узнать какие есть атрибуты в классе с помощью __dict__
print(Person.__dict__)

# Получить значение у атрибута name в классе Person
# третим аргументом передаётся число/строка которая вернётся если искомый атрибут не найден
# print(getattr(Person, 'name', 'не нашёл 1'))
# print(getattr(Person, 'nAMe', 'не нашёл 2'))

Person.name = 'Misha'
print(Person.name)

# можно создать атрибут в классе
Person.x = 100
print(Person.x)

# Установить новое значение для атрибута 'x' в классе Person
setattr(Person, 'x', 200)
print(Person.x)
# Так же можно и создать новый атрибут
setattr(Person, 'y', 201)
print(Person.y)

# Удаление атрибута
del Person.x
print(getattr(Person, 'x', 'не нашёл x'))

delattr(Person, 'y')
print(getattr(Person, 'y', 'не нашёл y'))

