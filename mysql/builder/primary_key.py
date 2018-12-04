class PrimaryKey:
    def __init__(self, names):
        self._names = names

    def add(self, name):
        self._names.append(name)

    def __str__(self):
        return "PRIMARY KEY ({0})".format(', '.join(self._names))