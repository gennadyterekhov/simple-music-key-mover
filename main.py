import math


class NoteName:
    PAUSE = 'Pause'
    DO = 'C'
    RE = 'D'
    MI = 'E'
    FA = 'F'
    SOL = 'G'
    LA = 'A'
    TI = 'B'
    order = [
        DO,
        RE,
        MI,
        FA,
        SOL,
        LA,
        TI,
    ]
    # C maj
    nameToOrderMap = {
        DO: 0,
        RE: 1,
        MI: 2,
        FA: 3,
        SOL: 4,
        LA: 5,
        TI: 6,
    }
    nameToRussianName = {
        DO: "До",
        RE: "Ре",
        MI: "Ми",
        FA: "Фа",
        SOL: "Соль",
        LA: "Ля",
        TI: "Си",
    }


class MusicalKey:
    def __init__(self, noteName: str, isMajor=True, isFlat=False, isSharp=False):
        self.noteName = noteName
        self.isMajor = isMajor
        self.isFlat = isFlat
        self.isSharp = isSharp


class MusicalNote:
    useScientificNotation = False
    scientificPitchNotationOffset = 3

    def __init__(self, name: str, duration=0.25, octave=1):
        self.name = name
        self.duration = duration
        self.octave = octave

    def __repr__(self) -> str:
        if self.useScientificNotation:
            return f'{self.name}{self.octave + self.scientificPitchNotationOffset}'
        # this is bad
        # hardcoded for jingle bells
        if self.duration < 0.25:
            spaces = 0
        if self.duration == 0.25:
            spaces = 1
        if self.duration > 0.25:
            spaces = 2
        if self.duration >= 0.5:
            spaces = 3

        spaceSymbol = '_'
        if self.name == NoteName.PAUSE:
            # because the note will take up one char space regardless of duration, so mst the pause too
            return '_' + spaces * spaceSymbol
        # nm = NoteName.nameToRussianName[self.name]
        nm = self.name
        return f'{nm}' + (spaces * spaceSymbol)

        if self.octave == 1:
            return f'{nm}' + (spaces * spaceSymbol)
        return f'{nm}{self.octave}' + (spaces*spaceSymbol)


class ScaleDegree:
    def __init__(self, order: int, key: MusicalKey, duration=0.25, octave=1):
        self.order = order
        self.key = key
        self.duration = duration
        self.octave = octave


