from src.entities.noteName import NoteName

class MusicalNote:
    useScientificNotation = False
    useRussianName = False
    useKalimbaNumber = False
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

        spaceSymbol = ' '
        if self.name == NoteName.PAUSE:
            # because the note will take up one char space regardless of duration, so mst the pause too
            return ' ' + spaces * spaceSymbol
        
        name = self.name
        if self.useRussianName:
            name = NoteName.nameToRussianName[self.name]
        if self.useKalimbaNumber:
            name = NoteName.nameToOrderMap[self.name] + 1

        if self.octave == 1:
            return f'{name} ' + (spaces * spaceSymbol)
        octaveDots = (self.octave-1) * '°' 
        return f'{name}{octaveDots}' + (spaces*spaceSymbol)
