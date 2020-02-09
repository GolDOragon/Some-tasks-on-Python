# Taken from mission The Warriors

class Army():
    def __init__(self):
        self.units= []

    def add_units(self, unit_type, unit_amount):
        self.units.append((unit_type, unit_amount))


class Battle:
    '''
    получить 2 армии
    пока в армиях есть люди
        для ближайших бойцов устроить поединок
        забыть проигравшего
        запомнить после боевые характеристики победившего бойца

    '''
    def fight(self, first_army, second_army):
        unit_type_1, unit_amount_1 = first_army.units[0][0], first_army.units[0][1]
        unit_type_2, unit_amount_2 = second_army.units[0][0], second_army.units[0][1]

        unit1, unit2 = unit_type_1(), unit_type_2()
        while unit_amount_1 >=0 and unit_amount_2 >= 0:
            if fight(unit1, unit2):
                unit_amount_2 -= 1
                unit2 = unit_type_2()
            else:
                unit_amount_1 -= 1
                unit1 = unit_type_1()
        if unit_amount_1 >= 0:
            return True
        else:
            return False

class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5
        # self.is_alive = True

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

    print("Coding complete? Let's try tests!")
'''
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
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

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
