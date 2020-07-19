class Vehicle:
    def __init__(self, position):
        self.position = position

    def travel (self, destination):
        rout= calculate_route(source=self.position, to=destination)
        self.move_along(rout)
    
    def calculate_route(self, source, to):
        return 0
    
    def move_along(self, route):
        print('moving')

class Car(Vehicle):
    pass

class Airplane(Vehicle):
    pass

class RadioMixin:
    def __init__(self):
        self.radio= Radio()
    
    def turn_on(self,station):
        self.radio.set_station(station)
        self.radio.play()
    
class Radio :
    def set_station(self, station):
        self.station = station
    def play(self):
        print(f'Playing {self.station}')

class Car(Vehicle, RadioMixin):
    def __init__(self):
        Vehicle.__init__(self, (10,20))
        RadioMixin.__init__(self)


car=Car()
car.turn_on("FM")










class Person():
    def __init__(self, damage = 0, health = 100):
        self.damage =damage
        self.health = health

    def hit(self, damage):
        print(f"You lost {damage} HP")
        self.health -= damage

class Knight(Person):
    def __init__(self, armor = 0, attack = 10, weapons = None):
        Person.__init__(self)
        self.armor = armor
        self.attack = attack
        self.weapons = weapons
    def take_weapons(self, weapons):
        self.weapons = weapons
        print(f"You take {self.weapons}")   

me =Knight()
print(f"Your armor = {me.armor}")
me.armor=50
print(f"Your armor now = {me.armor}")
print(f"Your attack is {me.attack}")
print(f"Your weapons: {me.weapons}")
me.take_weapons('Knife')
print(f"You have {me.weapons}")
me.hit(52)
print(f"You health now is {me.health} HP")