
numbers = [int(i) for i in input().split()]
minimun = numbers[0]

for num in numbers:
    if num < minimun:
        minimun = num
print(minimun)