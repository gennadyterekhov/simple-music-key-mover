from src.services.inputToSongTransformationConverter import InputToSongTransformationConverter
from src.services.keyChanger import KeyChanger
from src.entities.musicalKey import KeyCMajor, KeyFMajor
from src.entities.musicalNote import MusicalNote
from src.entities.tempo import Tempo


class Arranger:

    def __init__(
        self,
        inputToSong: InputToSongTransformationConverter,
        changer: KeyChanger,
    ):
        self.inputToSong = inputToSong
        self.changer = changer

    def arrange(self):
        songTransformation = self.inputToSong.getSongTransformationFromInput()

        notes = songTransformation.song.melody.notes
        tempo = songTransformation.song.tempo
        self.outputResultNotes(notes, tempo)

        originalKey = KeyFMajor()
        targetKey = KeyCMajor()

        targetKeyNotes = self.changer.changeKey(originalKey, targetKey, notes)

        self.outputResultNotes(targetKeyNotes, tempo)

    def outputResultNotes(self, notes: list, tempo: Tempo):
        currentBarDuration = 0
        barsOnCurrentLine = 0
        fullBarDuration = tempo.number * tempo.duration
        for n in (notes):
            self.printNote(n)
            currentBarDuration += n.duration
            if currentBarDuration == fullBarDuration:
                print('    |    ', end='')
                currentBarDuration = 0
                barsOnCurrentLine += 1
            if barsOnCurrentLine == tempo.barsPerLine:
                barsOnCurrentLine = 0
                print()
                print()
        print()

    def printNote(self, note: MusicalNote):
        print(note, end='')
