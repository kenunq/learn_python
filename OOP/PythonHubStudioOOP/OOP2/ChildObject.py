# Наследование классов

from ParentObject import Verification

class V2(Verification):

    # переопределяем метод __init__ и добавляем параметр age
    def __init__(self, login, password, age):

        # Verification.__init__(self, login, password)
        # аналогичная запись, self передаётся в super автоматически
        super().__init__(login, password)

        self.save()
        self.age = age

    # переопределяем метод save
    # сначало пайтон смотрит есть ли метод save в классе V2
    # если не находит то идёт искать в родительский класс Verification
    def save(self): # дополняем функционал для метода save
        with open('users.txt', 'r') as file:
            for user in file:
                if f'{self.login, self.password}' + '\n' == user:
                    raise ValueError ('Такой пользователь уже существует.')
        # после выполнения нового метода вызываем выполнение старого метода
        # Verification.save(self)
        # аналогичная запись, self передаётся в super автоматически
        super().save()

    def show(self):
        return self.login, self.password, self.age

user = V2('Kenny3', '123456789', 27)
print(user.show())
