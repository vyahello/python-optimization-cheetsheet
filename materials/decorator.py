def coroutine(func):
    """
    A decorator function that eliminates the need to call .next()
    when starting a coroutine.
    """
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start


if __name__ == "__main__":
    @coroutine
    def grep(pattern):
        print(f"Search for '{pattern}' pattern")
        while True:
            value = yield
            if pattern in value:
                print(value)


    g = grep("python")
    # Notice now you don't need a next() call here
    g.send("Yeah, but no, but yeah, but no")
    g.send("A series of tubes")
    g.send("python generators rock!")
