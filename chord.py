class Chord:
    def __init__(self):
        self.chromatic_scale = [
            "C", "C#", "D", "D#", "E", "F",
            "F#", "G", "G#", "A", "A#", "B"
        ]

        # Flats → sharps
        self.enharmonic_map = {
            "Db": "C#", "Eb": "D#", "Gb": "F#",
            "Ab": "G#", "Bb": "A#"
        }

        # Sharps → flats
        self.reverse_map = {v: k for k, v in self.enharmonic_map.items()}

        # Interval names
        self.interval_names = {
            0: "T", 1: "2m", 2: "2M", 3: "3m", 4: "3M",
            5: "4J", 6: "5º", 7: "5J",
            8: "6m", 9: "6M", 10: "7m", 11: "7M"
        }

        # Degrees
        self.degrees = {
            0: "I", 1: "II", 2: "II", 3: "III", 4: "III",
            5: "IV", 6: "V", 7: "V",
            8: "VI", 9: "VI", 10: "VII", 11: "VII"
        }

        # Chord formulas (intervals)
        self.chords = {
            "5": [0, 7],
            "maj": [0, 4, 7],#
            "m": [0, 3, 7],#
            "dim": [0, 3, 6],
            "aug": [0, 4, 8],
            "sus2": [0, 2, 7],
            "sus4": [0, 5, 7],
            "7": [0, 4, 7, 10],#
            "maj7": [0, 4, 7, 11],
            "m7": [0, 3, 7, 10],
            "6": [0, 4, 7, 9],
            "m6": [0, 3, 7, 9],
            "9": [0, 4, 7, 10, 2],
            "m9": [0, 3, 7, 10, 2],
        }

    def normalize(self, note):
        return self.enharmonic_map.get(note, note)

    def format(self, note, prefer_flats):
        if prefer_flats:
            return self.reverse_map.get(note, note)
        return note

    # -------- CORE --------
    def get_chord(self, root, chord_type):
        prefer_flats = "b" in root
        root = self.normalize(root)

        if root not in self.chromatic_scale:
            raise ValueError("Invalid root")

        if chord_type not in self.chords:
            raise ValueError("Chord not supported")

        root_index = self.chromatic_scale.index(root)
        intervals = self.chords[chord_type]

        notes = []
        indexes = []
        interval_names = []
        degrees = []

        for i in intervals:
            idx = (root_index + i) % 12
            note = self.chromatic_scale[idx]

            notes.append(self.format(note, prefer_flats))
            indexes.append(idx)
            interval_names.append(self.interval_names[i])
            degrees.append(self.degrees[i])

        return {
            "name": f"{root}{chord_type}",
            "notes": notes,
            "indexes": indexes,
            "intervals": intervals,
            "interval_names": interval_names,
            "degrees": degrees,
            "count": len(notes)
        }

    # -------- PRINT --------
    def print_chord(self, root, chord_type):
        data = self.get_chord(root, chord_type)

        print(f"Chord: {data['name']}")
        print(f"Notes: {' - '.join(data['notes'])}")
        print(f"Indexes: {data['indexes']}")
        print(f"Intervals: {data['intervals']}")
        print(f"Interval Names: {data['interval_names']}")
        print(f"Degrees: {data['degrees']}")
        print(f"Number of notes: {data['count']}")

    # -------- PARSER --------
    def parse_chord(self, chord_str):
        chord_str = chord_str.strip()

        if len(chord_str) == 0:
            raise ValueError("Empty chord")

        # Step 1: extract root
        root = chord_str[0]

        if len(chord_str) > 1 and chord_str[1] in ["#", "b"]:
            root += chord_str[1]
            suffix = chord_str[2:]
        else:
            suffix = chord_str[1:]

        # Step 2: normalize suffix
        if suffix == "":
            suffix = "maj"   # default (C = C major)

        # Normalize aliases
        suffix_map = {
            "M": "maj",
            "major": "maj",
            "min": "m",
            "-": "m",
            "minor": "m",
            "Δ": "maj7",
            "maj7": "maj7",
            "M7": "maj7",
        }

        suffix = suffix_map.get(suffix, suffix)

        # Step 3: validate
        if suffix not in self.chords:
            raise ValueError(f"Chord type not supported: {suffix}")

        return root, suffix
    def get_chord_from_string(self, chord_str):
        root, chord_type = self.parse_chord(chord_str)
        return self.get_chord(root, chord_type)

    def print_chord_from_string(self, chord_str):
        root, chord_type = self.parse_chord(chord_str)
        self.print_chord(root, chord_type)


c = Chord()
 

c.print_chord("C", "maj")

c.print_chord_from_string("Cmaj7")
