import asyncio


async def count():  # single event loop
    print("One")
    await asyncio.sleep(1)  # when task reaches here it will sleep for 1 second and says to do other job meantime
    print("Two")            # temporary gives control to another function


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")  # 1.01 seconds
