from src.entities.tempo import Tempo
from src.entities.melody import Melody


class Song:
    def __init__(self, melody: Melody, tempo: Tempo):
        self.melody = melody
        self.tempo = tempo
