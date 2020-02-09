'''Напишите программу, которая получает на вход три целых числа, по
одному числу в строке, и выводит на консоль в три строки сначала
максимальное, потом минимальное, после чего оставшееся число.
На ввод могут подаваться и повторяющиеся числа.

'''

'''
a, b, c = [int(input()) for i in range(3)]
n1, n2, n3 = 0, 0, 0,
if a > b:
    if a > c:
        n1 = a
    elif a < c:
        n1 = c
    if b > c:
        n2 = b
        n3 = c
    else:
        n2 = c
        n3 = b

elif b > a:
    if b < c
        n1 = c
    elif b > c
        n1 = b
    if a > c:
        n2 = a
        n3 = c
    else:
        n2 = c
        n3 = a
'''

a, b, c = [int(input()) for i in range(3)]

if a < b:
    a,b = b,a
if a < c:
    a,c = c,a
if b < c:
    b,c = c, b

print(a, c, b, sep='\n')