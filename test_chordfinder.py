from chordfinder import ChordFinder


class TestChordFinder:
    def setup_method(self):
        self.finder = ChordFinder()

    def test_parse_major(self):
        assert self.finder.parse("C") == ("C", "major")

    def test_parse_minor(self):
        assert self.finder.parse("Am") == ("A", "minor")

    def test_parse_sharp(self):
        assert self.finder.parse("F#m") == ("F#", "minor")

    def test_parse_enharmonic(self):
        assert self.finder.parse("Bb") == ("A#", "major")

    def test_parse_empty(self):
        assert self.finder.parse("") == (None, None)

    def test_parse_invalid(self):
        assert self.finder.parse("X") == (None, None)

    def test_parse_with_spaces(self):
        assert self.finder.parse("  C  ") == ("C", "major")

    def test_find_invalid_returns_zero_matrix(self):
        f = self.finder.find("X")
        assert f.matriz == [[0, 0, 0, 0, 0, 0, 0]]

    def test_get_matrix_major(self):
        m = self.finder.get_matrix("C")
        assert all(len(row) == 7 for row in m)
        assert m[0] == [0, -1, 3, 2, 0, 1, 0]

    def test_get_matrix_am(self):
        m = self.finder.get_matrix("Am")
        assert all(len(row) == 7 for row in m)
        assert m[0] == [0, -1, 0, 2, 2, 1, 0]
