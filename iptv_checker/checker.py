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
        urls_to_check = await self.get_all_urls(playlist)
        tasks = []
        async with aiohttp.ClientSession() as session:
            for url in urls_to_check:
                tasks.append(check_channel(session, url))
            results = await asyncio.gather(*tasks)
        self.available_channels = [url for url in results if url]

    async def get_all_urls(self, playlist):
        all_urls = playlist.get_urls()
        nested_playlists = playlist.get_nested_playlists()
        for nested_playlist_url in nested_playlists:
            nested_content = await download_playlist(nested_playlist_url)
            nested_playlist = Playlist(nested_content)
            all_urls.extend(await self.get_all_urls(nested_playlist))
        return all_urls

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
