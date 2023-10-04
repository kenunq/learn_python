class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property # превращаем метод в свойство, по дефолту getter
    def my_balance(self):
        print('getter')
        return self.__balance

    # методы getter, setter, deleter называются одним именем
    @my_balance.setter
    def my_balance(self, value):
        print('setter')
        if not isinstance(value, (int, float)):
            raise ValueError('Баланс должен быть числом')
        self.__balance = value

    @my_balance.deleter
    def my_balance(self):
        print('deleter')
        del self.__balance

ba1 = BankAccount('Ivan', 200)
print(ba1.my_balance)
ba1.my_balance = 400
print(ba1.my_balance)
del ba1.my_balance
