class Test:
    def __init__(self, value):
        self.value = value

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Test)):
            raise TypeError("Операнд справа должен иметь тип int или Test")
        return other if isinstance(other, int) else other.value

    def __eq__(self, other):
        """Обрабатывает оператор == и ( != если не переопределён дандер метод __ne__ )"""
        right_operand_value = self.__verify_data(other)
        # при вызове != интерпритатор подставит not к результату сравнения ( если не переопределён дандер метод __ne__ )
        return self.value == right_operand_value

    def __lt__(self, other):
        """Обрабатывает оператор < и ( > если не переопределён дандер метод __gt__ )"""
        right_operand_value = self.__verify_data(other)
        # при вызове > интерпритатор подставит not к результату сравнения ( если не переопределён дандер метод __gt__ )
        return self.value < right_operand_value

    def __le__(self, other):
        """Обрабатывает оператор <= и ( => если не переопределён дандер метод __ge__ )"""
        right_operand_value = self.__verify_data(other)
        # при вызове => интерпритатор подставит not к результату сравнения ( если не переопределён дандер метод __ge__ )
        return self.value <= right_operand_value


t1 = Test(20)
t2 = Test(20)
# по умолчанию при сравнении экземпляров класса, сравниваются id объектов
# но если переопределить дандер метод __eq__ можно указать свою логику сравнения
print(t1 == t2)
print(t1 != t2)
print(t1 < t2)
print(t1 > t2)
print(t1 <= t2)
print(t1 >= t2)
