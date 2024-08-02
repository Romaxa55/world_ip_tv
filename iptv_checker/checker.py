import aiohttp
import asyncio
from .playlist import Playlist
from .utils import download_playlist, check_channel

class IPTVChecker:
    def __init__(self, playlist_url):
        self.playlist_url = playlist_url
        self.available_channels = []

    async def check_channels(self, playlist_content):
        playlist = Playlist(playlist_content)
        tasks = []
        async with aiohttp.ClientSession() as session:
            for url in playlist.get_segment_urls():
                tasks.append(check_channel(session, url))
            results = await asyncio.gather(*tasks)
        self.available_channels = [url for url in results if url]

    def create_new_playlist(self):
        playlist = Playlist()
        playlist.add_segments(self.available_channels)
        return playlist.to_m3u()

    async def run(self):
        playlist_content = await download_playlist(self.playlist_url)
        await self.check_channels(playlist_content)
        new_playlist_content = self.create_new_playlist()
        with open('available_channels.m3u', 'w') as f:
            f.write(new_playlist_content)
