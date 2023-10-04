class Cat:

    def __init__(self, name, breed, age, color):
        print(f'hello new object is {self, name, breed, age, color}')
        self.name = name
        self.bred = breed
        self.age = age
        self.color = color

bob = Cat('Bob', 'pers', 2, 'grey')
