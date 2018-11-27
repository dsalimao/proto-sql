from proto.item_pb2 import Item
from proto.store_pb2 import Store
from mysql.builder.query import Query, Insert
from google.protobuf.internal.python_message import GeneratedProtocolMessageType
from mysql.common import _get_table_name, _to_value_dict, _to_proto
from mysql.conn_pool import mysql_pool

# Operator and it's valid type
OP = {
    'gt': ['>', 3,5], # long and int
    'lt': ['<', 3,5], # long and int
    'ge': ['>=',3,5], # long and int
    'le': ['<=',3,5], # long and int
    'eq': ['=',3,5,9,14], # all
    'in': ['in',9,14], # enum and string
}

class Model:
    def __init__(self, message: GeneratedProtocolMessageType):
        self._m = message
        self._fields = {}
        for field in list(message.DESCRIPTOR.fields):
            self._fields[field.name] = (field.number, field.type)
            if field.name == 'id':
                self.id_column = "c" + str(field.number)

    def get(self, id):
        q = Query().from_table(_get_table_name(self._m)).where("{0}={1}".format(self.id_column, id))
        row = mysql_pool.execute(str(q), return_one=True)
        return _to_proto(self._m, row)

    def filter(self, **kwargs):
        def to_string(val, is_str):
            if isinstance(val, list):
                if is_str:
                    return "(" + ",".join(["'" +str(v)+"'" for v in val]) + ")"
                else:
                    return "(" + ",".join([str(v) for v in val]) + ")"
            elif is_str:
                return "'"+str(val)+"'"
            else:
                return str(val)

        wheres = []
        for key in kwargs:
            field = key.split('__')[0]
            op = key.split('__')[1]
            val = kwargs[key]
            if field not in self._fields:
                raise ValueError('No field {0}'.format(field))
            if op not in OP:
                raise ValueError('No operator {0}'.format(op))
            if self._fields[field][1] not in OP[op]:
                raise ValueError('Operator {0} is invalid for field {1} with type {2}'.format(op, field, self._fields[field][1]))
            if op == 'in' and not isinstance(val, list):
                raise ValueError('In operator only accept list')
            wheres.append('c'+str(self._fields[field][0]) + OP[op][0] + to_string(val, self._fields[field][1]==9))

        q = Query().from_table(_get_table_name(self._m)).where(' AND '.join(wheres))
        rows = mysql_pool.execute(str(q), return_one=False)

        return [_to_proto(self._m, row) for row in rows]

    def insert(self, obj):
        _,_,values = _to_value_dict(self._m, obj)
        q = Insert(values).into_table(_get_table_name(self._m))
        row = mysql_pool.execute(str(q), write=True)
        return row

model = Model(Store)
a = Store()
a.name = "123asd22"
a.web_url ="www.google.com"
a.store_type = Store.OUTDOOR
print(a)
print(Store.CLOTH)
print(type(a.store_type))
model.insert(a)
ppp=model.filter(name__eq='123asd22',store_type__eq=2)
print(ppp)
pp = model.get(2)
print(pp)

