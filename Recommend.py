
from collections import defaultdict


class RecommendSong:
    def __init__(self):
        self.songs = {}
        self.popularity = defaultdict(int)

    def add_songs(self,song):
        self.songs[song.song_id] =song

    def record_play(self,song_id):
        self.popularity[song_id] +=1

    def recommend_by_genre(self,user,limit=5):
        recommendations = [
            song for song in self.songs.values()
            if song.genre in user.liked_genre and song.song_id not in user.play_history
        ]
        return recommendations[:limit]
    def recommend_by_artist(self, user, limit=5):
        recommendations = [
        song for song in self.songs.values()
        if song.artist in user.liked_artists and song.song_id not in user.play_history
        ]
        return recommendations[:limit]
    def recommend_popular(self, limit=5):
        sorted_songs = sorted(
        self.songs.values(),
        key=lambda song: self.popularity[song.song_id],
        reverse=True
        )
        return sorted_songs[:limit]
