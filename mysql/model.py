from proto.item_pb2 import Item
from google.protobuf.message import Message
from mysql.builder.table import CreateTable
from mysql.builder.query import Query, Insert
from mysql.builder import field as field_
from google.protobuf.internal.python_message import GeneratedProtocolMessageType
from mysql.common import get_table_name, to_dict

class Model:
    def __init__(self, message):
        if type(message) != GeneratedProtocolMessageType or not issubclass(message, Message):
            raise Exception('Not a proto message')
        self._m = message

    def get(self, id):
        q = Query().from_table(get_table_name(self._m)).where("id=1")
        print(q)

    def insert(self, obj):
        q = Insert(to_dict(self._m, obj)).into_table(get_table_name(self._m))
        return q

a=Model(Item)
i = Item()
i.name ='asdasd'
print(a.insert(i))

