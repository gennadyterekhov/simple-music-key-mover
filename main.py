from src.services.inputToSongTransformationConverter import InputToSongTransformationConverter
from src.services.keyChanger import KeyChanger
from src.services.noteToScaleConverter import NoteToScaleConverter
from src.services.scaleToNoteConverter import ScaleToNoteConverter
from src.services.arranger import Arranger


def getArranger():
    jingleBells = '/Users/gena/code/projects/simple-music-key-mover/storage/input/examples/jingleBells.json'
    inputToSongTransformationConverter = InputToSongTransformationConverter(jingleBells)
    noteToScaleConverter = NoteToScaleConverter()
    scaleToNoteConverter = ScaleToNoteConverter()
    keyChanger = KeyChanger(noteToScaleConverter, scaleToNoteConverter)
    arranger = Arranger(inputToSongTransformationConverter, keyChanger)
    return arranger


def main():
    arranger = getArranger()
    arranger.arrange()


if __name__ == '__main__':
    main()
