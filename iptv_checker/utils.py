import asyncio
import os
import re

import aiohttp
import logging

logger = logging.getLogger(__name__)


def read_playlist_urls(filepath):
    playlist_urls = {}
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or ':' not in line:
                continue
            country, url = line.split(':', 1)
            url = url.strip()
            if not url.startswith(('http://', 'https://')):
                logger.warning(f"Invalid URL for {country}: {url}")
                continue
            playlist_urls[country.strip()] = url
    return playlist_urls


async def download_playlist(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    return await response.text()
                else:
                    logger.error(f"Failed to download playlist from {url}: HTTP {response.status}")
        except aiohttp.ClientError as e:
            logger.error(f"Client error while downloading playlist from {url}: {e}")
        except asyncio.TimeoutError:
            logger.error(f"Timeout while downloading playlist from {url}")

    return ""


def create_index_m3u():
    index_content = "#EXTM3U\n"
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, 'output')

    # Словарь для хранения каналов по группам
    grouped_channels = {}

    for root, _, files in os.walk(output_dir):
        for file in files:
            if file.endswith('.m3u') and file != 'index.m3u':
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    lines = content.splitlines()[1:]
                    for i in range(0, len(lines), 2):
                        group_title = re.search(r'group-title="([^"]+)"', lines[i]).group(1)
                        channel_info = f'{lines[i]}\n{lines[i + 1]}\n'
                        if group_title not in grouped_channels:
                            grouped_channels[group_title] = []
                        grouped_channels[group_title].append(channel_info)

    # Сортируем группы по алфавиту
    for group_title in sorted(grouped_channels):
        for channel_info in grouped_channels[group_title]:
            index_content += channel_info

    index_path = os.path.join(output_dir, 'index.m3u')
    with open(index_path, 'w') as f:
        f.write(index_content)

    print(f"Index file created at {index_path}")
