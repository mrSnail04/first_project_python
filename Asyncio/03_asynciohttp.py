import asyncio

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


def print_photo_title(photos):
    for photo in photos:
        print(f'{photo.title}', end='\n')


async def photo_by_album(task_name, album, session):
    print(f'{task_name}')
    url = f'http://jsonplaceholder.typicode.com/photos?albumId={album}'
    response = await session.get(url)
    photo_json = await response.json()

    return [Photo.from_json(photo) for photo in photo_json]


@async_measure_time
async def main():
    # async with aiohttp.ClientSession() as session: #Вывести title фоток
    #     photos = await photo_by_album('Task 1', 3, session)
    #     print_photo_title(photos)
    async with aiohttp.ClientSession() as session: #посчитать кол-во фото в альбомах
        photo_in_album = await asyncio.gather(
            *(photo_by_album(f'Task {i + 1}', album, session) for i, album in enumerate(range(2, 30))))
        photos_count = sum([len(cur) for cur in photo_in_album])
        print(f'{photos_count=}')


if __name__ == '__main__':
    asyncio.run(main())
