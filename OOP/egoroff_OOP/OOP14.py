# Магические методы __getitem__, __setitem__, __delitem__

class Vector:

    def __init__(self, *args) -> None:
        self.values = list(args)

    def __repr__(self) -> str:
        return str(self.values)

    def __getitem__(self, index):
        print('get index:', index)
        if index < len(self.values):
            return self.values[index]
        else:
            raise IndexError('Индекс вышел за границы коллекции')

    def __setitem__(self, index, value):
        print('set index:', index)
        if index < len(self.values):
            self.values[index] = value

        elif index > len(self.values):
            # при выходе за границы индексации заполнить промежуток значениями
            diff = index - (len(self.values) - 1)
            self.values.extend(['Заполнитель'] * diff)

            self.values[index] = value
        else:
            raise IndexError('Индекс вышел за границы коллекции')

    def __delitem__(self, index):
        print('del index:', index)
        if index < len(self.values):
            del self.values[index]
        else:
            raise IndexError('Индекс вышел за границы коллекции')

v1 = Vector(1, 2, 434, 32)
print(v1.values)

v2 = Vector(3, 43, 5, 56, 45, 3423)
print(v2.values)

print(v1[3], v2[-1]) # с помощью магических методов можно сделать доступным обращение по индексу к классу

v1[1] = 300
print(v1.values)

del v2[0]
print(v2.values)

v1[8] = 450
print(v1.values)
