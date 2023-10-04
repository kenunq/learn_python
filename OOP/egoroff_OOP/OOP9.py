# Магические методы __str__ и __repr__ служат для того что бы объекты были более наглядны
# например без маг методов print(Экземпляр класса) выдаст: <__main__.Lion object at 0x0000018684AC5130>
# с магическим методом print(Экземпляр класса) выдаст то что вы укажете в return

class Lion:

    def __init__(self, name) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f'The object Lion - {self.name}'

    def __str__(self) -> str:
        return f'Lion - {self.name}'

q = Lion('Bob')
print(q)
