def counter(maximum):
    initial = 0
    while initial < maximum:
        value = yield initial  # equals to None till .send(number) is called
        # If value is given (remember default is None) then change the counter
        if value is not None:
            initial = value
        else:
            initial += 1


if __name__ == "__main__":
    c = counter(10)
    for i in c:
        print(i)
        if i == 5:
            c.throw(ValueError("It is too large"))
