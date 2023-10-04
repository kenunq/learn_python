'''
Объект    - единица информации в памяти
Экземпляр - конкретный объект какого то класса
Класс     - инструкция по созданию объектов определенного типа
Метод     - функция в классе для воздействия на объект
Атрибут   - переменная общая для всех экземпляров класса находящаяся внутри класса но вне методов
'''

class Purse():
    # в self передаётся имя объекта с которым в данный момент будет работать класс
    # метод __init__ срабатывает при создании экземпляра класса (объекта)
    def __init__(self, valuta, userName='Unknown'):
        if valuta not in ('RUB', 'USD', 'EUR'):
            raise ValueError ('Не правильная валюта!')
        # двумя __ можно сделать свойство приватным, то есть его нельзя будет изменить вызвав вне класса
        # это называется инкапсуляция, однако обратиться к объекту всё же можно с помощью данной записи:
        # НАЗВАНИЕ-ЭКЗЕМПЛЯРА-КЛАССА._НАЗВАНИЕ-КЛАССА__НАЗВАНИЕ-ОБЪЕКТА-КОТОРЫЙ-ХОТИМ-ВЫЗВАТЬ
        self.__money = 0.00
        self.valuta = valuta
        self.userName = userName

    def top_up_balance(self, howMoney):
        self.__money = self.__money + howMoney
        return howMoney

    def top_down_balance(self, howMoney):
        if self.__money - howMoney < 0:
            # создаём кастомный эррор со своим сообщением с помощью
            # оператора raise который сработает при нашем условии
            raise ValueError ('Не достаточно средств!')
        self.__money = self.__money - howMoney
        return howMoney

    def info(self):
        return self.__money, self.userName

    def __del__(self): # метод __del__ срабатывает при завершении программы для каждого экземпляра класса
        print(f'Кошелёк {self.valuta} удалён.')

# создаём 3 экземпляра класса (объекта)
rub_purse = Purse('RUB', 'Иван')
usd_purse = Purse('USD')
eur_purse = Purse('EUR', 'Bill')

usd_purse.__money = 10 # т.к. мы сделали свойство приватным его больше нельзя изменить вне класса
usd_purse.userName = 'Karl' # это свойство мы можем изменять вне класса т.к. оно не приватно

del rub_purse # объекты можно удалять командой del в любом месте кода, либо в конце методом __del__

usd_purse.top_up_balance(20) # пополняем баланс
eur_purse.top_up_balance(usd_purse.top_down_balance(7)) # переводим 7 баксов на другой кошелёк
# итого
print('Остаток usd_purse:', usd_purse.info())
print('Остаток eur_purse:', eur_purse.info())
