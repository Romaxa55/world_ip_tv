import aiohttp


async def download_playlist(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def check_channel(session, url):
    try:
        async with session.get(url, timeout=5) as response:
            return url if response.status == 200 else None
    except:
        return None
