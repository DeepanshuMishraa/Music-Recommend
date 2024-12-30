class Song:
    def __init__(self,song_id,title,artist,genre,released):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.genre = genre
        self.released = released

    def __repr__(self):
        return f"{self.title} by {self.artist} of genre {self.genre} released in {self.released} with id {self.song_id}"
