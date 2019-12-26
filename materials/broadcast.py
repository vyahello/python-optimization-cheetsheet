"""
An example of broadcasting a data stream onto multiple coroutine targets.
"""

import time
from materials.decorator import coroutine


# A data source. This is not a coroutine, but it sends data into one target
def follow(thefile, target):
    thefile.seek(0, 2)  # Go to end of a file
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        target.send(line)


# A filter
@coroutine
def grep(pattern, target):
    while True:
        line = yield  # Receive a line
        if pattern in line:
            target.send(line)  # Send to next stage


# A sink. A coroutine that receives data
@coroutine
def printer():
    while True:
        line = yield
        print(line)


# Broadcast a stream onto multiple targets
@coroutine
def broadcast(targets):
    while True:
        item = yield
        for target in targets:
            target.send(item)


if __name__ == "__main__":
    f = open("access.log", "+a")
    follow(f, broadcast((grep("python", printer()), grep("ply", printer()), grep("swig", printer()))))
