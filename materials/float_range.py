def float_range(start, stop, increment):
    initial_point = start
    while initial_point < stop:
        yield initial_point
        initial_point += increment


if __name__ == "__main__":
    for number in float_range(0, 4, 0.5):
        print(number)
