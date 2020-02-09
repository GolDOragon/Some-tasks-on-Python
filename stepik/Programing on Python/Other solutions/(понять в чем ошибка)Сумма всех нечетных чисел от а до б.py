'''
Вывести сумму всех нечётных чисел от a до b

'''

import time
start_time = time.time()

#a, b = [int(input()) for _ in range(2)]
a = 1
b = 12345678
s = 0
'''
for i in range(a, b+1):
    if i % 2 == 1:
        s += 1
print(s)

'''
if a % 2 == 0:
    for i in range(a+1, b+1, 2):
        s += i
else:
    for i in range(a, b+1, 2):
        s += i
print(s)

print("time elapsed: {:.2f}s".format(time.time() - start_time))