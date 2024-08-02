import os
import asyncio
from .checker import IPTVChecker
from .utils import read_playlist_urls, create_index_m3u

if __name__ == "__main__":
    # Получение пути к файлу playlists.txt, который находится на уровень выше от проекта
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    playlists_path = os.path.join(base_dir, 'playlists.txt')

    # Чтение URL-ов из файла playlists.txt
    playlist_urls = read_playlist_urls(playlists_path)

    # Ограничение числа одновременных задач
    semaphore = asyncio.Semaphore(100)  # Задаем лимит в 10 одновременных задач

    # Создание экземпляра IPTVChecker для каждого URL и запуск его
    async def main():
        tasks = []
        for country_name, playlist_url in playlist_urls.items():
            if playlist_url.startswith(("http://", "https://")):
                checker = IPTVChecker(country_name, playlist_url, semaphore)
                tasks.append(checker.run())
            else:
                print(f"Invalid URL: {playlist_url} for {country_name}")
        await asyncio.gather(*tasks)

        # Создание главного index.m3u файла
        create_index_m3u(playlist_urls)

    asyncio.run(main())
