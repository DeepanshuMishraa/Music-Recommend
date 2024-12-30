from Recommend import RecommendSong
from Song import Song
from User import User


rec_sys = RecommendSong()

songs =[
    Song(1, "Shape of You", "Ed Sheeran", "Pop", 2017),
    Song(2, "Blinding Lights", "The Weeknd", "Pop", 2020),
    Song(3, "Bohemian Rhapsody", "Queen", "Rock", 1975),
    Song(4, "Stairway to Heaven", "Led Zeppelin", "Rock", 1971),
    Song(5, "Imagine", "John Lennon", "Soft Rock", 1971),
    Song(6, "Levitating", "Dua Lipa", "Pop", 2021),
]
for song in songs:
    rec_sys.add_songs(song)

user = User(1,"ALice")

user.like_song(songs[0])  # Likes "Shape of You"
user.like_song(songs[2])  # Likes "Bohemian Rhapsody"
user.play_song(songs[0])  # Plays "Shape of You"
rec_sys.record_play(songs[0].song_id)
rec_sys.record_play(songs[2].song_id)


print("Genre-based recommendations:")
print(rec_sys.recommend_by_genre(user))

print("\nArtist-based recommendations:")
print(rec_sys.recommend_by_artist(user))

print("\nPopular recommendations:")
print(rec_sys.recommend_popular())
