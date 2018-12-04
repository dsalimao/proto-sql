class Interleave:
    def __init__(self, fks, ref):
        self._fks = fks
        self._ref = ref

    def add(self, fk):
        self._fks.append(fk)

    def __str__(self):
        return "INTERLEAVE IN PARENT {0} ({1})".format(
            self._ref, ', '.join(self._fks))
