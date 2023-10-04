# https://www.youtube.com/watch?v=H323khQJL40

# Декораторы

# @property # геттер
# @method.setter # сеттер
# @classmethod
# @staticmethod

# модуль datetime возвращает текущее время
from datetime import datetime

# создаём экземпляры игроков
class Player():

    # дефолтные свойства класса
    __LVL, __HEALTH = 1, 100 # 1 или 2 нижних подчёркивания называется инкапсуляцией
    # даже к инкапсулированному свойству/атрибуту/методу можно обратиться с помощью
    # данной записи: НАЗВАНИЕ-ЭКЗЕМПЛЯРА-КЛАССА._НАЗВАНИЕ-КЛАССА__НАЗВАНИЕ-ОБЪЕКТА-КОТОРЫЙ-ХОТИМ-ВЫЗВАТЬ

    # добавить к экземпляру класса свойства кроме тех которые перечислены
    # в атрибуте __slots__ нельзя, будет срабатывать исключение
    __slots__ = ['__lvl', '__health', '__born']

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = datetime.now()

    # property без setter может существовать, наоборот нет
    @property
    def lvl(self):
        return self.__lvl, f'{datetime.now() - self.__born}'

    @lvl.setter
    def lvl(self, numeric):
        self.__lvl += Player.__typeTest(numeric)
        if self.__lvl >= 100:
            self.__lvl = 100

    # classmethod нужен для того что бы взаимодействовать
    # не с экземплярами класса а с целым классом
    # в параметр cls будет попадать не
    # имя экземпляра а имя самого класса
    @classmethod
    def set_cls_field(cls, lvl=1, health=100):
        # в данном случае мы будем вызывать этот метод и
        # передавать в него аргументы lvl, health которые
        # в свою очередь будут изменять константы класса
        cls.__LVL = Player.__typeTest(lvl)
        cls.__HEALTH = Player.__typeTest(health)

    # метод проверки типа полученных данных
    # staticmethod служит лиж для того что бы программист понимал
    # что этот метод не будет изменяться, он статический
    @staticmethod
    def __typeTest(value):
        # если значение является классом int возвращаем значение
        if isinstance(value, int):
            return value
        # иначе создаём ошибку
        else:
            raise TypeError ('Must be int')

# unit = Player()

# print(unit.lvl)
# unit.lvl = 6
# print(unit.lvl)
