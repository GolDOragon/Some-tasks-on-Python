
class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        #self.is_alive = True

    @property
    def is_alive(self) -> bool:
        return self.health > 0



class Knight(Warrior):
    def __init__(self):
        super().__init__()
        self.attack = 7


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack
        if unit_2.health > 0:
            unit_1.health -= unit_2.attack
    return unit_1.is_alive

'''
    warrior = unit_1, unit_2
    i = 0
    while unit_1.is_alive and unit_2.is_alive:
        warrior[-i + 1].health -= warrior[i].attack
        if warrior[-i + 1].health < 1:
            warrior[-i + 1].is_alive = False
        i = (i + 1) % 2
    if warrior[0].is_alive:
        return True
    elif warrior[1].is_alive:
        return False

'''
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    print('All right!')
    input()