import parameters
import itertools as it


class Table:
    ALL_CARDS: set = set(range(1, parameters.DECK_SIZE + 1))

    def __init__(self, main_hand: set):
        self.main_hand: set = main_hand
        self.other_hand: set = Table.ALL_CARDS - main_hand

        self.main_perms = list(it.permutations(self.main_hand))
        self.other_perms = list(it.permutations(self.other_hand))

        self.score_table = {(main, other): self._cell_score(main, other) for
                            (main, other) in it.product(self.main_perms, self.other_perms)}

        self.main_mins = {main: min([self.score_table.get((main, other)) for other in self.other_perms])
                          for main in self.main_perms}

        self.other_maxs = {other: max([self.score_table.get((main, other)) for main in self.main_perms])
                           for other in self.other_perms}

        self.mesh_count = 0
        self.min_count = 0
        self.max_count = 0

        self._counting()

    def _counting(self):
        for main in self.main_perms:
            for other in self.other_perms:
                if self.is_mesh(main, other):
                    self.mesh_count += 1
                elif self.is_min(main, other):
                    self.min_count += 1
                elif self.is_max(main, other):
                    self.max_count += 1

    def is_min(self, main, other):
        return self.score_table[(main, other)] == self.main_mins[main]

    def is_max(self, main, other):
        return self.score_table[(main, other)] == self.other_maxs[other]

    def is_mesh(self, main, other):
        return self.is_max(main, other) and self.is_min(main, other)

    def specifier(self, main, other):
        if self.is_mesh(main, other):
            return "mesh"
        elif self.is_max(main, other):
            return "max"
        elif self.is_min(main, other):
            return "min"
        else:
            return ""

    @staticmethod
    def _cell_score(main, other):
        return sum(map(lambda t: 1 if t[0] > t[1] else 0, zip(main, other)))

    def name(self):
        return "-".join(map(str, self.main_hand))

    def __str__(self):
        return f"table (main: {self.main_hand}, other: {self.other_hand})"
