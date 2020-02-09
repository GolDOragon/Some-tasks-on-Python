'''
Жители страны Малевии часто экспериментируют с планировкой комнат.
Комнаты бывают треугольные, прямоугольные и круглые. Чтобы быстро
вычислять жилплощадь, требуется написать программу, на вход которой
подаётся тип фигуры комнаты и соответствующие параметры, которая бы
выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14.

'''

# Square of tringle
def tringle(a, b, c):
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return S
# Square of rectangle
def rectangle(a, b):
    S = a * b
    return S
# Square of circle
def circle(r):
    S = 3.14 * r*r
    return S

figure = input()

if figure == 'треугольник':
    x, y, z = [int(input()) for i in range(3)]
    print(tringle(x, y, z))

elif figure == 'прямоугольник':
    x, y = [int(input()) for i in range(2)]
    print(rectangle(x, y))

elif figure == 'круг':
    x = int(input())
    print(circle(x))

else:
    print('Figure not found')