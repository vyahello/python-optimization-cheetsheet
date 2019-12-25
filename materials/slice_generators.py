import itertools


def doubles_of(number):
    for num in range(number):
        yield 2 * num


if __name__ == "__main__":
    print(help(itertools.islice))

    for element in itertools.islice(doubles_of(50), 10, 15):
        print(element)
