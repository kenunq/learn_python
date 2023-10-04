from ParentObject import Player

# передаём уровень игрока
Player.set_cls_field(7)
unit1 = Player()
print(unit1.lvl)

# по умолчанию 1 lvl поэтому
# можно ничего не передавать
Player.set_cls_field()
unit2 = Player()
print(unit2.lvl)
unit2.lvl = 3
# если задать значение класса float
# сработает исключение
# unit2.lvl = 2.4
print(unit2.lvl)
