'''
Напишите программу по следующему описанию. Есть класс "Воин". От него создаются
два экземпляра-юнита. Каждому устанавливается здоровье в 100 очков. В случайном
порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет. У того, кого
бьют, оно уменьшается на 20 очков от одного удара. После каждого удара надо
выводить сообщение, какой юнит атаковал, и сколько у противника осталось
здоровья. Как только у кого-то заканчивается ресурс здоровья, программа завершается
сообщением о том, кто одержал победу.

'''
import random


class warrior:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = int(hp)
        self.dmg = int(damage)

    def attack(self, enemy):
        dmg = random.randint(0, self.dmg)
        enemy.hp -= dmg
        if enemy.hp < 0: # # You can't have negative HP
            enemy.hp = 0
        print(f'{self.name} attacks {enemy.name} and damage {dmg} HP! {enemy.name} have {enemy.hp} HP!')


def battle(war1, war2):
    while war1.hp > 0 and war2.hp > 0:
        r = random.random()
        if r >= 0.5:
            war1.attack(war2)
        else:
            war2.attack(war1)

    if war1.hp == 0:
        winner = war2
        loser = war1
    else:
        winner = war1
        loser = war2

    print(f'Oh, no! {loser.name} falls, {winner.name} wins with {winner.hp} HP!')


warrior1 = warrior('Hero', 100, 20)
warrior2 = warrior('Orc', 100, 20)

battle(warrior1, warrior2)
