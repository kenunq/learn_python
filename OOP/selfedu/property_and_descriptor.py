class Point3DWithProperty:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")
    
    # Если необходимо реализовывать много геттеров/сеттеров/делитеров
    # возможно стоит реализовать один класс дескриптор
    # для замены огромного количества проперти которые будут загромождать код
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, coord):
        self.verify_coord(coord)
        self._x = coord
    
    
    @property
    def y(self):
        return self._y
    
    @x.setter
    def y(self, coord):
        self.verify_coord(coord)
        self._y = coord
    
    
    @property
    def z(self):
        return self._z
    
    @x.setter
    def z(self, coord):
        self.verify_coord(coord)
        self._z = coord


# Дескриптор данных, служит для получения/установки/удаления данных как замена property
class IntDescriptor:
    # self - Ссылка на экземпляр класса, то есть IntDescriptor()
    # owner - Ссылка на класс Point3DWithDescriptor
    # name - имя атрибута, то есть "x", "y", "z"
    def __set_name__(self, owner, name):
        """Вызывается при создании экземпляра класса IntDescriptor"""
        self.name = '_' + name
    
    # self - Ссылка на экземпляр класса, то есть IntDescriptor()
    # instance - Ссылка на экземпляр класса Point3DWithDescriptor
    # owner - Ссылка на класс Point3DWithDescriptor
    def __get__(self, instance, owner):
        """Вызывается в момент чтения значения"""
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)
    
    # self - Ссылка на экземпляр класса, то есть IntDescriptor()
    # instance - Ссылка на экземпляр класса Point3DWithDescriptor
    # value - Значение для присвоения
    def __set__(self, instance, value):
        """Вызывается в момент присваивания значения"""
        self.verify_coord(value)
        print(f'IntDescriptor __set__: {self.name} = {value}')
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)

    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError("Координата должна быть целым числом")


class Point3DWithDescriptor:
    # при создании экземпляров дескриптора в нём появляются атрибуты "_x", "_y", "_z"
    x = IntDescriptor()
    y = IntDescriptor()
    z = IntDescriptor()
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p1 = Point3DWithProperty(1, 2, 3)
print('Point3DWithProperty __dict__:', p1.__dict__) # {'_x': 1, '_y': 2, '_z': 3}

p2 = Point3DWithDescriptor(1, 2, 3)
print('Point3DWithDescriptor __dict__:', p2.__dict__) # {'_x': 1, '_y': 2, '_z': 3}
