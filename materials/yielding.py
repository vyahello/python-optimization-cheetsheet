def countdown_from(number):
    print(f"Starting to count from {number}!")
    while number > 0:
        yield number
        number -= 1
    print("Done!")


def increment(start, stop):
    yield from range(start, stop)


countdown = countdown_from(number=10)
for count in countdown:
    print(count)


incremental = increment(start=1, stop=10)
for inc in incremental:
    print(inc)
