# Tasks 1 and 2

class Country:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def add(self, boo):

        return Country(self.name + " " + boo.name,
                       self.population + boo.population)

    def __add__(self, boo):

        return Country(self.name + " " + boo.name,
                       self.population + boo.population)


bosnia = Country('Bosnia', 10_000_000)
herzegovina = Country('Herzegovina', 5_000_000)

bosnia_herzegovina = bosnia.add(herzegovina)
print(bosnia_herzegovina.population)  # -> 15_000_000
print(bosnia_herzegovina.name)  # -> 'Bosnia Herzegovina'

bosnia_herzegovina_add = bosnia + herzegovina
print(bosnia_herzegovina_add.population)  # -> 15_000_000
print(bosnia_herzegovina_add.name)  # -> 'Bosnia Herzegovina'


# Task 3

class Car:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5
        return self.speed

    def brake(self):
        self.speed -= 5
        if self.speed < 0:
            return 0
        else:
            return self.speed

    def display_speed(self):
        print(f'Current speed is {self.speed} km/h')


chevrolet_aveo = Car('chevrolet', 'aveo', 2008, 110)

chevrolet_aveo.accelerate()
chevrolet_aveo.accelerate()
chevrolet_aveo.accelerate()
chevrolet_aveo.brake()
chevrolet_aveo.display_speed()
