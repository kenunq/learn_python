import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)
    
    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError("pick from empty BingoCage")
    
    # определение дандер метода __call__ в классе позволяет делать экземпляр класса вызываемым объектом
    def __call__(self):
        print('class BingoCage def __call__')
        return self.pick()


bc = BingoCage(range(10))
print(bc())
print(bc())
print(bc())
