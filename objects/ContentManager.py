class ContentManager(object):

    def __init__(self, streamer):
        self.streamer = streamer
        self.songs = []
        self.radios = []
        self.search_results =[]
        self.title = ''
        self.subtitle = ''
        self.search_menu = False

    def load(self):
        self.songs = self.streamer.client.get_all_songs()
        self.radios = self.streamer.client.get_all_stations()

    def search_songs(self,artist="",album="",song=""):
        search_results = [s for s in self.songs if (album in s['album'] and artist in s['artist'] and song in s['title'])]
        if len(search_results) > 0:
            self.title = artist+album+song
            self.subtitle = "Search Results"
            self.search_menu = True
            self.search_results = search_results
