import time
start_time = time.time()

n = 10000
'''
for i in range(n):
    for j in range(n):
        print('*', end = '')
    print()

'''

print(str(("*"*n+'\n')*n))

print("time elapsed: {:.2f}s".format(time.time() - start_time))
