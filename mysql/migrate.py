from proto.item_pb2 import Item
from proto.store_pb2 import Store
from google.protobuf.message import Message
from mysql.builder.table import CreateTable
from mysql.builder import field as field_
from google.protobuf.internal.python_message import GeneratedProtocolMessageType
from mysql.common import _get_table_name, _to_meta
from mysql.meta import _init_meta, _get_table_meta, _replace_table_meta
from mysql.conn_pool import mysql_pool


TYPE = {
    3: field_.LongField,
    5: field_.IntegerField,
    9: field_.TextField,
    14: field_.EnumField,
}


def migrate(message):
    _init_meta()
    table_name = _get_table_name(message)
    old_table_metadata = _get_table_meta(table_name)
    new_table_metadata = _to_meta(message)

    conn = mysql_pool.start_manual()
    if not old_table_metadata:
        # Doesn't exist, create the table, and update in meta table.
        try:
            with conn.cursor() as cursor:
                _replace_table_meta(table_name, new_table_metadata, cursor)
                _create_table(message).execute(cursor)
            conn.commit()
        except Exception as e:
            raise e
        finally:
            mysql_pool.end_manual(conn)
    else:
        # TODO
        # Already exist, alter the table, and update in meta table.
        try:
            with conn.cursor() as cursor:
                _replace_table_meta(table_name, new_table_metadata, cursor)
                _create_table(message).execute(cursor)
            conn.commit()
        except Exception as e:
            raise e
        finally:
            mysql_pool.end_manual(conn)


def _create_table(message: GeneratedProtocolMessageType):
    table_name = _get_table_name(message)

    has_id = False
    fields = []
    for field in list(message.DESCRIPTOR.fields):
        if field.name == 'id':
            if field.type == 3 or field.type == 5:
                fields.append(TYPE[field.type]("c"+str(field.number), is_id=True))
                has_id = True
            else:
                raise Exception("id must be int32 or int64")
        else:
            fields.append(TYPE[field.type]("c"+str(field.number)))
    if not has_id:
        raise Exception("message must have int32 or int64 typed `id` field as primary key.")

    return CreateTable(table_name, fields)


migrate(Store)