# Напишите программу, которая получает на вход три целых числа,
# по одному числу в строке, и выводит на консоль в три строки сначала
# максимальное, потом минимальное, после чего оставшееся число.
# На ввод могут подаваться и повторяющиеся числа.

a, b, c = [int(input()) for i in range(3)]

if a >= b and a >= c:
    print(a)
    if b >= c:
        print(c)
        print(b)
    else:
        print(b)
        print(c)

elif b >= a and b >= c:
    print(b)
    if a >= c:
        print(c)
        print(a)
    else:
        print(a)
        print(c)
        
elif c >= b and c >= a:
    print(c)
    if a >= b:
        print(b)
        print(a)
    else:
        print(a)
        print(b)
