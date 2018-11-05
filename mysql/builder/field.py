class Field:
    def __init__(self, name, **kwargs):
        self._name = name
        self._is_id = False
        if 'is_id' in kwargs:
            self._is_id = True

    def name(self):
        return self._name

    def is_id(self):
        return self._is_id


class IntegerField(Field):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

    def __str__(self):
        builder = self.name() + " INT NOT NULL"
        if self.is_id():
            builder += " PRIMARY KEY AUTO_INCREMENT"
        else:
            builder += " DEFAULT 0"
        return builder


class LongField(Field):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

    def __str__(self):
        builder = self.name() + " BIGINT NOT NULL"
        if self.is_id():
            builder += " PRIMARY KEY AUTO_INCREMENT"
        else:
            builder += " DEFAULT 0"
        return builder


class BooleanField(Field):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

    def __str__(self):
        builder = self.name() + " BOOLEAN NOT NULL DEFAULT 0,"
        return builder


class CharField(Field):
    def __init__(self, name, max_length=100, **kwargs):
        super().__init__(name, **kwargs)
        self._max_length = max_length

    def __str__(self):
        builder = "{0} VARCHAR({1}) NOT NULL DEFAULT \"\"".format(self.name(), self._max_length)
        return builder


class TextField(Field):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

    def __str__(self):
        builder = "{0} TEXT".format(self.name())
        return builder


class EnumField(Field):
    def __init__(self, name, **kwargs):
        super().__init__(name, **kwargs)

    def __str__(self):
        builder = self.name() + " INT NOT NULL DEFAULT 0"
        return builder