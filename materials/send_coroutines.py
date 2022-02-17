from typing import Coroutine


def coroutine():
    while True:
        value = yield  # allows manipulating yielded value
        print(value)


i = coroutine()
i.send(None)  # initial value should be 'None'
i.send(1)
i.send(10)


def counter(maximum):
    initial = 0
    while initial < maximum:
        value = yield initial  # equals to None till .send(number) is called
        # If value is given (remember default is None) then change the counter
        if value is not None:
            initial = value
        else:
            initial += 1


c = counter(10)
print(next(c))  # 0
print(next(c))  # 1
c.send(5)
print(next(c))  # 6


def is_palindrome_number(number):
    return number == int(str(number)[::-1])


def infinite_palindromes():
    number = 0
    while True:
        if is_palindrome_number(number):
            i = yield number
            if i is not None:
                number = i
        number += 1


c = infinite_palindromes()
print(next(c))  # 0
print(next(c))  # 1
print(c.send(100))  # 101
print(next(c))  # 111


def print_name(prefix):
    print("Search for ", prefix, " prefix")
    while True:
        name = yield
        if prefix in name:
            print(name)


pn = print_name("Dear")
next(pn)  # calls first yield expression
pn.send("Alex")
pn.send("Dear Alex")  # matches with prefix


def grep(pattern):
    print(f"Search for '{pattern}' pattern")
    while True:
        value = yield
        if pattern in value:
            print(f"Matched: '{value}'")


g = grep("hey")
next(g)  # to start coroutine
g.send("hello")
g.send("hey")
g.send("hey Mike")
