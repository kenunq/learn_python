from learn_OPP import Car

a4 = Car('audi', 'a4', 2016)
# print(a4.company)

bmw = Car('BMW', 'x7', 2015)


a4.read_odometer()
bmw.read_odometer()

a4.increment_odometer(10)

a4.read_odometer()
bmw.read_odometer()

a4.increment_odometer(10)
a4.increment_odometer(10)
a4.increment_odometer(10)
a4.increment_odometer(10)
a4.increment_odometer(10)
bmw.increment_odometer(5)

a4.read_odometer()
bmw.read_odometer()

a4.update_odometer(60)

a4.read_odometer()
bmw.read_odometer()