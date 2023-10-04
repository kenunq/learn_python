from pprint import pprint
from dataclasses import dataclass


class Thing:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price
    
    def __repr__(self):
        print('repr')
        return f'{self.__class__.__name__}({self.__dict__})'
    
    # def __str__(self):
    #     print('str')
    #     return f'{self.__class__.__name__}({self.__dict__})'


@dataclass
class ThingData:
    name: str
    weight: int
    price: float


t = Thing("Учебник по Python", 100, 190.90)
print(t)

# Так же в датаклассах уже реализованы дандер методы __init__, __repr__, __eq__ и т.д.
td1 = ThingData("Учебник по Python", 100, 190.90)
# за счёт __repr__ дата классы отображают атрибуты объекта а не адрес в памяти
print(td1)

td2 = ThingData("Учебник по Python", 100, 190.90)
# за счёт __eq__ дата классы сравниваются по значениям атрибутов
print(f'{td1 == td2 = }') # True

print('\n\n\n')
pprint(ThingData.__dict__)
