# Пирамида из звездочек
import time
start_time = time.time()

x = int(input())
i = 1

while i <= x:
    print(' '*(x - i) + '**'*i )
    i += 1

print("time elapsed: {:.2f}s".format(time.time() - start_time))