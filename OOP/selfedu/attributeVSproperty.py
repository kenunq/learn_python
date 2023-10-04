class Test:
    my_attribute = 2 # атрибут класса является общим для всех его экземпляров
    
    def __init__(self):
        print('class Test def __init__')
        self.my_property = 4 # свойство экземпляра является индивидуальным для каждого экземпляра

    def meth(self):
        # для доступа к атрибутам класса внутри метода можно использовать как ссылку на класс так и на его экземпляр
        print('Test.my_attribute:', Test.my_attribute)
        print('self.my_attribute:', self.my_attribute)

    def set_bound(self, val):
        print('значение атрибута класса my_attribute:', getattr(Test, 'my_attribute'),
              '\nсловарь свойств экземпляра класса:', self.__dict__)
        # при присваивании значения атрибуту класса через экземпляр класса self,
        # оператор присваивания создаёт свойство с таким же именем для экземпляра класса
        # self.my_attribute = val
        # если использовать ссылку на класс то значение присвоится атрибуту класса
        # и никакого свойства экземпляра создано не будет
        # Test.my_attribute = val
        print('значение атрибута класса my_attribute:', getattr(Test, 'my_attribute'),
              '\nсловарь свойств экземпляра класса:', self.__dict__)


print(Test.my_attribute) # к атрибуту класса можно получить доступ без создания экземпляра
print(Test().my_attribute) # к атрибуту класса можно получить доступ через экземпляр класса

print()
try:
    Test.my_property # к свойству экземпляра класса нельзя получить доступ без создания экземпляра
except AttributeError as exc:
    print(exc)
    print(Test().my_property) # к свойству экземпляра класса можно получить доступ через экземпляр класса

print()
Test().meth()

print()
Test().set_bound(6)
