# Пространство имён класса

PYTHON_DEV = 6
GO_DEV = 6
REACT_DEV = 4

class DepartamentIT:
    PYTHON_DEV = 3
    GO_DEV = 3
    REACT_DEV = 2

    def info(self):
        # по дефолту имена переменных ищатся в глобальном пространстве
        # если указать self либо название класса, то поиск будет идти внутри класса
        print('local with self', self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)
        print('local with name', DepartamentIT.PYTHON_DEV, DepartamentIT.GO_DEV, DepartamentIT.REACT_DEV)
        # print('global var', PYTHON_DEV, GO_DEV, REACT_DEV)

    @property
    def info_with_prop(self):
        print('local with self', self.PYTHON_DEV, self.GO_DEV, self.REACT_DEV)
        print('local with name', DepartamentIT.PYTHON_DEV, DepartamentIT.GO_DEV, DepartamentIT.REACT_DEV)
        print('global var', PYTHON_DEV, GO_DEV, REACT_DEV)

    @classmethod
    def info_class(cls):
        print('local with cls', cls.PYTHON_DEV, cls.GO_DEV, cls.REACT_DEV)

    @staticmethod
    def info_static():
        print('local with static', DepartamentIT.PYTHON_DEV, DepartamentIT.GO_DEV, DepartamentIT.REACT_DEV)

    def hiring_py_dev_self(self):
        self.PYTHON_DEV += 2 # создаст локалькую переменную внутри экземпляра класса со значением 5

    def hiring_py_dev_name(self):
        DepartamentIT.PYTHON_DEV += 2 # изменит переменную внутри класса и соответственно для всех его экземпляров

    def make_backend(self):
        print('Python and Go')

    def make_frontend(self):
        print('React')

it1 = DepartamentIT()
it1.info()
print()
it1.info_with_prop
print()
it1.info_class()
print()
it1.info_static()
print()
it1.hiring_py_dev_self()
it1.info()
print()
it1.hiring_py_dev_name()
it1.info()
