from dataclasses import dataclass, field, InitVar


# декоратор может принимать параметры:
# frozen=False(default)/True # делает атрибуты класса неизменяемыми (read only, только для чтения)
@dataclass
class ThingData2:
    # если необходимо наоборт исключить из __repr__ атрибут, тогда указываем repr=False в функции field
    # если необходимо исключить атрибут при сравнии с помощью __eq__, тогда указываем compare=False в функции field
    made_in: str = field(repr=False, compare=False)

    # если необходимо указать дефолтное значение при использовании функции field, тогда указываем default=<значение>
    company: str = field(default='Tech Industries')

    # по умолчанию изменяемые типы данных нельзя указывать в датаклассе
    # для этого необходимо использовать специальную функцию field (если необходимо получить пустой список)
    # либо указывать их в дандер методе __post_init__ (если необходимо получить заполненный список)
    tech_params: list = field(default_factory=list)

    # tech_params2 указан в атрибутах только для того чтобы __repr__ отображал этот атрибут при принте
    tech_params2: list = field(init=False) # не передавать атрибут tech_params2 в __init__ класса ThingData2

    # атрибуты дата класса могут принимать значения по умолчанию
    name: str = "NoteBook"
    weight: int = 280
    price: float = 3749.99

    # при аннотировании с помощью класса InitVar, атрибут автоматически попадает в метод __post_init__
    in_store: InitVar[bool] = True

    # срабатывает после обычного __init__
    def __post_init__(self, *args, **kwargs):
        print('def __post_init__:', args, kwargs)
        self.tech_params2 = [1, 2]


td3 = ThingData2(made_in='China', name='MacBook', price=22499.90)
print(td3)

td4 = ThingData2(made_in='China', name='Lenovo', price=8999.99)
print(td4)
