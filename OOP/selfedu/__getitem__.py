class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)
    
    # определение дандер методов __getitem__, __setitem__, __delitem__
    # позволяет обращатся к экземпляру класса как к последовательности по индексу с помощью квадратных скобок
    def __getitem__(self, item):
        if 0 <= item < len(self.marks):
            return self.marks[item]
        raise IndexError("Неверный индекс")
    
    def __setitem__(self, item, value):
        if not isinstance(value, int) or item < 0:
            raise TypeError("Индекс должен быть целым положительным числом")
        if item >= len(self.marks):
            offset = item + 1 - len(self.marks)
            self.marks += [None] * offset
        self.marks[item] = value
    
    def __delitem__(self, item):
        if not isinstance(item, int):
            raise TypeError("Индекс должен быть целым положительным числом")
        del self.marks[item]


s1 = Student("Сергей", [5, 5, 3, 2, 5])
del s1[2]
print(s1.marks)
s1[8] = 55
print(s1.marks)
