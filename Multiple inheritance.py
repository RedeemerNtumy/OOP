'''
A game with Wizards and archers
'''


class User():
    def sign_in(self):
        return 'Logged in'


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        return f'Attacking with a power of {self.power}'


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        return f'Number of arrows left : {self.num_arrows}'


wizard1 = Wizard("James", 100)
print(wizard1.attack())
print(wizard1.name)
print(wizard1.sign_in())
'''
We want to have a user that possesses both powers
'''


class Hybrid(Wizard, Archer):
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)


Hb1 = Hybrid("John", 80, 100)
print(Hb1.attack())
print(Hb1.check_arrows())
