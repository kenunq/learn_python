# Магические методы

# | Оператор | Метод оператора           |
# | x + y    | __add__(self, other)      |
# | x - y    | __sub__(self, other)      |
# | x * y    | __mul__(self, other)      |
# | x / y    | __truediv__(self, other)  |
# | x // y   | __floordiv__(self, other) |
# | x % y    | __mod__(self, other)      |

# | Оператор | Метод оператора            |
# | x += y   | __iadd__(self, other)      |
# | x -= y   | __isub__(self, other)      |
# | x *= y   | __imul__(self, other)      |
# | x /= y   | __itruediv__(self, other)  |
# | x //= y  | __ifloordiv__(self, other) |
# | x %= y   | __imod__(self, other)      |

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other): # метод когда экземпляр класса при мат. операции находится слева
        # число слева это self, число справа это other
        print('вызов __add__')
        if isinstance(other, BankAccount): # если мы пытаемся сложить 2 экземпляра данного класса то складываем балансы
            print('условие if isinstance(other, BankAccount): выполнено')
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            print('условие if isinstance(other, (int, float)): выполнено')
            return self.balance + other

    def __radd__(self, other): # метод когда экземпляр класса при мат. операции находится справа
        print('вызов __radd__')
        return self + other

ba1 = BankAccount('Ivan', 900)
print(ba1.balance + 300)

print(ba1 + 400) # Если не создаём маг. метод __add__ получаем ошибку TypeError

# при вызове в таком порядке сначало вызывается __radd__ который меняет местами аргументы, затем вызывается __add__
print(600 + ba1) # Если не создаём маг. метод __radd__ получаем ошибку TypeError

ba2 = BankAccount('Mark', 500)
print(ba2 + ba1)
