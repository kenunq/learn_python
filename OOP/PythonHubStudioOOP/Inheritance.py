# Полиморфизм это разное поведение одного и того же метода в разных классах

# классы A, B суперклассы т.к. не от кого не наследуются
class A():
    def method(self):
        print('class A')

class B():
    def method(self):
        print('class B')

# дочернему классу C доступны методы родительского класса B
class C(B):
    def method(self):
        print('class C')

# дочернему классу D доступны методы родительских классов C, A
class D(C, A):
    def method(self):
        print('class D')

        # super().method() # вызываем первый родительский класс C

        # если хотим вызвать метод из класса A можем поместить класс с иерархией ниже A в функцию super
        super(B, self).method()

        # получаем список в какой последовательности идёт иерархия классов
        # print(self.__class__.__mro__)
        # результат:
        # <class '__main__.D'>,
        # <class '__main__.C'>,
        # <class '__main__.B'>,
        # <class '__main__.A'>,
# print(D.__mro__) # второй способ

D().method()
