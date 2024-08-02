import m3u8

class Playlist:
    def __init__(self, content=None):
        self.playlist = m3u8.loads(content) if content else m3u8.M3U8()

    def get_segment_urls(self):
        return [segment.uri for segment in self.playlist.segments]

    def add_segments(self, urls):
        for url in urls:
            self.playlist.add_segment(m3u8.Segment(uri=url))

    def to_m3u(self):
        return self.playlist.dumps()
