'''
Напишите программу, которая выводит часть последовательности
1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ... (число повторяется столько раз,
чему равно). На вход программе передаётся неотрицательное целое число
n — столько элементов последовательности должна отобразить программа.
На выходе ожидается последовательность чисел, записанных через пробел
в одну строку.
Например, если n = 7, то программа должна вывести 1 2 2 3 3 3 4.

'''

import time

n = int(input())
start_time = time.time()

x = 0
for i in range(1, n+1):
    if x == n: break
    for j in range(i):
        if x == n: break
        print(i, end=' ')
        x += 1
print()
print("time elapsed: {:.10f}s".format(time.time() - start_time))