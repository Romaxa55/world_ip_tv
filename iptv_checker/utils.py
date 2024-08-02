import asyncio

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
