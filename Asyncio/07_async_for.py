import asyncio


async def fetch_doc(doc):
    await asyncio.sleep(3)
    return doc


async def get_docs(docs):
    for cur_doc in docs:
        doc = await fetch_doc(cur_doc)
        for page in doc:
            await asyncio.sleep(1)
            yield page


async def main():
    async for page in get_docs(['doc1', 'doc2']):
        print(f'Finally {page}')


if __name__ == '__main__':
    asyncio.run(main())
