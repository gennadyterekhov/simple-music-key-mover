class MusicalKey:
    def __init__(self, noteName: str, isMajor=True, isFlat=False, isSharp=False):
        self.noteName = noteName
        self.isMajor = isMajor
        self.isFlat = isFlat
        self.isSharp = isSharp



class KeyCMajor (MusicalKey):
    def __init__(self):
        super().__init__('C', isMajor=True)


class KeyFMajor (MusicalKey):
    def __init__(self):
        super().__init__('F', isMajor=True)

