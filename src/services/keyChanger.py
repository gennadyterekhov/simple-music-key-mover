from src.services.noteToScaleConverter import NoteToScaleConverter
from src.services.scaleToNoteConverter import ScaleToNoteConverter
from src.entities.musicalKey import MusicalKey


class KeyChanger:
    def __init__(
        self,
        noteToScaleConverter: NoteToScaleConverter,
        scaleToNoteConverter: ScaleToNoteConverter,
    ):
        self.noteToScaleConverter = noteToScaleConverter
        self.scaleToNoteConverter = scaleToNoteConverter

    def changeKey(self, originalKey: MusicalKey, targetKey: MusicalKey, notes: list) -> list:
        melodyAsSteps = self.noteToScaleConverter.convertMelodyToSteps(
            notes, originalKey)
        melodyInTargetKey = self.scaleToNoteConverter.convertStepsToKey(
            melodyAsSteps, targetKey)

        return melodyInTargetKey
