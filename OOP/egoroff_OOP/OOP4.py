# Моносостояние для всех экземпляров
class Cat:
    __shared_attr = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        # присвоив словарь с дефолтными атрибутами в self.__dict__ применяем атрибуты в словаре ко всем экземплярам класса
        # и даже при изменении атрибута он изменится у всех экземпляров
        self.__dict__ = Cat.__shared_attr

d = Cat()
g = Cat()

# d.breed = 'siam'

print(d.breed, d.color)
print(g.breed, d.color)
