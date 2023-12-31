from src.entities.noteName import NoteName
from src.entities.musicalKey import MusicalKey
from src.entities.musicalNote import MusicalNote
from src.entities.scaleDegree import ScaleDegree

class NoteToScaleConverter:
    def convertMelodyToSteps(self, notes: list, originalKey: MusicalKey) -> list:
        steps = []
        step = None
        for n in notes:
            step = self.convertNoteToStep(n, originalKey)
            steps.append(step)
        return steps

    def convertNoteToStep(self, note: MusicalNote, originalKey: MusicalKey) -> ScaleDegree:
        if note.name == NoteName.PAUSE:
            return ScaleDegree(-1, key=originalKey, duration=note.duration, octave=note.octave)

        orderInCMajor = NoteName.nameToOrderMap[note.name]
        differenceWithCMajor = NoteName.nameToOrderMap[originalKey.noteName]

        order = (orderInCMajor - differenceWithCMajor + 7) % 7

        octave = note.octave + (orderInCMajor - differenceWithCMajor + 7) // 7
        # +1 because we were dealing with indices before
        return ScaleDegree(order + 1, key=originalKey, duration=note.duration, octave=octave)
