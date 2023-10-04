class DefenedVector:
    def __init__(self, value):
        self.__value = value
    
    def __enter__(self):
        print('class DefenedVector def __enter__')
        # при открытии менеджера контекста делаем поверхностную копию переданого объекта
        # и присваиваем её в свойство экземпляра класса __temporary,
        # возвращаем __temporary он попадёт в алиас as defened.
        # Тем самым мы защищаем изначальный объект т.к. будем работать внутри менеджера контекста с его копией.
        self.__temporary = self.__value[:]
        return self.__temporary
    
    def __exit__(self, exc_type, exc_value, trace):
        print('class DefenedVector def __exit__:', exc_type, exc_value)
        # при выходе из менеджера контекста проверяем, если небыло никаких исключений то
        # поэлементно копируем обратно в изначальный объект __value изменённый __temporary
        # за счёт оператора [:]
        if exc_type is None:
            self.__value[:] = self.__temporary
        return False


v1 = [1, 2, 3]
v2 = [2, 3]

try:
    # за счёт кастомного менеджера контекста при возникновении исключения список v1 не был изменён частично
    with DefenedVector(v1) as defened:
        for i in range(len(defened)):
            defened[i] += v2[i]
except IndexError as exc:
    print(exc)

print('v1:', v1)

try:
    # при возникновении исключения список v1 был изменён частично
    for i in range(len(v1)):
        v1[i] += v2[i]
except IndexError as exc:
    print(exc)

print('v1:', v1)
