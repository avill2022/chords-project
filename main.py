from scale import Scale
from chord import Chord
from progression import Progression


s = Scale()
c = Chord()


p = Progression(s, c)
p.print_progression("C", "major")
p.print_progression("A", "minor")
p.print_progression_degrees("C", "major", ["I", "IV", "V"])
p.print_progression_degrees("A", "minor", ["I", "VI", "VII"])
p.print(
    p.get_by_degrees("C", "major", ["I", "IV", "V"]),
    "3-Chord (I-IV-V)"
)
p.print(
    p.get_from_roman("C", "major", "I - V - vi - IV"),
    "Roman Progression"
)
p.print(
    p.harmonic_circle("C", "major"),
    "Harmonic Circle"
)
p.print(
    p.melodic_circle("C", "major"),
    "Melodic Circle"
)
p.print(
    p.major_thirds("C", "major"),
    "Major Thirds"
)
p.print(
    p.minor_fourths("C", "major"),
    "Cycle of Fourths"
)
