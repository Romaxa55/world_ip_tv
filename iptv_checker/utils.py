import os

import aiohttp
import logging

logger = logging.getLogger(__name__)


async def download_playlist(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                return await response.text()
    except aiohttp.ClientError as e:
        logger.error(f"Client error while downloading playlist {url}: {e}")
        raise
    except aiohttp.client_exceptions.NonHttpUrlClientError as e:
        logger.error(f"Non-HTTP URL error for {url}: {e}")
        raise
    except asyncio.TimeoutError:
        logger.error(f"Timeout error while downloading playlist {url}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error while downloading playlist {url}: {e}")
        raise


def read_playlist_urls(file_path):
    with open(file_path, 'r') as f:
        return {line.split()[0]: line.split()[1] for line in f if line.strip()}

def create_index_m3u(playlist_urls):
    index_content = "#EXTM3U\n"
    base_url = "https://yourdomain.github.io/iptv/"  # Замените на свой домен

    for country_name, playlist_url in playlist_urls.items():
        filename = os.path.basename(playlist_url)
        country_url = f"{base_url}{filename}"
        index_content += f"#EXTINF:-1,{country_name}\n{country_url}\n"

    # Сохранение index.m3u файла
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, '..', 'output')
    os.makedirs(output_dir, exist_ok=True)
    index_path = os.path.join(output_dir, 'index.m3u')

    with open(index_path, 'w') as f:
        f.write(index_content)

    print(f"Index file created at {index_path}")
