# Множественное наследование

class Goods:
    def __init__(self, name, weight, height):
        super().__init__() # для того чтобы отработал инициализатор в классе MixinLog
        
        print('class Goods def __init__')
        self.name = name
        self.weight = weight
        self.height = height
    
    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.height}')


class MixinLog:
    def __init__(self):
        super().__init__() # для того чтобы отработал инициализатор в классе MixinLog2
        
        print("class MixinLog def __init__")
        self.id = 152973
    
    def save_sell_log(self):
        print(f'{self.id}: товар был продан в 00:00 часов')


class MixinLog2:
    def __init__(self):
        print("class MixinLog2 def __init__")
        self.id = 982587
    
    def save_sell_log2(self):
        print(f'{self.id}: товар был продан в 13:00 часов')


class NoteBook(Goods, MixinLog, MixinLog2):
    pass


n = NoteBook('acer', 1.5, 30000)
n.print_info()
n.save_sell_log()
n.save_sell_log2()

# т.к. класс Goods указан первым в списке наследования MRO,
# все переданные аргументы при создании экземпляра класса NoteBook
# попадут в метод __init__ класса Goods, и за счёт того что мы указали super().__init__()
# сначала вызовется метод __init__ у класса MixinLog, который является следующим по списку в MRO
# и т.к. в этом методе так же указан super().__init__() будет вызван метод __init__ у класса MixinLog2
# и как будет выполнен __init__ в MixinLog2, интерпритатор вернётся к __init__ в MixinLog выполнит его,
# и только потом вернётся к __init__ в Goods и так же выполнит его

# [<class '__main__.NoteBook'>, <class '__main__.Goods'>, <class '__main__.MixinLog'>, <class 'object'>]

# print(NoteBook.__mro__) # MRO - Method Resolution Order
print(NoteBook.mro())
