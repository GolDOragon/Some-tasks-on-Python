'''import random


class RandomIterator:
    def __iter__(self):
        raise self

    def __init__(self, k):
        self.k = k
        self.i = 0

    def __next__(self):
        if self.i < self.k:
            self.i += 1
            return random()
        else:
            raise StopIteration


def random_generator(k):
    for i in range(k):
        yield random()


gen = random_generator(3)
print(gen)
print(type(gen))
'''

def simple_gen():
    print('Checkpoint 1')
    yield 1
    print('Checkpoint 2')
    return "No more elements"
    yield 2
    print('Checkpoint 3')

gen = simple_gen()
x = next(gen)
print(x)
y = next(gen)
print(y)
z = next(gen)