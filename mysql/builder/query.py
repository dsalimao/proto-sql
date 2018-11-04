class Query:
    def __init__(self, selects=["*"]):
        self._selects = selects

    def from_table(self, table):
        self._from = table
        return self

    def where(self, where_clause):
        self._where_clause = where_clause
        return self

    def __str__(self):
        selects = ", ".join(self._selects)
        from_ = self._from
        where = self._where_clause
        builder = 'SELECT {0} FROM {1} WHERE {2};'.format(selects, from_, where)
        return builder


class Insert:
    def __init__(self, dic):
        self._dic = dic

    def into_table(self, table):
        self._table = table
        return self

    def __str__(self):
        columns = []
        values = []
        for column in self._dic:
            columns.append(str(column))
            values.append(str(self._dic[column]))

        builder = 'INSERT INTO {0} ({1}) VALUES ({2});'.format(self._table, ", ".join(columns), ", ".join(values))
        return builder
