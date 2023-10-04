class Hero:
    ''' Class to create Hero for our game '''
    def __init__(self, name, level, race):
        ''' initialization our Hero '''
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        ''' print all parameters of this Hero '''
        discription = self.name, 'Level is:', self.level, 'Race is:', self.race, 'Health is:', self.health
        print(discription)

    def level_up(self):
        ''' Upgrade level of Hero '''
        self.level += 1

    def move(self):
        ''' Start moving hero '''
        print('Hero ' + self.name + ' start moving...')

    def set_health(self, new_health):
        self.health = new_health


class SuperHero(Hero):
    ''' Class to create SuperHero '''
    def __init__(self, name, level, race, magiclevel=100):
        ''' initialization our SuperHero '''
        # с помощью super() в данном случае означает Hero т.к. мы от него наследуемся
        # и __init__ инициализируем атрибуты родительского класса Hero
        super().__init__(name, level, race)
        self.magiclevel = magiclevel

    def make_magic(self):
        ''' Use magic '''
        self.magiclevel -= 10

    # переопределение родительского метода
    def show_hero(self):
        ''' print all parameters of this SuperHero '''
        discription = self.name, 'Level is:', self.level, 'Race is:', self.race, 'Health is:', self.health, 'Magic is:', self.magiclevel
        print(discription)


my_hero = Hero('Vurdalak', 7, 'Orc')
my_hero.health = 43
my_hero.show_hero()

my_super_hero = SuperHero('Moisey', 10, 'Human', 14)
my_super_hero.health = 62
my_super_hero.show_hero()

my_super_hero.make_magic()
my_super_hero.show_hero()
