class BadName(Exception):
    pass


def greet(name):
    if name[0].isupper():
        return 'Hello, ' + name
    else:
        raise BadName("'{}' is inappropriate name".format(name))

print(greet('Anton'))
print(greet('anton'))

'''
while True:
    try:
        name = input('Please enter your name: ')
        greeting = greet(name)
        print(greeting)
    except ValueError:
        print('Please try again')
    else:
        break
'''
