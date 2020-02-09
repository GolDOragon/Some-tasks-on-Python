'''
Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
Также реализуйте новое исключение NonPositiveError.

В классе PositiveList переопределите метод append(self, x) таким образом, чтобы при попытке добавить неположительное целое число бросалось исключение NonPositiveError и число не добавлялось, а при попытке добавить положительное целое число, число добавлялось бы как в стандартный list.

В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.

Примечание:
Положительными считаются числа, строго большие нуля.

'''
'''
def greet(name):
    if name[0].isupper():
        return 'Hello, ' + name
    else:
        raise BadName("'{}' is inappropriate name".format(name))

'''
class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError(f'{x} is not positive number ')

class NonPositiveError(Exception):
    pass

lst = PositiveList()
a = [1, 2, 3, 4, -5]

for i in a:
    lst.append(i)

print(lst)