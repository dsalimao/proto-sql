from proto.item_pb2 import Item
from google.protobuf.message import Message
from mysql.builder.table import CreateTable
from mysql.builder import field as field_
from google.protobuf.internal.python_message import GeneratedProtocolMessageType
from mysql.common import get_table_name
TYPE = {
    3: field_.LongField,
    5: field_.IntegerField,
    9: field_.TextField,
}

def migrate(message):
    if type(message) != GeneratedProtocolMessageType or not issubclass(message, Message):
        raise Exception('Not a proto message')

    table_name = get_table_name(message)

    has_id = False
    fields = []
    for field in list(Item.DESCRIPTOR.fields):
        if field.name == 'id':
            if field.type == 3 or field.type == 5:
                fields.append(TYPE[field.type](field.name, is_id=True))
                has_id = True
            else:
                raise Exception("id must be int32 or int64")
        else:
            fields.append(TYPE[field.type](field.name))
    if not has_id:
        raise Exception("message must have int32 or int64 typed `id` field as primary key.")

    c = CreateTable(table_name, fields)
    print(c)


item=Item()
item.id = 1
# res = list(Item.DESCRIPTOR.fields)
# for r in res:
#     print(r.type)
# print(res)
migrate(Item)
# Item.descriptor