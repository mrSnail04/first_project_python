#Найти более сладкое мороженное исходя из посыпки и состава
class IceCream:
    def __init__(self, name, flavor, sprinkles):
        self.name = name
        self.flavor = flavor
        self.sprinkles = sprinkles

    def sweetest_icecream(lst):
        flavor_value = {
            'Plain': 0,
            'Vanilla': 5,
            'ChocolateChip': 5,
            'Strawberry': 10,
            'Chocolate': 10
        }
        print(max([icecream.sprinkles + flavor_value[icecream.flavor] for icecream in lst]))
ice1 = IceCream('ice1', 'Chocolate', 13)
ice2 = IceCream('ice2', 'Vanilla', 0)
ice3 = IceCream('ice3', 'Strawberry', 7)
ice4 = IceCream('ice4', 'Plain', 18)
ice5 = IceCream('ice5', 'ChocolateChip', 3)
IceCream.sweetest_icecream([ice1, ice2, ice3, ice4, ice5])
