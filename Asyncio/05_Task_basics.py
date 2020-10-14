import asyncio


async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')
    return ('Tick.Tock')


async def main():
    t1 = asyncio.create_task(tick(), name='Task1')
    t2 = asyncio.ensure_future(tick())

    result = await asyncio.gather(t1, t2)

    for x in result:
        print(x)

    print(f'{t1.get_name()}. Done={t1.done()} ')
    print(f'{t2.get_name()}. Done={t2.done()} ')

if __name__ == '__main__':
    asyncio.run(main())
