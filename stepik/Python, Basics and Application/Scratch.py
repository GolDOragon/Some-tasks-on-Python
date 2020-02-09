ok_status = True
vowels = ['a', 'u', 'i', 'e', 'o']

def check(word):
    global ok_status
    for vowel in vowels:
        if vowel in word:
            return True

    ok_status = False
    return False
print(check('abacaca'))
print(ok_status)
print(check('www'))
print(ok_status)

class A:
    pass

class B(A):
    pass

class C:
    pass

class D(C):
    pass

class E(B, C, D):
    pass

print(E.mro())