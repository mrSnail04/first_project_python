import asyncio



async def tick():
    print('Tick')
    await asyncio.sleep(1)
    print('Tock')


async def main():
    awaitable_obj = asyncio.gather(tick(), tick(), tick())
    for task in asyncio.all_tasks():
        print(task, end='\n')
    await awaitable_obj


if __name__ == '__main__':
    #asyncio.run(main())
    loop = asyncio.get_event_loop()
    try:
        loop.create_task(main())
        loop.run_forever()
        #loop.run_until_complete(main())
        print('Coroutines have finished')
    except KeyboardInterrupt: #ctrl+C что бы закрыть loop
        print('Manually closed application')
    finally:
        loop.close()
        print('Loop is closed')
        print(f'loop is closed = {loop.is_closed()}')

