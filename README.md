[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub contributors](https://img.shields.io/github/contributors/vyahello/python-optimization-cheetsheet.svg)](https://GitHub.com/vyahello/python-optimization-cheetsheet/graphs/contributors/)

# Python optimization cheetsheet
Implementation of python optimization cheetsheet (`yield`, `generators`, `coroutines` and `asyncio`). Source code located [here](materials).

**Tools**
- python 3.6, 3.7, 3.8
- [asyncio](https://docs.python.org/3/library/asyncio.html)
- [black](https://black.readthedocs.io/en/stable/)
- [pylint](https://www.pylint.org/)

## Content
- [generators](#generators)
  - [functions](#functions)
  - [expressions](#expressions)
  - [new iteration patterns with generators](#new-iteration-patterns-with-generators)
  - [advanced operations with generators](#advanced-operations-with-generators)
  - [memory efficient objects](#memory-efficient-objects)
- [coroutines](#coroutines)
- [asyncio](#asyncio)

## Generators
> Basic functions calculate values and returns them, otherwise generators return a lazy iterator that returns a stream of values.
> 
> A common use case of generators is to work with data streams or large files like `.csv` files
### functions
**Basic generator sample**
```python
# materials/generator_sample.py

def generator_sample():
    yield 100


generator = generator_sample()
print(generator)
print(type(generator))
print(dir(generator))
print(hasattr(generator, '__next__'))
print(next(generator))
print(next(generator))

generator_list = list(generator_sample())
print(generator_list)
print(len(generator_list))

print(sum(generator_sample()))
```
**Generator with multiple yield statements**
```python
# materials/multiple_yields.py

def multiple_yields():
    yield 'This'
    yield 'is'
    yield 'my'
    yield 'generator'
    yield 'function'
    yield '!'


values = multiple_yields()
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))

other_values = multiple_yields()
for value in other_values:
    print(value)
```
**Yielding iterable with generator**
> Any function that has `yield` operator is a generator.
>
> Generation an infinite sequence, however, will require the use of a generator, since your computer memory is finite.
> Yield is an expression rather than statement.
```python
# materials/yielding.py

def is_palindrome_number(number):
    return number == int(str(number)[::-1])


def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1


for number in infinite_sequence():
    if is_palindrome_number(number):
        print(number)


def countdown_from(number):
    print(f'Starting to count from {number}!')
    while number > 0:
        yield number
        number -= 1
    print('Done!')


def increment(start, stop):
    yield from range(start, stop)


countdown = countdown_from(number=10)
for count in countdown:
    print(count)


incremental = increment(start=1, stop=10)
for inc in incremental:
    print(inc)
```

### expressions
```python
# materials/generator_expressions.py

even_numbers = (num for num in range(15) if num % 2 == 0)
print(even_numbers)
for num in even_numbers:
    print(num)


def multiply_each_by(multiplier):
    return (element * multiplier for element in range(5))


multiplied_container = multiply_each_by(multiplier=3)
print(multiplied_container)
for obj in multiplied_container:
    print(obj)
```

### new iteration patterns with generators
```python
# materials/float_range.py

def float_range(start, stop, increment):
    initial_point = start
    while initial_point < stop:
        yield initial_point
        initial_point += increment


for number in float_range(0, 4, 0.5):
    print(number)
```
```python
# materials/countdown.py

class Countdown:
    def __init__(self, start):
        self._start = start

    def __iter__(self):
        number = self._start
        while number > 0:
            yield number
            number -= 1

    def __reversed__(self):
        number = 1
        while number <= self._start:
            yield number
            number += 1


forward_countdown = Countdown(10)
for f_count in forward_countdown:
    print(f_count)

reversed_countdown = reversed(Countdown(10))
for r_count in reversed_countdown:
    print(r_count)
```

### advanced operations with generators
**Slice generator elements**
```python
# materials/slice_generators.py

import itertools


def doubles_of(number):
    for num in range(number):
        yield 2 * num


print(help(itertools.islice))

for element in itertools.islice(doubles_of(50), 10, 15):
    print(element)
```
**Concatenate generators sequence**
```python
# materials/concatenate_generators.py

import itertools


def fruits():
    for fruit in ('apple', 'orange', 'banana'):
        yield fruit


def vegetables():
    for vegetable in ('potato', 'tomato', 'cucumber'):
        yield vegetable


print(help(itertools.chain))

bucket = itertools.chain(fruits(), vegetables())
for item in bucket:
    print(item)
```
**Zip generators elements**
```python
# materials/zip_generators.py

import itertools


def ascending():
    yield from (1, 2, 3, 4, 5)


def descending():
    yield from (5, 4, 3, 2, 1)


for pair in itertools.zip_longest(ascending(), descending()):
    print(pair)
```

### memory efficient objects
```python
# materials/memory_efficacy.py

import sys
import cProfile

generator_container = (num * 3 for num in range(10000000) if num % 6 == 0 or num % 7 == 0)
print(sys.getsizeof(generator_container))

list_container = [num * 3 for num in range(10000000) if num % 6 == 0 or num % 7 == 0]
print(sys.getsizeof(list_container))

print(cProfile.run('sum(generator_container)'))
print(cProfile.run('sum(list_container)'))
```

## Coroutines
> Coroutines can consume and produce data. They can pause stream execution till next message is sent.
>
> Generators produce data for iteration while coroutines can also consume data.

**Sending values with `.send` method**
```python
# materials/send_coroutines.py

def coroutine():
    while True:
        value = yield  # allows to manipulate yielded value
        print(value)


i = coroutine()
i.send(None)  # initial value should be 'None'
i.send(1)
i.send(10)


def counter(maximum):
    initial = 0
    while initial < maximum:
        value = (yield initial)  # equals to None till .send(number) is called
        # If value is given (remember default is None) then change the counter
        if value is not None:
            initial = value
        else:
            initial += 1


c = counter(10)
print(next(c))  # 0
print(next(c))  # 1
print(c.send(5))  # 5
print(next(c))  # 6

def is_palindrome_number(number):
    return number == int(str(number)[::-1])


def infinite_palindromes():
    number = 0
    while True:
        if is_palindrome_number(number):
            i = (yield number)
            if i is not None:
                number = i
        number += 1


c = infinite_palindromes()
print(next(c))  # 0
print(next(c))  # 1
print(c.send(100))  # 101
print(next(c))  # 111


def print_name(prefix):
    print("Search for", prefix, "prefix")
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
```

**Raise an exception with `.throw` method**
> `.throw()` allows you to throw exceptions through the generator.

```python
# materials/throw_coroutines.py

def counter(maximum):
    initial = 0
    while initial < maximum:
        value = (yield initial)  # equals to None till .send(number) is called
        # If value is given (remember default is None) then change the counter
        if value is not None:
            initial = value
        else:
            initial += 1


c = counter(10)
for i in c:
    print(i)
    if i == 5:
        c.throw(ValueError("It is too large"))
```

**Stop generator with `.close` method**
> `.close()` allows you to stop a generator. Instead of calling `.throw()`, you use `.close()` (it calls StopIteration error). 

```python
# materials/close_coroutines.py

def counter(maximum):
    initial = 0
    while initial < maximum:
        value = (yield initial)  # equals to None till .send(number) is called
        # If value is given (remember default is None) then change the counter
        if value is not None:
            initial = value
        else:
            initial += 1


c = counter(10)
for i in c:
    print(i)
    if i == 5:
        c.close()  # stops as here is raises 'StopIteration' exception


def print_name(prefix):
    print("Search for", prefix, "prefix")
    try:
        while True:
            name = yield
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("Closing generator!")


pn = print_name("Dear")
next(pn)  # calls first yield expression
pn.send("Alex")
pn.send("Dear Alex")  # matches with prefix
```

**Create pipelines**
> Coroutines can be used to set pipes

```python
# materials/coroutine_chaining.py

def producer(sentence: str, next_coroutine):
    """Split strings and feed it to pattern_filter coroutine."""
    tokens = sentence.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()


def pattern_filter(pattern="ing", next_coroutine=None):
    """Search for pattern and if pattern got matched, send it to print_token coroutine."""
    print(f"Search for {pattern} pattern")
    try:
        while True:
            token = yield
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print("Done with filtering")


def print_token():
    """Act as a sink, simply print the token."""
    print("I'm sink, I'll print tokens")
    try:
        while True:
            token = yield
            print(token)
    except GeneratorExit:
        print("Done with printing")


pt = print_token()
next(pt)
pf = pattern_filter(next_coroutine=pt)
next(pf)

sentence = "Bob is running behind a fast moving car"
producer(sentence, pf)
```

**Tricks**
```python
# materials/decorator.py

def coroutine(func):
    """A decorator function that eliminates the need to call .next() when starting a coroutine."""
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start


if __name__ == "__main__":
    @coroutine
    def grep(pattern):
        print(f"Search for '{pattern}' pattern")
        while True:
            value = yield
            if pattern in value:
                print(value)


    g = grep("python")
    # Notice now you don't need a next() call here
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")
```

## AsyncIO

### Materials
- https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
- https://www.python.org/dev/peps/pep-0289
- https://www.python.org/dev/peps/pep-0342
- https://docs.python.org/3/library/asyncio.html
- https://docs.python.org/3.6/glossary.html#term-generator
- https://realpython.com/introduction-to-python-generators
- https://www.geeksforgeeks.org/coroutine-in-python
- http://www.dabeaz.com/coroutines

### Meta
Author – Volodymyr Yahello vyahello@gmail.com

Distributed under the `Apache (2.0)` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure **git** for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
