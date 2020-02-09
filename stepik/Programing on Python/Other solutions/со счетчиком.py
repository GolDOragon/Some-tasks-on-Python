import time
start_time = time.time()

number = 10000
cntr = 0
star = ''
while cntr <= number:
    print(star)
    star +="*"
    cntr += 1


print("time elapsed: {:.2f}s".format(time.time() - start_time))