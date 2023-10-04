# Инкапсуляция
# Публичные, Приватные, Защищённые атрибуты и методы

# Публичные - без нижних подчёркиваний в начале
# Защищённые - с одним подчёркиванием в начале (говорит о том что атрибут не стоит использовать вне класса)
# Приватные - с двумя подчёркиваниями в начале (запрещает использовать вне класса, ошибка - AttributeError)

class BankAccount:
    def __init__(self, name, balance, passport) -> None:
        self._name = name
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_data(self):
        print(self.__name, self.__balance, self.__passport)

account1 = BankAccount('Bob', 100_000, 45484564654)
account1.print_data()
# print(account1.__name, account1.__balance, account1.__passport)

# НАЗВАНИЕ-ЭКЗЕМПЛЯРА-КЛАССА._НАЗВАНИЕ-КЛАССА__НАЗВАНИЕ-ОБЪЕКТА-КОТОРЫЙ-ХОТИМ-ВЫЗВАТЬ
print('обращение к приватному объекту:', account1._BankAccount__balance)
