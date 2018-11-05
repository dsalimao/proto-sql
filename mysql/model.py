from proto.item_pb2 import Item
from proto.store_pb2 import Store
from mysql.builder.query import Query, Insert
from google.protobuf.internal.python_message import GeneratedProtocolMessageType
from mysql.common import _get_table_name, _to_value_dict, _to_proto
from mysql.conn_pool import mysql_pool

class Model:
    def __init__(self, message: GeneratedProtocolMessageType):
        self._m = message
        for field in list(message.DESCRIPTOR.fields):
            if field.name == 'id':
                self.id_column = "c" + str(field.number)
                break

    def get(self, id):
        q = Query().from_table(_get_table_name(self._m)).where("{0}={1}".format(self.id_column, id))
        row = mysql_pool.execute(str(q), return_one=True)
        return _to_proto(self._m, row)

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
pp = model.get(2)
print(pp)

