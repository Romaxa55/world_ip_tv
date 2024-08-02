import aiohttp
import asyncio
import logging
import os
import m3u8
from .playlist import Playlist
from .utils import download_playlist

# Настройка логгера
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class IPTVChecker:
    def __init__(self, country_name, playlist_url, semaphore):
        self.country_name = country_name
        self.playlist_url = playlist_url
        self.available_channels = []
        self.semaphore = semaphore

    async def check_channels(self, playlist_content):
        playlist = Playlist(playlist_content)
        channels_to_check = playlist.get_channels()
        tasks = []
        async with aiohttp.ClientSession() as session:
            for i, channel in enumerate(channels_to_check):
                tasks.append(self.check_channel(session, channel))
                if (i + 1) % 10 == 0 or i + 1 == len(channels_to_check):
                    logger.info(f"Parsed {i + 1} channels, {len(channels_to_check) - (i + 1)} remaining.")
            results = await asyncio.gather(*tasks)
        self.available_channels = [channel for channel in results if channel]
        logger.info(f"Checked {len(channels_to_check)} channels, {len(self.available_channels)} are available.")

    async def check_channel(self, session, channel):
        async with self.semaphore:
            url = channel["url"]
            try:
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        # Проверка плейлиста
                        playlist_content = await response.text()
                        m3u_playlist = m3u8.loads(playlist_content, uri=url)
                        if m3u_playlist.segments:
                            # Если есть сегменты, проверяем первый сегмент
                            segment_url = m3u_playlist.segments[0].absolute_uri
                            if await self.check_segment(session, segment_url):
                                logger.info(f"Channel {channel['name']} ({url}) is available with segments.")
                                return channel
                            else:
                                logger.warning(f"Channel {channel['name']} ({url}) has no working segments.")
                                return None
                        elif m3u_playlist.playlists:
                            # Если есть вложенные плейлисты, проверяем их
                            for p in m3u_playlist.playlists:
                                nested_playlist_url = p.absolute_uri
                                if await self.check_playlist(session, nested_playlist_url):
                                    logger.info(f"Channel {channel['name']} ({url}) is available with nested playlists.")
                                    return channel
                            logger.warning(f"Channel {channel['name']} ({url}) has no working nested playlists.")
                            return None
                        else:
                            # Если это прямой поток без сегментов
                            logger.info(f"Channel {channel['name']} ({url}) is a direct stream.")
                            return channel
                    else:
                        logger.warning(f"Channel {channel['name']} ({url}) is not available. Status code: {response.status}")
                        return None
            except Exception as e:
                logger.error(f"Error checking channel {channel['name']} ({url}): {e}")
                return None

    async def check_segment(self, session, segment_url):
        try:
            async with session.get(segment_url, timeout=10) as response:
                if response.status == 200:
                    return True
                else:
                    logger.warning(f"Segment {segment_url} is not available. Status code: {response.status}")
                    return False
        except Exception as e:
            logger.error(f"Error checking segment {segment_url}: {e}")
            return False

    async def check_playlist(self, session, playlist_url):
        try:
            async with session.get(playlist_url, timeout=10) as response:
                if response.status == 200:
                    return True
                else:
                    logger.warning(f"Nested playlist {playlist_url} is not available. Status code: {response.status}")
                    return False
        except Exception as e:
            logger.error(f"Error checking nested playlist {playlist_url}: {e}")
            return False

    def create_new_playlist(self):
        playlist = Playlist()
        playlist.add_channels(self.available_channels)
        logger.info(f"Total available channels to save: {len(self.available_channels)}")
        return playlist.to_m3u(group_title=self.country_name)

    async def run(self):
        logger.info(f"Starting to check playlist from {self.playlist_url}")
        playlist_content = await download_playlist(self.playlist_url)
        await self.check_channels(playlist_content)

        if not self.available_channels:
            logger.info("No available channels, skipping save.")
            return

        new_playlist_content = self.create_new_playlist()

        # Определение пути для сохранения файла на уровень выше
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(current_dir, '..', 'output')
        os.makedirs(output_dir, exist_ok=True)
        filename = os.path.basename(self.playlist_url)
        output_path = os.path.join(output_dir, filename)

        with open(output_path, 'w') as f:
            f.write(new_playlist_content)
        logger.info(f"New playlist with available channels has been created at {output_path}.")
