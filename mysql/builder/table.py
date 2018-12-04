class CreateTable:
    def __init__(self, name, fields, pk, constraint=None, interleave=None):
        self._name = name
        self._fields = fields
        self._pk = pk
        self._ct = constraint
        self._il = interleave

    def __str__(self):
        builder = 'CREATE TABLE IF NOT EXISTS {0} ( '.format(self._name)
        field_strs = []
        for field in self._fields:
            field_strs.append(str(field))

        field_strs.append(str(self._pk))

        if self._ct:
            field_strs.append(str(self._ct))

        builder += ", ".join(field_strs)

        if self._il:
            builder += ") {0};".format(str(self._il))
        else:
            builder += ");"

        print(builder)
        return builder

    def execute(self, cursor):
        cursor.execute(self.__str__())


class AlterTable:
    def __init__(self, name):
        self._name = name
        self._add_col = []
        self._del_col = []

    def add_column(self, field):
        self._add_col.append(field)
        return self

    def delete_column(self, col_name):
        self._del_col.append(col_name)
        return self

    def __str__(self):
        builder = 'ALTER TABLE {0}'.format(self._name)

        for field in self._add_col:
            builder += " ADD COLUMN {0},".format(str(field))

        for field in self._del_col:
            builder += " DROP COLUMN {0},".format(field)

        if builder[-1] == ",":
            builder = builder[:-1]
        builder += ";"

        print(builder)
        return builder

    def execute(self, cursor):
        cursor.execute(self.__str__())

