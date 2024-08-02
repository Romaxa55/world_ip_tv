import os
import asyncio
from .checker import IPTVChecker
from .utils import read_playlist_urls, create_index_m3u


async def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    playlists_path = os.path.join(base_dir, 'playlists.txt')

    playlist_urls = read_playlist_urls(playlists_path)
    semaphore = asyncio.Semaphore(200)

    tasks = []
    for country_name, playlist_url in playlist_urls.items():
        checker = IPTVChecker(country_name, playlist_url, semaphore)
        tasks.append(checker.run())

    await asyncio.gather(*tasks)

    create_index_m3u()


if __name__ == "__main__":
    asyncio.run(main())
