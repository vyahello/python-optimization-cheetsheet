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
