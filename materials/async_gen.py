async def genfunc():
    yield 1
    yield 2


if __name__ == "__main__":
    gen = genfunc()
    assert gen.__aiter__() is gen
    assert await gen.__anext__() == 1
    assert await gen.__anext__() == 2
    await gen.__anext__()  # This line will raise StopAsyncIteration.
