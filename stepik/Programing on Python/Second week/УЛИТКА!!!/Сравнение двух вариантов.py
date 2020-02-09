import time

n = int(input())

start_time = time.time()

sheet = [[0]*n for j in range(n)]
y = 1
# Номера строки и столбца.
i, j = 0, 0

for y in range(1, n**2):
    sheet[i][j] = y

    if i <= j+1 and i+j < n-1:
        j += 1
    elif  i < j:
        i += 1
    elif j >= n-i:
        j -= 1
    elif i > j+1:
        i -= 1
    y += 1
sheet[i][j] = y

for lists in sheet:
    print(*lists)
print("time elapsed: {:.10f}s".format(time.time() - start_time))

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------

start_time = time.time()

sheet = [[0 for i in range(n)] for j in range(n)]
y = 1
# Номера строки и столбца.
i, j = 0, 0

# Блокировка занятых ячеек по сточкам и столбцам
hor_top, hor_below = 0, 0
ver_r, ver_l = 0, 0

while y <= n**2:

    for j in range(ver_l, n - ver_r):
        sheet[i][j] = y
        y += 1
    hor_top += 1

    for i in range(hor_top, n - hor_below):
        sheet[i][j] = y
        y += 1
    ver_r += 1

    for j in range(n-1 - ver_r, ver_l - 1, -1):
        sheet[i][j] = y
        y += 1
    hor_below += 1

    for i in range(n-1 - hor_below, hor_top - 1, -1):
        sheet[i][j] = y
        y += 1
    ver_l += 1

for x in sheet:
    print(*x)
print("time elapsed: {:.10f}s".format(time.time() - start_time))