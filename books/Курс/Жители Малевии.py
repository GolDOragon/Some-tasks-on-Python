# Жители страны Малевии часто экспериментируют с планировкой комнат.
# Комнаты бывают треугольные, прямоугольные и круглые.
# Чтобы быстро вычислять жилплощадь, требуется написать программу,
# на вход которой подаётся тип фигуры комнаты и соответствующие параметры,
# которая бы выводила площадь получившейся комнаты. Для числа π в стране
# Малевии используют значение 3.14.


figure = input()

if figure == 'треугольник':

    a, b, c = [int(input()) for i in range(3)]
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c))**0.5

elif figure == 'прямоугольник':

    a, b = int(input()), int(input())
    S = a*b

elif figure == 'круг':
    r = int(input())
    S = 3.14 * r ** 2

print(S)

    
