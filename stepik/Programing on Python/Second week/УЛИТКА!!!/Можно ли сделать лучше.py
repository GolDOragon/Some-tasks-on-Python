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