config = {
    "tempo": {"number": 4, "duration": 0.25, "barsPerLine": 4},
    "notes": [
        # 1st line
        MusicalNote('C'),
        MusicalNote('A'),
        MusicalNote('G'),
        MusicalNote('F'),

        MusicalNote('C', 0.5),
        MusicalNote('Pause'),
        MusicalNote('C', 0.125),
        MusicalNote('C', 0.125),

        MusicalNote('C'),
        MusicalNote('A'),
        MusicalNote('G'),
        MusicalNote('F'),

        MusicalNote('D', 0.5),
        MusicalNote('Pause', 0.5),

        # 2nd line
        MusicalNote('D'),
        MusicalNote('B'),
        MusicalNote('A'),
        MusicalNote('G'),

        MusicalNote('E', 0.5),
        MusicalNote('Pause', 0.5),

        MusicalNote('C', octave=2),
        MusicalNote('C', octave=2),
        MusicalNote('B'),
        MusicalNote('G'),

        MusicalNote('A', 0.5),
        MusicalNote('Pause', 0.5),


        # 3rd line, almost the same as the 1st
        MusicalNote('C'),
        MusicalNote('A'),
        MusicalNote('G'),
        MusicalNote('F'),

        MusicalNote('C', 0.5),
        MusicalNote('Pause'),
        MusicalNote('C', 0.125),
        MusicalNote('C', 0.125),

        MusicalNote('C'),
        MusicalNote('A'),
        MusicalNote('G'),
        MusicalNote('F'),

        MusicalNote('D', 0.5),
        MusicalNote('Pause', 0.25),
        MusicalNote('D', 0.25),

        # 4th line, looks like the 2nd
        MusicalNote('D'),
        MusicalNote('B'),
        MusicalNote('A'),
        MusicalNote('G'),

        MusicalNote('C', octave=2),
        MusicalNote('C', octave=2),
        MusicalNote('C', octave=2),
        MusicalNote('C', octave=2),

        MusicalNote('D', octave=2),
        MusicalNote('C', octave=2),
        MusicalNote('B'),
        MusicalNote('G'),

        MusicalNote('F', 0.5),
        MusicalNote('Pause', 0.5),


        # main melody 1 line
        MusicalNote('A'),
        MusicalNote('A'),
        MusicalNote('A', 0.5),

        MusicalNote('A'),
        MusicalNote('A'),
        MusicalNote('A', 0.5),

        MusicalNote('A'),
        MusicalNote('C', octave=2),
        MusicalNote('F', ),
        MusicalNote('G'),

        MusicalNote('A', 0.5),
        MusicalNote('Pause', 0.5),

        # main melody 2 line
        MusicalNote('B'),
        MusicalNote('B'),
        MusicalNote('B'),
        MusicalNote('B'),

        MusicalNote('B'),
        MusicalNote('A'),
        MusicalNote('A'),
        MusicalNote('A', 0.125),
        MusicalNote('A', 0.125),

        MusicalNote('A'),
        MusicalNote('G'),
        MusicalNote('G'),
        MusicalNote('A'),

        MusicalNote('G', 0.5),
        MusicalNote('C', 0.5),


        # main melody 3 line
        MusicalNote('B'),
        MusicalNote('B'),
        MusicalNote('B'),
        MusicalNote('B'),

        MusicalNote('B'),
        MusicalNote('A'),
        MusicalNote('A'),
        MusicalNote('A', 0.125),
        MusicalNote('A', 0.125),

        MusicalNote('C', octave=2),
        MusicalNote('C', octave=2),
        MusicalNote('B'),
        MusicalNote('G'),

        MusicalNote('F', 0.5),
        MusicalNote('Pause', 0.5),
    ]
}


diContainer = {
    'services': {

    },
}


class KeyCMajor (MusicalKey):
    def __init__(self):
        super().__init__('C', isMajor=True)


class KeyFMajor (MusicalKey):
    def __init__(self):
        super().__init__('F', isMajor=True)


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

        # +1 because we were dealing with indices before
        return ScaleDegree(order + 1, key=originalKey, duration=note.duration, octave=note.octave)


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


def changeKey(originalKey: MusicalKey, targetKey: MusicalKey, notes: list) -> list:
    melodyAsSteps = diContainer['services']['NoteToScaleConverter'].convertMelodyToSteps(
        notes, originalKey)
    melodyInTargetKey = diContainer['services']['ScaleToNoteConverter'].convertStepsToKey(
        melodyAsSteps, targetKey)

    return melodyInTargetKey


def arrange():
    notes = config['notes']
    tempo = config['tempo']
    outputResultNotes(notes, tempo)

    originalKey = KeyFMajor()
    targetKey = KeyCMajor()

    targetKeyNotes = changeKey(originalKey, targetKey, notes)

    outputResultNotes(targetKeyNotes, tempo)


def outputResultNotes(notes: list, tempo: dict):
    currentBarDuration = 0
    barsOnCurrentLine = 0
    fullBarDuration = tempo['number'] * tempo['duration']
    for n in (notes):
        printNote(n)
        currentBarDuration += n.duration
        if currentBarDuration == fullBarDuration:
            print('    |    ', end='')
            currentBarDuration = 0
            barsOnCurrentLine += 1
        if barsOnCurrentLine == tempo['barsPerLine']:
            barsOnCurrentLine = 0
            print()
    print()


def printNote(note: MusicalNote):
    print(note, end='')


def setUpDiContainer():
    global diContainer
    diContainer['services']['NoteToScaleConverter'] = NoteToScaleConverter()
    diContainer['services']['ScaleToNoteConverter'] = ScaleToNoteConverter()


def main():
    setUpDiContainer()
    arrange()


if __name__ == '__main__':
    main()
