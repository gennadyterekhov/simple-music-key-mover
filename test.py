from main import NoteToScaleConverter, KeyCMajor, MusicalNote, NoteName, ScaleDegree, ScaleToNoteConverter, MusicalKey


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
