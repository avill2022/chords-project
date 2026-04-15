class Scale:
    def __init__(self):
        self.chromatic_scale = [
            "C", "C#", "D", "D#", "E", "F",
            "F#", "G", "G#", "A", "A#", "B"
        ]

        self.enharmonic_map = {
            "Db": "C#",
            "Eb": "D#",
            "Gb": "F#",
            "Ab": "G#",
            "Bb": "A#"
        }

        self.reverse_enharmonic_map = {v: k for k, v in self.enharmonic_map.items()}

        self.scales = {
            "major": [0, 2, 4, 5, 7, 9, 11],
            "minor": [0, 2, 3, 5, 7, 8, 10],
        }

    def normalize_note(self, note):
        return self.enharmonic_map.get(note, note)

    def format_note(self, note, prefer_flats=False):
        if prefer_flats:
            return self.reverse_enharmonic_map.get(note, note)
        return note

    # -------- NOTES --------
    def get_scale_array(self, root, scale_type):
        prefer_flats = "b" in root
        normalized_root = self.normalize_note(root)

        if normalized_root not in self.chromatic_scale:
            raise ValueError(f"Invalid root note: {root}")

        root_index = self.chromatic_scale.index(normalized_root)
        intervals = self.scales[scale_type]

        result = []
        for step in intervals:
            note_index = (root_index + step) % 12
            note = self.chromatic_scale[note_index]
            note = self.format_note(note, prefer_flats)
            result.append(note)

        return result

    # -------- RELATIVE INDEXES --------
    def get_scale_intervals(self, scale_type):
        return self.scales[scale_type]

    # -------- ABSOLUTE INDEXES --------
    def get_scale_indexes(self, root, scale_type):
        normalized_root = self.normalize_note(root)

        if normalized_root not in self.chromatic_scale:
            raise ValueError(f"Invalid root note: {root}")

        root_index = self.chromatic_scale.index(normalized_root)
        intervals = self.scales[scale_type]

        return [(root_index + step) % 12 for step in intervals]

    # -------- PRINT METHODS --------
    def print_scale(self, root, scale_type):
        notes = self.get_scale_array(root, scale_type)
        print(f"{root} {scale_type} scale: {' - '.join(notes)}")

    def print_scale_indexes(self, root, scale_type):
        indexes = self.get_scale_indexes(root, scale_type)
        print(f"{root} {scale_type} indexes: {indexes}")

    def print_scale_full(self, root, scale_type):
        notes = self.get_scale_array(root, scale_type)
        indexes = self.get_scale_indexes(root, scale_type)
        intervals = self.get_scale_intervals(scale_type)

        print(f"{root} {scale_type} scale:")
        print(f"Notes:    {' - '.join(notes)}")
        print(f"Indexes:  {indexes}")
        print(f"Steps:    {intervals}")


##
s = Scale()

# Only notes
s.print_scale("Db", "major")

# Absolute indexes
s.print_scale_indexes("Db", "major")
# Example: [1, 3, 5, 6, 8, 10, 0]

# Full info
s.print_scale_full("Eb", "minor")
