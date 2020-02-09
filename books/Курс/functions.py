m = [1, 2, 3, 4, 5, 6]
n = m[:]
for i in range(len(m) - 1):
    print(i, m[i])
    if m[i] % 2 == 1:
        del m[i]

print(m)
