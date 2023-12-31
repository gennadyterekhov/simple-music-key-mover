from src.entities.noteName import NoteName
from src.entities.musicalKey import MusicalKey
from src.entities.musicalNote import MusicalNote
from src.entities.scaleDegree import ScaleDegree


class ScaleToNoteConverter:
    def convertStepsToKey(self, melodyAsSteps: list, targetKey: MusicalKey) -> list:
        melody = []
        note = None
        for st in melodyAsSteps:
            note = self.convertStepToNote(st, targetKey)
            melody.append(note)
        return melody

    def convertStepToNote(self, step: ScaleDegree, targetKey: MusicalKey) -> MusicalNote:
        targetKeyOffset = NoteName.nameToOrderMap[targetKey.noteName]
        # -1 because step.order is natural step number, not index
        noteName = NoteName.order[targetKeyOffset + step.order - 1 % 7]
        if step.order == -1:
            noteName = NoteName.PAUSE
        return MusicalNote(noteName, duration=step.duration, octave=step.octave)
