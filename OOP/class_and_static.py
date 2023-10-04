class User:
    def __init__(self, name, email):
        print('[def __init__] name:', name, 'email:', email)
        self.name = name
        self.email = email

    def get_info(self):
        print(f'[def get_info] {self.name} - {self.email}')

    # если в @staticmethod не передать экземпляр класса то получится обычная функция
    # которая не будет уметь обращатся к элементам класса через self
    @staticmethod
    def get_info_static(self):
        print(f'[def get_info_static] {self.name} - {self.email}')

    # в @classmethod автоматически первым аргументом передаётся не экземпляр класса а сам класс.
    # поэтому метод может работать со всем что находится внутри класса кроме экземпляров вне класса
    @classmethod
    def get_info_class(cls, user_list):
        print('[def get_info_class] cls:', cls)
        name, email = user_list
        return cls(name, email)

# классическая передача аргументов в класс
# user = User('Admin0', 'test0@test.com')
# user.get_info()

# передача экземпляра класса в @staticmethod
# user2 = User('Admin1', 'test1@test.com')
# user2.get_info_static(user2)

# передача списка в качестве аргумента в @classmethod
user_list = ['Admin2', 'test2@test.com']
user3 = User.get_info_class(user_list)
user3.get_info()
