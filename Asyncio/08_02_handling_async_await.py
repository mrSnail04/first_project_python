import asyncio
import time
import aiohttp
from multithreding.decorators import async_measure_time


class Photo:
    def __init__(self, album_id, photo_id, title, url, thumbnail_url):
        self.album_id = album_id
        self.photo_id = photo_id
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url

    @classmethod
    def from_json(cls, obj):
        return Photo(obj['albumId'], obj['id'], obj['title'], obj['url'], obj['thumbnailUrl'])


def print_photo_titles(photos):
    for photo in photos:
        print(f'{photo.title}', end='\n')


async def photos_by_album(task_name, album, session):
    if not isinstance(album, int):
        raise RuntimeError('Invalid album number')
    print(f'{task_name=}')
    url = f'http://jsonplaceholder.typicode.com/photos?albums/{album}/photos/'
    response = await session.get(url)
    photo_json = await response.json()
    await asyncio.sleep(1)

    return [Photo.from_json(photo) for photo in photo_json]


async def download_albums(albums):
    async with aiohttp.ClientSession() as session:
        for album in albums:
            try:
                yield await photos_by_album(f't{album}', album, session)
            except Exception as ex:
                print(repr(ex))


@async_measure_time
async def main():
    async for photos in download_albums([1, 2, 'a', 4]):
        print_photo_titles(photos)


if __name__ == '__main__':
    asyncio.run(main())
    time.sleep(3)
    print('Main ended')
