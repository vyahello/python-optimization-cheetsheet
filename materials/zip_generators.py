import itertools


def ascending():
    yield from (1, 2, 3, 4, 5)


def descending():
    yield from (5, 4, 3, 2, 1)


for pair in itertools.zip_longest(ascending(), descending()):
    print(pair)
