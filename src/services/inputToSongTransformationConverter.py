from src.entities.songTransformation import SongTransformation
from src.entities.song import Song
from src.entities.musicalKey import MusicalKey
from src.entities.musicalNote import MusicalNote
from src.entities.tempo import Tempo
from src.entities.melody import Melody
import json


class InputToSongTransformationConverter:

    # public

    def __init__(self, pathToSongFile: str = '/Users/gena/code/projects/simple-music-key-mover/storage/input/song.json') -> None:
        self.pathToSongFile = pathToSongFile

    def getSongTransformationFromInput(self) -> SongTransformation:
        data = self.getInputFileData()
        return self.getSongTransformationFromDict(data)

    # private

    def getSongTransformationFromDict(self, data: dict) -> SongTransformation:
        song = self.getSongFromDict(data)
        targetKey = self.getTargetKeyFromDict(data)
        return SongTransformation(song=song, targetKey=targetKey)

    def getSongFromDict(self, data: dict) -> Song:
        return Song(
            melody=self.getMelodyFromDict(data),
            tempo=self.getTempoFromDict(data),
        )

    def getMelodyFromDict(self, data: dict) -> Melody:
        return Melody(
            notes=self.getNotesFromDict(data),
            key=self.getMelodyKeyFromDict(data),
        )

    def getNotesFromDict(self, data: dict) -> list:
        notes = []
        for note in data['song']['melody']['notes']:
            notes.append(MusicalNote(
                note['name'],
                note['duration'],
                note['octave'],
            ))
        return notes

    def getMelodyKeyFromDict(self, data: dict) -> MusicalKey:
        return MusicalKey(
            data['song']['melody']['key']['noteName'],
            data['song']['melody']['key']['isMajor'],
            data['song']['melody']['key']['isFlat'],
            data['song']['melody']['key']['isSharp'],
        )

    def getTempoFromDict(self, data: dict) -> Tempo:
        return Tempo(
            data['song']['tempo']['number'],
            data['song']['tempo']['duration'],
            data['song']['tempo']['barsPerLine'],
        )

    def getTargetKeyFromDict(self, data: dict) -> MusicalKey:
        return MusicalKey(
            data['targetKey']['noteName'],
            data['targetKey']['isMajor'],
            data['targetKey']['isFlat'],
            data['targetKey']['isSharp'],
        )

    def getInputFileData(self) -> dict:
        return json.loads(self.getInputFileContents())

    def getInputFileContents(self) -> str:
        file = open(self.pathToSongFile)
        contents = file.read()
        file.close()
        return contents
