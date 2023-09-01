# типа данных в питоне

#изменяемые(mutable)
# print(type(   {1,2,"a"}  )) #  -> <class 'set'> множество
# print(type(   {"a":1, 2:"b"}   )) #  -> <class 'dict'> словарь
# print(type(   [1,2,"a"]   )) #  -> <class 'list'> список
#
# from array import array
#
# print(type(  array("l", [1,2,4])  )) #  -> <class 'array.array'> массив
#print(type(bytearray(3))) # -> <class 'bytearray'> массив байт

#неизменяемые (unmutable)
# print(type(   1   )) #  -> <class 'int'> Числа
# print(type(   "abc"   )) #  -> <class 'str'> строки
# print(type(   (1,2,"a")  )) #  -> <class 'tuple'> картеж
# print(type(   None  )) #  -> <class 'NoneType'> Нету данных
# print(type(   False  )) #  -> <class 'bool'> Логическое значение
# print(type(   3.4  )) #  -> <class 'float'> дробное число
# print(type(   2 + 4j  )) #  -> <class 'complex'> комплексное число
# print(type(   frozenset([1,2,"a"])  )) #  -> <class 'frozenset'> Неизменяемое множество
#print(type(   bytes(123)   )) #  -> <class 'bytes'> байты

#print(complex(1+3j)) #создание комплексного числа


#узнать id объекта
# print(id( "str" )) # -> 140735957027056
# print( id( (1,2,"a") ) ) # -> 2850657923840

#узнать адрес в памяти в шестнадцатиричном формате
# print(hex(id("str"))) # -> 0x7fffa4b9c8f0
# print(hex(id(123))) # -> 0x7fffa4cff268

# print("123 = ", bytes(123)) # преобразует объект в неизменяемую строку байтов
# print("Привет Мир! =", bytes('Привет Мир!', encoding='utf-8'))

# перевод int в бинарную строку
# print("123 =", bin(123)) # -> 0b1111011
# print("123 =", bin(123)[2:]) # -> 1111011


#изменяемый обект(id и место в памяти объекта всегда одинаковый)
# x = [1,4,"a"]
# print(id(x), x) # -> 1313106120704 [1, 4, 'a']
# x[1] = 6
# print(id(x), x) # -> 1313106120704 [1, 6, 'a']
# x.append("g")
# print(id(x), x) # -> 1313106120704 [1, 6, 'a', 'g']


#неизменяемый объект(любое действие с объектом меняем его id)
# str = "123"
# print(id(str), str) # -> 2866371710448 123
# str = str[:2] + "6"
# print(id(str), str) # -> 2866371710128 126
# str += "5"
# print(id(str), str) # -> 2866371710320 1265


# Области видимости объектов
#built-in # встроенные функции в интерпретаторе, для их использования не нужно импортировать модули, а так же операторы(зарезервированные слова)
#global #объекты доступные в пространтсве имён модуля
#local # объекты достпуные внутри функции
#nonlocal # объекты доступные из блока внешней функции(обёртки)

# def a():
#     ''' Документация функции a '''
#
# class b:
#     ''' Документация класса b '''
#
#     def my_method_only_my():
#         pass
#
# print("Имя объекта", a.__name__, b.__name__) # позволяет посмотреть имя объекта
# print("Документация объекта", a.__doc__, b.__doc__) # позволяет посмотреть документацию объекта
# print(help(a)) # позволяет посмотреть документацию объекта
# print(globals()) # показывает доступные объекты в пространстве имен модуля
# import math
# print(dir(math)) # позволяет узнать какие объекты содержаться в функции/модуле (без аргументов в текущем пространстве имен модуля)
# print(dir(a))
# print(__name__) # узнать какое состояние имеет переменная __name__ в текущем пространстве имен модуля


# print(callable(len), callable("str")) # проверяем является ли объект вызываемым -> True False

# print(locals()) # возвращает словарь с переменными и их значениями из текущей локальной области видимости в виде словаря(dict)

# проверить, относится ли объект к определенному типу данных

# print(isinstance('str', int)) # -> False
# print(isinstance('str', str)) # -> True
#
# #тоже самое, но с помощью type
#
# print(type('str') == int)
# print(type('str') == str)

#принадлежность объекта к определенному сабклассу можно проверить с помощью функции issubclass

# print(issubclass(int, type(72))) # -> True
# print(issubclass(int, type("Hello, world!"))) # -> False
# print(issubclass(str, type("Hello, world!"))) #-> True

#функция type определяет тип данных

# if type(True) == bool:
#     print("boolean")
# if type(1) == int:
#     print(type(1))

# функция bool преобразует число в True или False
#если число == 0 тогда ложь, если число меньше или больше 0 тогда истина
# print(bool(0))
# print(bool(1))
# print(bool(-1))

# так же и со строками, только вместо 0 принимается пустая строка
# print(bool(""))
# print(bool("123"))

#так же и с коллекциями
# print(bool([]))
# print(bool([1,3]))

#умножение разных типов данных
print(1 * 5) # int -> 5
print("1" * 5) # str -> "11111"
print((1,) * 5) # tuple -> (1, 1, 1, 1, 1)
print([1] * 5) # list -> [1, 1, 1, 1, 1]
print([[]] * 5) # list -> [[], [], [], [], []]
print(["1"] * 5) # list -> ['1', '1', '1', '1', '1']
print(True*5, 1*5)
print(False*5, 0*5)


