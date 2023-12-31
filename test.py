from src.entities.noteName import NoteName
from src.entities.musicalKey import MusicalKey, KeyCMajor
from src.entities.scaleDegree import ScaleDegree
from src.entities.songTransformation import SongTransformation
from src.entities.musicalNote import MusicalNote
from src.services.noteToScaleConverter import NoteToScaleConverter
from src.services.scaleToNoteConverter import ScaleToNoteConverter
from src.services.inputToSongTransformationConverter import InputToSongTransformationConverter
import pytest


class TestInputToSongTransformationConverter:
    def testCannotConvertCompletelyEmptyFile(self):
        with pytest.raises(Exception):
            pathToSongFile = '/Users/gena/code/projects/simple-music-key-mover/storage/input/test/empty.json'

            itstConverter = InputToSongTransformationConverter(pathToSongFile)
            songTransformation = itstConverter.getSongTransformationFromInput()


    def testCanConvertNonSensicalValues(self):
        pathToSongFile = '/Users/gena/code/projects/simple-music-key-mover/storage/input/test/nonsense.json'

        itstConverter = InputToSongTransformationConverter(pathToSongFile)
        songTransformation = itstConverter.getSongTransformationFromInput()
        assert (isinstance(songTransformation, SongTransformation))
        assert (len(songTransformation.song.melody.notes) == 0)
        assert (isinstance(songTransformation.song.melody.key, MusicalKey))
        assert (songTransformation.song.melody.key.noteName == 'lorem ipsum')
        assert (songTransformation.targetKey.noteName == 'howdy pardner')

    def testCanConvertEmptyMelody(self):
        # sorry I dont understand how it works
        # pathToSongFile = '../../storage/input/test/emptyMelody.json'
        pathToSongFile = '/Users/gena/code/projects/simple-music-key-mover/storage/input/test/emptyMelody.json'

        itstConverter = InputToSongTransformationConverter(pathToSongFile)
        songTransformation = itstConverter.getSongTransformationFromInput()
        assert (isinstance(songTransformation, SongTransformation))
        assert (len(songTransformation.song.melody.notes) == 0)
        assert (isinstance(songTransformation.song.melody.key, MusicalKey))
        assert (songTransformation.song.melody.key.noteName == NoteName.FA)
        assert (songTransformation.targetKey.noteName == NoteName.DO)


class TestNoteToScaleConverter:
    def testOneNoteToStep(self):
        ntsConverter = NoteToScaleConverter()
        notes = [MusicalNote(NoteName.DO)]
        originalKey = KeyCMajor()
        melodyAsSteps = ntsConverter.convertMelodyToSteps(notes, originalKey)
        assert (len(melodyAsSteps) == 1)
        assert (isinstance(melodyAsSteps[0], ScaleDegree))
        assert (melodyAsSteps[0].order == 1)

    def testSeveralNotesToSteps(self):
        ntsConverter = NoteToScaleConverter()
        notes = [
            MusicalNote(NoteName.DO),
            MusicalNote(NoteName.DO),
            MusicalNote(NoteName.RE),
            MusicalNote(NoteName.MI),
        ]
        originalKey = KeyCMajor()
        melodyAsSteps = ntsConverter.convertMelodyToSteps(notes, originalKey)
        assert (len(melodyAsSteps) == 4)
        assert (isinstance(melodyAsSteps[0], ScaleDegree))
        assert (melodyAsSteps[0].order == 1)
        assert (melodyAsSteps[1].order == 1)
        assert (melodyAsSteps[2].order == 2)
        assert (melodyAsSteps[3].order == 3)


class TestScaleToNoteConverter:

    def testOneStepToSameNote(self):
        stnConverter = ScaleToNoteConverter()
        originalKey = KeyCMajor()
        targetKey = MusicalKey(NoteName.MI)
        steps = [ScaleDegree(3, originalKey)]
        melodyAsNotes = stnConverter.convertStepsToKey(steps, targetKey)
        assert (len(melodyAsNotes) == 1)
        assert (isinstance(melodyAsNotes[0], MusicalNote))
        assert (melodyAsNotes[0].name == NoteName.SOL)

    def testOneStepToNextNote(self):
        stnConverter = ScaleToNoteConverter()
        originalKey = KeyCMajor()
        targetKey = MusicalKey(NoteName.SOL)

        steps = [ScaleDegree(3, originalKey)]

        melodyAsNotes = stnConverter.convertStepsToKey(steps, targetKey)
        assert (len(melodyAsNotes) == 1)
        assert (isinstance(melodyAsNotes[0], MusicalNote))
        assert (melodyAsNotes[0].name == NoteName.TI)

    def testOneStepToPreviousNote(self):
        stnConverter = ScaleToNoteConverter()
        originalKey = KeyCMajor()
        targetKey = MusicalKey(NoteName.RE)

        steps = [ScaleDegree(3, originalKey)]

        melodyAsNotes = stnConverter.convertStepsToKey(steps, targetKey)
        assert (len(melodyAsNotes) == 1)
        assert (isinstance(melodyAsNotes[0], MusicalNote))
        assert (melodyAsNotes[0].name == NoteName.FA)
