from abc import ABC, abstractmethod, ABCMeta


# у абстрактоного класса нельзя создать экземпляр класса
class MyAbstractClass(ABC):
    @abstractmethod
    def some():
        print('MyAbstractClass -> def some')

try:
    my_abstract_class = MyAbstractClass()
except Exception as exc: # Не удается создать экземпляр абстрактного класса MyAbstractClass с помощью абстрактных методов.
    print(exc)


# дочерний класс не перестанет быть абстрактным пока в нём не определится абстрактный метод
class Cat(MyAbstractClass):
    pass

try:
    cat = Cat()
except Exception as exc: # Не удается создать экземпляр абстрактного класса Cat с помощью абстрактных методов.
    print(exc)


class Dog(MyAbstractClass):
    def some(self):
        print('Dog -> def some')

dog = Dog()
dog.some()



# если необходимо реализовать абстрактный мета класс используем ABCMeta
class OneMeta(ABCMeta):
    def __new__(cls, name, bases, dict):
        pass

    def __init__(self, name, bases, dict):
        pass

    def __prepare__(name, bases, **kwds):
        pass

    def __call__(cls, *args, **kwargs):
        pass

# https://pythonist.ru/metaklassy-v-python/
# если необходимо реализовать обычный мета класс используем type
class Two(type):
    def __new__(cls, name, bases, dict):
        pass

    def __init__(self, name, bases, dict):
        pass

    # def __prepare__(name, bases, **kwds):
    #     pass

    def __call__(cls, *args, **kwargs):
        pass


class MyClass(metaclass=Two):
    pass
