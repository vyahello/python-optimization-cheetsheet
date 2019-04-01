# Python generators cheetsheet
Implementation of python generators cheetsheet which is aimed on helping to comprehend python generators by newcomers.

## Table of contents
- [Generator functions](#generator-functions)
- [Generator expressions](#generator-expressions)
- [Create new iteration patterns with generators](#create-new-iteration-patterns-with-generators)
- [Advanced operations with generators](#additional-materials)
- [Generators as memory efficient objects](#generators-as-memory-efficient-objects)

### Generator functions
Basic generator sample
```python
# generator_sample.py

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
Generator with multiple yield statements
```python
# multiple_yields.py

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
Yielding iterable with generator
```python
# yielding.py

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
Sending values to generators
```python
# send_values.py

def generator(input_number):
    number = yield
    while number < input_number:
        number = yield number
        number += 1


g = generator(10)
next(g)
print(g.send(5))
```

### Generator expressions
```python
# generator_expressions.py

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

### Create new iteration patterns with generators
```python
# float_range.py

def float_range(start, stop, increment):
    initial_point = start
    while initial_point < stop:
        yield initial_point
        initial_point += increment


for number in float_range(0, 4, 0.5):
    print(number)
```
```python
# countdown.py

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

### Advanced operations with generators
Slice generator elements
```python
# slice_generators.py

import itertools


def doubles_of(number):
    for num in range(number):
        yield 2 * num


print(help(itertools.islice))

for element in itertools.islice(doubles_of(50), 10, 15):
    print(element)
```
Concatenate generators sequence
```python
# concatenate_generators.py

import itertools


def fruits():
    for fruit in ['apple', 'orange', 'banana']:
        yield fruit


def vegetables():
    for vegetable in ['potato', 'tomato', 'cucumber']:
        yield vegetable


print(help(itertools.chain))

bucket = itertools.chain(fruits(), vegetables())
for item in bucket:
    print(item)
```
Zip generators elements
```python
# zip_generators.py

import itertools


def ascending():
    yield from (1, 2, 3, 4, 5)


def descending():
    yield from (5, 4, 3, 2, 1)


for pair in itertools.zip_longest(ascending(), descending()):
    print(pair)
```

### Generators as memory efficient objects
```python
# memory_efficacy.py

import sys
import cProfile


generator_container = (num * 3 for num in range(10000000) if num % 6 == 0 or num % 7 == 0)
print(sys.getsizeof(generator_container))

list_container = [num * 3 for num in range(10000000) if num % 6 == 0 or num % 7 == 0]
print(sys.getsizeof(list_container))

print(cProfile.run('sum(generator_container)'))
print(cProfile.run('sum(list_container)'))
```

### Additional materials
- https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions
- https://www.python.org/dev/peps/pep-0289
- https://www.python.org/dev/peps/pep-0342
- https://docs.python.org/3.6/glossary.html#term-generator
- https://realpython.com/introduction-to-python-generators


# Contributing
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vyahello@gmail.com"
  ```
- `python3.6` is required to run the code
