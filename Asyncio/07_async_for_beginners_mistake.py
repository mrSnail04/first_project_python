import asyncio


class AsyncIterator():
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __aiter__(self):
        return self

    async def __anext__(self):
        print(f'Start {self.i}')
        await asyncio.sleep(1)
        print(f'End {self.i}')

        if self.i >= self.n:
            raise StopAsyncIteration
        self.i += 1
        return self.i


async def main():
    async for n in AsyncIterator(10):
        print(f'Finally {n}')


if __name__ == '__main__':
    asyncio.run(main())

# Ожидают результат:
# start 0
# start 1
# start 2
# .. start 10
#
# end 0
# end 1
# end 2
# .. end 10
#
# finally 0
# finally 1
# finally 2
# .. finally 10