# Наследование

# parent
class Human:

    def can_walk(self):
        print('Я могу ходить')

    def can_breathe(self):
        print('Я могу дышать')

# класс Doctor наследуется от родительского класса Human и перенимает все его методы
class Doctor(Human): # subclass

    def can_cure(self):
        print('Я могу лечить')

# класс Ortoped наследуется от родительского класса Doctor а тот в свою очередь от Human
# класс Ortoped возьмёт методы у обоих классов выше по иерархии
class Ortoped(Doctor): # subclass

    def can_cure_bones(self):
        print('Я могу лечить травмы костей')

# класс Architector наследуется от родительского класса Human и перенимает все его методы
class Architector(Human): # subclass

    def can_build(self):
        print('Я могу построить здание')

doc1 = Doctor()
# doc1.can_cure()
# doc1.can_walk()
# doc1.can_breathe()

ort = Ortoped()
# ort.can_cure()
# ort.can_cure_bones
# ort.can_walk
# ort.can_breathe

arc1 = Architector()
# arc1.can_build()

# с помощью функции issubclass проверяем является ли Doctor под классом Human
print(issubclass(Doctor, Human))

# с помощью функции isinstance проверяем является ли doc1 экземпляром класса Doctor
print(isinstance(doc1, Doctor))
# если проверять у родительского класса тоже вернёт True, т.к. функция найдёт Doctor ниже по иерархии
print(isinstance(doc1, Human))
