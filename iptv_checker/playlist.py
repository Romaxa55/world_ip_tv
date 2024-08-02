import re

class Playlist:
    def __init__(self, content=None):
        self.channels = []
        if content:
            self.parse(content)

    def parse(self, content):
        lines = content.splitlines()
        for i in range(len(lines)):
            if lines[i].startswith('#EXTINF'):
                match = re.match(r'#EXTINF:-1.*tvg-logo="(?P<logo>[^"]+)".*,(?P<name>.+)', lines[i])
                if match:
                    channel = {
                        "name": match.group("name"),
                        "logo": match.group("logo"),
                        "url": lines[i + 1]
                    }
                    self.channels.append(channel)

    def get_urls(self):
        return [channel["url"] for channel in self.channels]

    def get_channels(self):
        return self.channels

    def add_channels(self, channels):
        self.channels.extend(channels)

    def to_m3u(self, group_title=None):
        m3u_content = "#EXTM3U\n"
        for channel in self.channels:
            group = f' group-title="{group_title}"' if group_title else ""
            m3u_content += f'#EXTINF:-1 tvg-logo="{channel["logo"]}"{group},{channel["name"]}\n{channel["url"]}\n'
        return m3u_content
