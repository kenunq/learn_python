# Дата классы позволяют определять типизированные атрибуты в которые будут помещены данные
# ниже приведён пример использования дата класса, функция возвращает дата класс
# и появляется возможность обращаться к его атрибутам через точку, при этом IDE посвечивает тип объекта,
# вместо возврата простого словаря и обращения по ключам в которых содержится неизвестный тип данных.
from dataclasses import dataclass


@dataclass
class A:
    x: str
    y: int
    z: dict

class B:
    x = 'myattr'
    y = 17
    z = {'Hello': 'World!'}

    def with_dataclass(self) -> A:
        return A(
            x=self.x,
            y=self.y,
            z=self.z,
        )

    def without_dataclass(self) -> dict:
        return dict(
            x=self.x,
            y=self.y,
            z=self.z,
        )

b = B()

b1 = b.with_dataclass()
print(b1.x, b1.y, b1.z)

b2 = b.without_dataclass()
print(b2['x'], b2['y'], b2.get('z'))
