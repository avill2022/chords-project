CHROMATIC_SCALE = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def note_index(note: str) -> int:
    return CHROMATIC_SCALE.index(note)

class figures:
    def __init__(self):
        self.index = 0
        self.matriz = [
            [0,-1,3,2,0,1,0],
            [3,-1,3,5,5,5,3],
            [5,8,7,5,5,5,8],
            [8,8,10,10,9,8,8],
            [10,-1,10,10,12,13,12],
        ]

    def add(self, n: int):
        self.index = n
        self.matriz = [[x if x == -1 else x + n for x in row] for row in self.matriz]
        return self.matriz

    def normaizate(self):
        for row in self.matriz:
            while True:
                vals = [x for x in row if x != -1]
                if not vals:
                    break
                if min(vals) < 12:
                    break
                for i in range(len(row)):
                    if row[i] != -1:
                        row[i] -= 12

    def organize(self):
        min_val = float('inf')
        min_idx = 0
        for i, row in enumerate(self.matriz):
            vals = [x for x in row if x != -1]
            if vals:
                rmin = min(vals)
                if rmin < min_val:
                    min_val = rmin
                    min_idx = i
        self.matriz = self.matriz[min_idx:] + self.matriz[:min_idx]

    def p_normailzation(self):
        for row in self.matriz:
            vals = [x for x in row if x != -1]
            if vals and max(vals) >= 5:
                first = row[0]
                for i in range(1, len(row)):
                    if row[i] != -1:
                        row[i] -= (first-1)

    def c_normalization(self):
        for row in self.matriz:
            vals = [x for x in row if x != -1]
            if vals and max(vals) <= 4:
                row[0] = 0

    def show_complete(self):
        strings = ['e', 'B', 'G', 'D', 'A', 'E']
        for row in self.matriz:
            capo = row[0]
            vals = list(reversed(row[1:]))

            rel_positions = []
            max_rel = 0
            for v in vals:
                if v != -1:
                    rel = v - capo
                    rel_positions.append(rel)
                    if rel > max_rel:
                        max_rel = rel
                else:
                    rel_positions.append(None)

            num_frets = max_rel + 1

            print(f'     {capo}')
            for label, rel, v in zip(strings, rel_positions, vals):
                if v == -1:
                    label = 'x'
                if rel is None or rel < 0:
                    line = f'{label} -||' + '---|' * num_frets
                else:
                    parts = ['-O-' if i == rel else '---' for i in range(num_frets)]
                    line = f'{label} -||' + '|'.join(parts) + '|'
                print(line)

    def show_chords(self):
        strings = ['e', 'B', 'G', 'D', 'A', 'E']
        for row in self.matriz:
            capo = 'no' if row[0] == 0 else str(row[0])
            print(f'capo:{capo}')
            for label, val in zip(strings, reversed(row[1:])):
                v = 'x' if val == -1 else str(val)
                print(f'{label} |---{v}---|')

    def show_chords_(self):
        strings = ['e', 'B', 'G', 'D', 'A', 'E']#e -||-O-|
        for row in self.matriz:
            capo = '' if row[0] == 0 else str(row[0])
            print(f'     {capo}')
            for label, val in zip(strings, reversed(row[1:])):
                v = 'x' if val == -1 else str(val)
                if v == 'x':
                    print(f'x-||---|---|---|---|')
                else:
                        print(f'{label}-||' + '|'.join(['-O-' if i == int(v) else '---' for i in range(1,5)]) + '|')
                    #print(f'{label} |---{v}---|')

    def show(self):
        note = CHROMATIC_SCALE[self.index]
        for row in self.matriz:
            vals = ''.join(str(x) if x != -1 else 'x' for x in row[1:])
            capo = 'NO' if row[0] == 0 else str(row[0])
            print(f'{note}:{vals} CAPO:{capo}')

data = figures()
#data.add(0)
data.normaizate()
data.organize()
data.p_normailzation()
#data.c_normalization()
data.show_chords_()
