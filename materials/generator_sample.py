def generator_sample():
    yield 100


if __name__ == "__main__":
    generator = generator_sample()
    print(generator)
    print(type(generator))
    print(dir(generator))
    print(hasattr(generator, "__next__"))
    print(next(generator))
    print(next(generator))

    generator_list = list(generator_sample())
    print(generator_list)
    print(len(generator_list))

    print(sum(generator_sample()))
