class CreateTable:
    def __init__(self, name, fields):
        self._name = name
        self._fields = fields

    def __str__(self):
        builder = 'CREATE TABLE IF NOT EXISTS {0} ( '.format(self._name)
        field_strs = []
        for field in self._fields:
            field_strs.append(str(field))
        builder += ", ".join(field_strs)
        builder += ");"

        print(builder)
        return builder

    def execute(self, cursor):
        cursor.execute(self.__str__())


class AlterTable:
    def __init__(self, name):
        self._name = name
        self._add_col = []

    def add_column(self, field):
        self._add_col.append(field)
        return self

    def __str__(self):
        builder = 'ALTER TABLE {0} '.format(self._name)

        for field in self._add_col:
            builder += "ADD COLUMN {0},".format(str(field))

        if builder[-1] == ",":
            builder = builder[:-1]
        builder += ";"

        print(builder)
        return builder

    def execute(self, cursor):
        cursor.execute(self.__str__())

