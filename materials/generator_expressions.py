even_numbers = (num for num in range(15) if num % 2 == 0)
print(even_numbers)
for num in even_numbers:
    print(num)


def multiply_each_by(multiplier):
    return (element * multiplier for element in range(5))


multiplied_container = multiply_each_by(multiplier=3)
print(multiplied_container)
for obj in multiplied_container:
    print(obj)
