'''try:
    x = [1, 2, 'hello', 7]
    x.sort()
    print(x)
except TypeError:
    print('Type error :(')

print('I can catch')
'''
'''
def f(x, y):
    try:
        return x / y
    except (TypeError, ZeroDivisionError) as e:
        print(type(e))
        print(e)
        print(e.args)

print(f(5, 0))
print(f(5,'aa'))
'''

'''
def f(x, y):
    try:
        return x / y
    except:
        print('Some error')


print(f(5, 0))
print(f(5, 'aa'))
print(ZeroDivisionError.mro())
'''

'''
try:
    15 / 0
except ArithmeticError:
    print('ArithmeticError')
except ZeroDivisionError:
    print('zero')
print(ZeroDivisionError.mro())
'''


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
       print('division by zero')
    else:
        print('rezult is', result)
    finally:
        print('finally')

divide(2, 1)
divide(2, 0)
print('last')
divide(2, [])