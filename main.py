from src.entities.musicalKey import MusicalKey, KeyCMajor, KeyFMajor
from src.entities.musicalNote import MusicalNote
from src.services.noteToScaleConverter import NoteToScaleConverter
from src.services.scaleToNoteConverter import ScaleToNoteConverter


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
