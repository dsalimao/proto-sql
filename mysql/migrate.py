from proto.item_pb2 import Item
from proto.store_pb2 import Store
from proto.receipts_pb2 import Receipts
from mysql.builder.table import CreateTable, AlterTable
from mysql.builder import field as field_
from mysql.builder.primary_key import PrimaryKey
from mysql.builder.constraint import Constraint
from mysql.builder.interleave import Interleave
from mysql.common import _get_table_names, _to_meta
from mysql.meta import _init_meta, _get_table_meta, _replace_table_meta
from mysql.conn_pool import mysql_pool
from google.protobuf.descriptor import Descriptor

TYPE = {
    3: field_.LongField,
    5: field_.IntegerField,
    9: field_.TextField,
    14: field_.EnumField,
}


def migrate(message):
    _init_meta()
    tables = _get_table_names(message)
    for table in tables:
        old_table_metadata = _get_table_meta(table[0])
        new_table_metadata = _to_meta(table[1])

        conn = mysql_pool.start_manual()
        print(table[0])
        print(old_table_metadata)
        print(new_table_metadata)
        if not old_table_metadata:
            # Doesn't exist, create the table, and update in meta table.
            try:
                with conn.cursor() as cursor:
                    _replace_table_meta(table[0], new_table_metadata, cursor)
                    _create_table(table[0], table[1], table[2]).execute(cursor)
                # conn.commit()
            except Exception as e:
                raise e
            finally:
                mysql_pool.end_manual(conn)
        else:
            # Already exist, alter the table, and update in meta table.
            alter_table = _alter_table(table[0], old_table_metadata, new_table_metadata)
            if alter_table:
                try:
                    with conn.cursor() as cursor:
                        _replace_table_meta(table[0], new_table_metadata, cursor)
                        alter_table.execute(cursor)
                    # conn.commit()
                except Exception as e:
                    raise e
                finally:
                    mysql_pool.end_manual(conn)


def _create_table(table_name, descriptor: Descriptor, parents=[]):
    has_id = False
    fields = []

    for field in list(descriptor.fields):
        if field.name == 'id':
            if field.type == 3 or field.type == 5:
                fields.append(TYPE[field.type]("id", is_id=True))
                has_id = True
            else:
                raise Exception("id must be int32 or int64")
        else:
            if field.type != 11:
                fields.append(TYPE[field.type]("c" + str(field.number)))

    if parents:
        pk = PrimaryKey([])
        ct = Constraint('fk', [], parents[-1])
        il = Interleave([], parents[-1])
        for parent in parents:
            pk.add(parent)
            ct.add(parent)
            il.add(parent)
        pk.add('id')
    else:
        pk = PrimaryKey(['id'])
        ct = None
        il = None

    if not has_id:
        raise Exception("message must have int32 or int64 typed `id` field as primary key.")

    return CreateTable(table_name, fields, pk, ct, il)


def _alter_table(table_name, old_table_metadata, new_table_metadata):
    old_dict = {}
    for col in old_table_metadata:
        old_dict[col['db_column']] = col

    new_dict = {}
    for col in new_table_metadata:
        new_dict[col['db_column']] = col

    alter = AlterTable(table_name)
    altered = False

    for key in new_dict:
        if key not in old_dict:
            # Find new field in proto, need to add new column in table
            add_field = TYPE[new_dict[key]['type']](new_dict[key]['db_column'])
            alter.add_column(add_field)
            altered = True
        else:
            if new_dict[key]['type'] != old_dict[key]['type']:
                raise Exception("Should not modify the type of field number %s".format(key[1:]))
            elif new_dict[key]['py_column'] != old_dict[key]['py_column']:
                altered = True

    for key in old_dict:
        if key not in new_dict:
            alter.delete_column(key)
            altered = True

    if altered:
        return alter
    return None


migrate(Receipts)
# migrate(Store)
