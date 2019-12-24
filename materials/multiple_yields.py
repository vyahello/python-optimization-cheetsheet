def multiple_yields():
    yield "This"
    yield "is"
    yield "my"
    yield "generator"
    yield "function"
    yield "!"


values = multiple_yields()
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))

other_values = multiple_yields()
for value in other_values:
    print(value)
