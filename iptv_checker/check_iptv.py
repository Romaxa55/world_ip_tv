import asyncio
from .checker import IPTVChecker

if __name__ == "__main__":
    checker = IPTVChecker("https://iptv-org.github.io/iptv/index.country.m3u")
    asyncio.run(checker.run())
