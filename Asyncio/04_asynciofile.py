import asyncio

import aiofiles

from multithreding.decorators import measure_time, async_measure_time


@measure_time
def read_large_file():
    with open('..\\data\\ENRUS.TXT', 'r') as f:
        return f.read()


@async_measure_time
async def async_read_large_file():
    async with aiofiles.open('..\\data\\ENRUS.TXT', 'r') as f:
        return await f.read()


def count_words(text):
    return len(text.split(' '))


@async_measure_time
async def async_main():
    text = await async_read_large_file()
    print(count_words(text))


@measure_time
def main():
    text = read_large_file()
    print(count_words(text))


if __name__ == '__main__':
    asyncio.run(async_main())
    print(measure_time(async_main))

    main()
    print(measure_time(main))
