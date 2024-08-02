import re


class Playlist:
    def __init__(self, content=None):
        self.segments = []
        self.nested_playlists = []
        if content:
            self.parse(content)

    def parse(self, content):
        lines = content.splitlines()
        for i in range(len(lines)):
            if lines[i].startswith('#EXTINF'):
                url = lines[i + 1]
                if url.endswith('.m3u') or url.endswith('.m3u8'):
                    self.nested_playlists.append(url)
                else:
                    self.segments.append(url)

    def get_urls(self):
        return self.segments

    def get_nested_playlists(self):
        return self.nested_playlists

    def add_segments(self, urls):
        self.segments = urls

    def to_m3u(self):
        m3u_content = "#EXTM3U\n"
        for url in self.segments:
            m3u_content += f"#EXTINF:-1,{url}\n{url}\n"
        return m3u_content
