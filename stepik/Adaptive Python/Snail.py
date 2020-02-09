'''
Snail

Snail creeps up the vertical pole of height H feets. Per day it goes A feets up,
and per night it goes B feets down. In which day the snail will reach the top of
the pole?

Input data format
On the input the program receives non-negative integers H, A, B, where H > B
and A > B. Every integer does not exceed 100.

Sample Input:
10
3
2

Sample Output:
8

'''

# H, up, down = int(input()), int(input()), int(input())
H, up, down = 15, 11, 2
if H <= up: print(1)
else:
    days = (H - up) % (up - down)
    print(days)

    '''
days = (H - down) // (up - down) + 1
m = up * days
while m < H:
    m += up
    days += 1
    if m >= H: break
    m -= down
print(days)
'''