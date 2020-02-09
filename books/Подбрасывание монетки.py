# Урок 3 задание 2
# Побрасываем монету 100 и сообщаем, сколько раз выпал орел,
# сколько - решка

input('Давай подбросим монету сотню раз?')

import random

attempt = 1
orel = 0
reshka = 0

while attempt <= 100:

    attempt += 1
    x = random.randrange(2)

    if x == 0:
        orel += 1
    else:
        reshka += 1

print('В результате 100 подбрасываний выпало', orel, 'орла и', \
      reshka, 'решки.')

input('Enter')
    


