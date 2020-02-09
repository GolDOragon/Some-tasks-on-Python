objects = [1, 2, 3, 4, 5, 5, 3, 3, 2, 1]

n = len(objects)
ans = n
for i in range(n):
    for j in range(i):
        if id(objects[i] )== id(objects[j]):
            ans -= 1
            break

print(ans)
