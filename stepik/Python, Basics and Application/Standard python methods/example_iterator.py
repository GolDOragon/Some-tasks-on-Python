class MyIterator:
    def __init__(self, iterable):
        self.index = 0
        self.iterable = iterable

    def __next__(self):
        if self.index < len(self.iterable):
            self.index += 1
            return self.iterable[self.index - 1]
        raise StopIteration


class MyList:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.lst):
            self.index += 1
            return self.lst[self.index - 1] / 2
        raise StopIteration


l = MyList([1, 2, 3, 4, 5])

print(type(l))
for i in l:
    print(i)
