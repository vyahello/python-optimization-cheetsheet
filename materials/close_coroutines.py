def counter(maximum):
    initial = 0
    while initial < maximum:
        value = yield initial  # equals to None till .send(number) is called
        # If value is given (remember default is None) then change the counter
        if value is not None:
            initial = value
        else:
            initial += 1


c = counter(10)
for i in c:
    print(i)
    if i == 5:
        c.close()


def print_name(prefix):
    print("Search for", prefix, "prefix")
    try:
        while True:
            name = yield
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("Closing generator!")


if __name__ == "__main__":
    pn = print_name("Dear")
    next(pn)  # calls first yield expression
    pn.send("Alex")
    pn.send("Dear Alex")  # matches with prefix
