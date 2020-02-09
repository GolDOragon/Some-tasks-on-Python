'''
Вычисление суммы чисел от а до b
Использование цикла вместо (?) арифметической прогрессии увеличивает
время выполнения программы в 3 раза!
'''

import time
start_time = time.time()
'''
a = 10
b = 12345678
sum = 0
while a <= b:
    sum += a
    a += 1
print(sum)

'''
print(sum(list(range(10,12345679))))

print("time elapsed: {:.2f}s".format(time.time() - start_time))

