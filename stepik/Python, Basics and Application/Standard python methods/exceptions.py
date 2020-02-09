class BadName(Exception):
    pass

_names = 'as'

def greet(name):
    if name[0].isupper():
        return 'Hello, ' + name
    else:
        raise BadName("'{}' is inappropriate name".format(name))

print('Import is execution')
