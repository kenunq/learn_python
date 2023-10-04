# Множественное наследование

class Doctor:

    def can_cure(self):
        print('Я доктор, я умею лечить')

    def can_build(self):
        print('Я доктор, я тоже умею строить')

class Builder:

    def can_build(self):
        print('Я строитель, я умею строить')

# порядок родительских классов имеет значение
# при вызове can_build пайтон сначало пойдёт в Doctor
# и если найдёт там can_build то не пойдёт во второй класс Builder
class Person(Doctor, Builder):
    pass

    # def can_build(self):
    #     print('Я человек, я тоже умею строить')

class Person2(Builder, Doctor):
    pass

    # def can_build(self):
    #     print('Я человек, я тоже умею строить')

print('Person порядок поиска:', Person.__mro__) # порядок поиска в родительских классах при вызове класса Person
print('Person2 порядок поиска:', Person2.__mro__)

p = Person()
p.can_cure()
p.can_build()
print('-'*25)
p2 = Person2()
p2.can_cure()
p2.can_build()
