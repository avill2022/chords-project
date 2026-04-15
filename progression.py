class Progression:
    def __init__(self, scale_obj, chord_obj):
        self.scale = scale_obj
        self.chord = chord_obj

        self.degrees = ["I", "II", "III", "IV", "V", "VI", "VII"]

        # Harmonization rules
        self.harmonizations = {
            "major": ["maj", "m", "m", "maj", "maj", "m", "dim"],
            "minor": ["m", "dim", "maj", "m", "m", "maj", "maj"]
        }

        # Common progressions
        self.common_progressions = {
            "I-IV-V": ["I", "IV", "V"],
            "I-V-vi-IV": ["I", "V", "VI", "IV"],
            "ii-V-I": ["II", "V", "I"],
            "vi-IV-I-V": ["VI", "IV", "I", "V"]
        }

    # -------- BASE --------
    def get_progression(self, root, scale_type):
        scale_notes = self.scale.get_scale_array(root, scale_type)
        chord_types = self.harmonizations[scale_type]

        result = []

        for i in range(7):
            chord_data = self.chord.get_chord(scale_notes[i], chord_types[i])

            result.append({
                "degree": self.degrees[i],
                "root": scale_notes[i],
                "type": chord_types[i],
                "name": chord_data["name"],
                "notes": chord_data["notes"]
            })

        return result

    # -------- DEGREE SELECTION --------
    def get_by_degrees(self, root, scale_type, degree_list):
        full = self.get_progression(root, scale_type)
        degree_map = {c["degree"]: c for c in full}

        return [degree_map[d] for d in degree_list]

    # -------- COMMON --------
    def get_common(self, root, scale_type, name):
        pattern = self.common_progressions[name]
        return self.get_by_degrees(root, scale_type, pattern)

    # -------- ROMAN PARSER --------
    def parse_roman(self, progression_str):
        tokens = progression_str.replace("-", " ").split()

        result = []
        for t in tokens:
            t = t.strip()

            # Detect minor (lowercase)
            if t.islower():
                degree = t.upper()
                quality = "m"
            else:
                degree = t.upper()
                quality = None  # will use harmonization

            result.append((degree, quality))

        return result

    def get_from_roman(self, root, scale_type, progression_str):
        parsed = self.parse_roman(progression_str)
        full = self.get_progression(root, scale_type)
        degree_map = {c["degree"]: c for c in full}

        result = []

        for degree, forced_quality in parsed:
            chord = degree_map[degree].copy()

            # Override quality if needed (vi vs VI difference)
            if forced_quality:
                chord = self.chord.get_chord(chord["root"], forced_quality)
                chord = {
                    "degree": degree,
                    "root": chord["notes"][0],
                    "type": forced_quality,
                    "name": chord["name"],
                    "notes": chord["notes"]
                }

            result.append(chord)

        return result

    # -------- SYSTEMS --------
    def harmonic_circle(self, root, scale_type):
        pattern = ["I", "IV", "VII", "III", "VI", "II", "V", "I"]
        return self.get_by_degrees(root, scale_type, pattern)

    def melodic_circle(self, root, scale_type):
        pattern = ["I", "II", "III", "IV", "V", "VI", "VII"]
        return self.get_by_degrees(root, scale_type, pattern)

    def major_thirds(self, root, scale_type):
        pattern = ["I", "III", "V", "VII"]
        return self.get_by_degrees(root, scale_type, pattern)

    def minor_fourths(self, root, scale_type):
        pattern = ["I", "IV", "VII", "III", "VI", "II", "V"]
        return self.get_by_degrees(root, scale_type, pattern)

    # -------- PRINT --------
    def print(self, data, title="Progression"):
        print(f"\n{title}:\n")
        for chord in data:
            print(f"{chord['degree']} → {chord['name']} ({', '.join(chord['notes'])})")

 # -------- PRINT --------
    def print_progression(self, root, scale_type):
        data = self.get_progression(root, scale_type)

        print(f"{root} {scale_type} harmonized scale:\n")

        for chord in data:
            print(
                f"{chord['degree']} → {chord['name']} "
                f"({', '.join(chord['notes'])})"
            )
    def get_progression_by_degrees(self, root, scale_type, degree_list):
        full = self.get_progression(root, scale_type)

        # Map degree → chord
        degree_map = {ch["degree"]: ch for ch in full}

        result = []
        for d in degree_list:
            if d not in degree_map:
                raise ValueError(f"Invalid degree: {d}")
            result.append(degree_map[d])

        return result

    def print_progression_degrees(self, root, scale_type, degree_list):
        data = self.get_progression_by_degrees(root, scale_type, degree_list)

        print(f"{root} {scale_type} progression {degree_list}:\n")
        for chord in data:
            print(f"{chord['degree']} → {chord['name']} ({', '.join(chord['notes'])})")
