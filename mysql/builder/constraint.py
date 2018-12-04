class Constraint:
    def __init__(self, name, fks, ref):
        """
        CONSTRAINT fk_order FOREIGN KEY (customer, order) REFERENCES orders
        """
        self._name = name
        self._fks = fks
        self._ref = ref

    def add(self, fk):
        self._fks.append(fk)

    def __str__(self):
        return "CONSTRAINT {0} FOREIGN KEY ({1}) REFERENCES {2}".format(
            self._name, ', '.join(self._fks), self._ref)
