from src.entities.musicalKey import MusicalKey
from src.entities.song import Song


class SongTransformation:
    def __init__(self, song: Song, targetKey: MusicalKey):
        self.song = song
        self.targetKey = targetKey
