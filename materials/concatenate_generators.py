import itertools


def fruits():
    for fruit in ("apple", "orange", "banana"):
        yield fruit


def vegetables():
    for vegetable in ("potato", "tomato", "cucumber"):
        yield vegetable


print(help(itertools.chain))

bucket = itertools.chain(fruits(), vegetables())
for item in bucket:
    print(item)
