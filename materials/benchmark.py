"""
A micro benchmark comparing the performance of sending messages into a coroutine vs. sending messages into an object
"""
from timeit import timeit
from materials.decorator import coroutine


# An object
class GrepHandler:
    def __init__(self, pattern, target):
        self._pattern = pattern
        self._target = target

    def send(self, line):
        if self._pattern in line:
            self._target.send(line)


# a coroutine
@coroutine
def grep(pattern, target):
    while True:
        line = yield
        if pattern in line:
            target.send(line)


# A null-sink to send data
@coroutine
def null():
    while True:
        item = yield


if __name__ == "__main__":
    # A benchmark
    line = "python is nice"
    p1 = grep("python", null())  # coroutine
    p2 = GrepHandler("python", null())  # an object

    print("Coroutine: ", timeit("p1.send(line)", "from __main__ import line, p1"))
    print("Object: ", timeit("p2.send(line)", "from __main__ import line, p2"))
