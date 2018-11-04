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

        return builder


