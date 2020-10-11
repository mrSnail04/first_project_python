import asyncio

from multithreding.decorators import async_measure_time


async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')


@async_measure_time
async def main():
    await asyncio.gather(tick(), tick(), tick())


if __name__ == '__main__':
    asyncio.run(main())
