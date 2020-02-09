''' Задача Марка '''

import math
import random

e = float(input('Задайте погрешность: '))
a = float(input('Задайте начало интервала: '))
b = float(input('Задайте конец интервала: '))

fx0, fx1, fx2 = 0,0,0
x0, x1, x2 = 0,0,0
l = b - a

while e <= l:

    x0 = (a + b) / 2
    x1 = a + l/4
    x2 = b - l/4

    fx0 = math.sin(x0)
    fx1 = math.sin(x1)
    fx2 = math.sin(x2)

    if fx1 < fx0:

        b = x0

    elif fx2 < fx0:

        a = x0

    else: print('Ошибка')

    l = b - a

print(fx0, '- минимальное значение фукции при ', x0)

 


    
