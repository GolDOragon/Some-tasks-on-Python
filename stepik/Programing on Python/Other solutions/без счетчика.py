import time
start_time = time.time()

number = 10000
star = '*'
while len(star) < number:
    print(star)
    star +="*"

print("time elapsed: {:.2f}s".format(time.time() - start_time))

