# Сражение с тролями
# Попробую добавить рандома в код
#

print("Your lone hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("Your hero unsheathes his sword for the last fight of his life.\n")

import random

health = 10
trolls = 0
damage = 0

while health > 0:
    trolls += random.randrange(2)
    damage = random.randrange(3)
    health -= damage

    print("Your hero swings and defeats an evil troll, " \
          "but takes", damage, "damage points.\n")

print("Your hero fought valiantly and defeated", trolls, "trolls.")
print("But alas, your hero is no more.")

input("\n\nPress the enter key to exit.")
