from chord_repo import CHROMATIC_SCALE, VARIATIONS, figures, note_index

ENHARMONIC = {
    "Db": "C#", "Eb": "D#", "Gb": "F#", "Ab": "G#", "Bb": "A#"
}

SUFFIX_MAP = {
    '': 'major',
    'm': 'minor',
    'minor': 'minor',
    '7': 'major7',
    'dom7': 'major7',
    'maj7': 'cmaj7',
    'M7': 'cmaj7',
    'm7': 'cm7',
    'dim': 'cdim',
    'aug': 'caug',
    '+': 'caug',
    'sus2': 'csus2',
    'sus4': 'csus4',
    '6': 'c6',
    'm6': 'cm6',
    '9': 'c9',
    'm9': 'cm9',
    '5': 'c5',
    'power': 'c5',
}

ZERO_MATRIX = [[0, 0, 0, 0, 0, 0, 0]]


class ChordFinder:
    def __init__(self):
        self.scale = CHROMATIC_SCALE
        self.variations = VARIATIONS
        self.enharmonic = ENHARMONIC
        self.suffix_map = SUFFIX_MAP

    def parse(self, chord_str: str):
        chord_str = chord_str.strip()
        if not chord_str:
            return None, None

        root = chord_str[0].upper()
        if len(chord_str) > 1 and chord_str[1] in '#b':
            root += chord_str[1]
            suffix = chord_str[2:]
        else:
            suffix = chord_str[1:]

        root = self.enharmonic.get(root, root)

        if root not in self.scale:
            return None, None

        variation = self.suffix_map.get(suffix)
        if variation is None:
            return None, None

        return root, variation

    def find(self, chord_str: str):
        root, variation = self.parse(chord_str)
        if root is None:
            return figures([row[:] for row in ZERO_MATRIX])

        template = [row[:] for row in self.variations[variation]]
        f = figures(template)
        n = note_index(root)
        f.add(n)
        f.normaizate()
        f.organize()
        f.p_normailzation()
        return f

    def show(self, chord_str: str):
        f = self.find(chord_str)
        f.show_chords_()
        f.show()

    def get_matrix(self, chord_str: str):
        f = self.find(chord_str)
        return f.matriz


if __name__ == '__main__':
    import sys
    finder = ChordFinder()
    for arg in sys.argv[1:]:
        print(f"\n=== {arg} ===")
        finder.show(arg)
