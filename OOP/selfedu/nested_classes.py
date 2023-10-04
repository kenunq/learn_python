class Women:
    def __init__(self):
        # к вложенному классу Meta можно обращатся через экземпляр класса Women
        print('class Women def __init__:', self.Meta.ordering)
    
    title = 'объект класса для поля title'
    photo = 'объект класса для поля photo'
    ordering = 'объект класса для поля ordering'
    
    # за счёт вложенного класса можно определять отдельное пространство имён
    # в котором можно создавать атрибуты с таким же именем как и в классе обёртке
    class Meta: # при создании экземпляра класса Women, экземпляр класса Meta НЕ создаётся.
        ordering = ['id']


print(Women.ordering)
print(Women.Meta.ordering)

w = Women()
print(w.ordering)
print(w.Meta.ordering)
