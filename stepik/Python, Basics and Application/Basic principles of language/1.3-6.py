def g():
    print('I am in funtion g')

def f():
    print('I am in function f')
    g()
    print('I am in function f')

print('I am outside of any function')
f()
print('I am outside of any function')

x = [1, 2, 3]
x.append(4)
x.append(5)
print(x)

top = x.pop()
print(top)
print(x)

top = x.pop()
print(top)
print(x)
