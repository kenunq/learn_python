class Goat:
    # дефолтное значение для всех экземпляров класса
    legs_num = 4
    # конструктор экземпляра класса
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    # встроенный метод преобразования к строке
    def __str__(self):
        s = 'height = {}, weight = {}'.format(self.height, self.weight)
        return s

marusya = Goat(60, 40)
notka = Goat(65, 42)

for x in marusya, notka:
    print(x)

notka.weight += 1
x = notka
x.weight += 5
print(x, notka)

notka.legs_num += 1
print(notka.legs_num, marusya.legs_num)
