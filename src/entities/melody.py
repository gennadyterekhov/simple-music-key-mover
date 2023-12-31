from src.entities.musicalKey import MusicalKey


class Melody:
    def __init__(self, notes: list, key: MusicalKey):
        self.notes = notes
        self.key = key
