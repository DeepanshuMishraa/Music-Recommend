from datetime import datetime

class User:
    def __init__(self,user_id,name):
        self.user_id = user_id
        self.name = name
        self.liked_genre = set()
        self.liked_songs = set()
        self.liked_artists = set()
        self.play_history = []

    def like_song(self,song):
        self.liked_genre.add(song.genre)
        self.liked_artists.add(song.artist)
        self.liked_songs.add(song.song_id)

    def play_song(self,song):
        self.play_history.append((song.song_id,datetime.now()))
