def checkio(number):
    feed_pegeons = []
    i = 0
    while number > 0:
        i += 1
        for j in range(i):
            if number > 0:
                feed_pegeons.append(1)
                number -= 1
            else:
                break
        for j in range(len(feed_pegeons)):
            if number > 0:
                feed_pegeons[j] += 1
                number -= 1
            else:
                break
    print(feed_pegeons)
    print(len(feed_pegeons))
    return len(feed_pegeons)
checkio(10)
"""
    if number == 2:
        return 1
    lst = []
    i = 1
    while True:
        for j in range(i):
            lst.append(1)
        lst = [j + 1 for j in lst]
        if sum(lst) > number:
            return len(lst)
        i += 1

print(checkio(10))




    def arithmetic_progression(n):
        return n * (2 * 1 + 1 * (n - 1)) / 2

    def limit(step):
        sum = 0
        for i in range(step):
            sum += arithmetic_progression(i)
        return sum
    i = 0
    while limit(i) < number:
        i += 1
    print(i)
    return i
checkio(10)


    def peg(S):
        return ((1 + 8 * S) ** 0.5 - 1) // 2
    S = []
    a = peg(number)
    for i in range(1, int(a)):
        S.append((a - i) * i)

    ans = len(S) - 1 + S[-1]
    print(ans)
    return ans
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    assert checkio(5) == 3, "3rd example"
    assert checkio(10) == 6, "4th example"

'''
    def peg(S):
        return ((1 + 8 * S) ** 0.5 - 1) // 2


    def bread(n):
        return n * (2 * 1 + 1 * (n - 1)) / 2


    a = peg(number)
    b = bread(peg(number))
    asd = a + number - b

    return peg(number) + number - bread(peg(number))

'''
(4 - 1) * 1 + (4 - 2) * 2 + (4 - 3) * 3

a = peg(number)

for i in range(1, int(a)):
    print((a-i) * i)

def peg(S):
    return ((1 + 8 * S) ** 0.5 - 1) // 2
S = []
for i in range(1, int(a)):
    S.append((a - i) * i)

ans = len(S) - 1 + S[-1]
"""