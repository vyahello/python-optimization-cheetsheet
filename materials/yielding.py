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
    print(f"Starting to count from {number}!")
    while number > 0:
        yield number
        number -= 1
    print("Done!")


def increment(start, stop):
    yield from range(start, stop)


if __name__ == "__main__":
    countdown = countdown_from(number=10)
    for count in countdown:
        print(count)

    incremental = increment(start=1, stop=10)
    for inc in incremental:
        print(inc)
