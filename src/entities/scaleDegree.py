from src.entities.musicalKey import MusicalKey

class ScaleDegree:
    def __init__(self, order: int, key: MusicalKey, duration=0.25, octave=1):
        self.order = order
        self.key = key
        self.duration = duration
        self.octave = octave
