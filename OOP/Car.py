class Car():
    '''Класс по созданию автомобиля'''

    def __init__(self, company, model, year):
        '''Здесь происходит инициализация атрибутов автомобиля'''
        # print('self:', self, model)
        self.company = company
        self.model = model
        self.year = year
        self.odometer_reading = 0 # атрибут по умолчанию равен 0
        # print('Экземпляр автомобиля создан')

    def description_name(self):
        '''Возвращаем описание автомобиля'''
        desc =  str(self.year) + ' ' + self.company + ' ' + self.model
        return desc.title()

    def read_odometer(self):
        '''Выводим пробег автомобиля'''
        print(f'Пробег этого {self.model} авто составляет: ' + str(self.odometer_reading) + 'км')

    def update_odometer(self, km):
        '''Устанавливаем значение на одометре'''
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print('Не стоит скручивать пробег!')

    def increment_odometer(self, km):
        '''Увеличиваем показания одометра на заданную величину'''
        if km >= 0:
            self.odometer_reading += km
