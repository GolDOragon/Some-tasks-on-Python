

def f(x):

    if x <= -2:
        ans = 1 - (x + 2)**2

    elif x <= 2:
        ans = - x / 2

    elif x > 2:
        ans = (x - 2)**2 + 1

    return ans

a =float(input())

print(f(a))
