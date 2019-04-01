def generator(input_number):
    number = yield
    while number < input_number:
        number = yield number
        number += 1


g = generator(10)
next(g)
print(g.send(5))
