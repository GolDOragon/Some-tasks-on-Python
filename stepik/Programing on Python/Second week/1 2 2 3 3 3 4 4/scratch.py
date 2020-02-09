import time

n = int(input())
start_time = time.time()

a = []
i = 0
while len(a) < n:
    a += [i] * i
    i += 1
print(*a[:n])

print()
print("time elapsed: {:.10f}s".format(time.time() - start_time))
