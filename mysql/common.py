from google.protobuf.internal.python_message import GeneratedProtocolMessageType
from google.protobuf.message import Message
from google.protobuf.descriptor import Descriptor


def _get_table_names(message: GeneratedProtocolMessageType):
    """
    Gets the table name in mysql based on Proto Message
    :param message
    """
    base_name = message.DESCRIPTOR.full_name.replace(".", "_").lower()
    res = {base_name: message.DESCRIPTOR}
    for field in message.DESCRIPTOR.fields:
        if field.type == 11: # message field
            res.update(_get_table_names_by_descriptor(field.message_type, prefix=base_name+"_c"+str(field.number)))
    return res


def _get_table_names_by_descriptor(descriptor: Descriptor, prefix=''):
    res = {prefix: descriptor}
    for field in descriptor.fields:
        if field.type == 11: # message field
            res.update(_get_table_names_by_descriptor(field.message_type, prefix=prefix+"_c"+str(field.number)))
    return res


def _to_meta(descriptor: Descriptor):
    """
    Builds the db table metadata for a Proto Message
    :param message
    :return list
    """
    columns = []

    fields = list(descriptor.fields)
    for field in fields:
        if field.type != 11:
            column = {'db_column': "c" + str(field.number), 'py_column': field.name, 'type': field.type}
            columns.append(column)
    return columns


def _to_value_dict(message: GeneratedProtocolMessageType, obj: Message):
    """
    Builds a dict from a proto message.
    :param message
    :param obj
    :return dict
    """
    fields = list(message.DESCRIPTOR.fields)
    dict_ = {}
    id_c = "c1"
    id_v = 0
    for field in fields:
        if field.name == "id":
            id_c = "c" +str(field.number)
            id_v = getattr(obj, field.name)
            continue
        val = getattr(obj, field.name)
        if isinstance(val, str):
            val = "\"{0}\"".format(val)
        dict_["c" + str(field.number)] = val
    return id_c, id_v, dict_


def _to_proto(message: GeneratedProtocolMessageType, row):
    """
    Builds a proto message instance from db row
    :param message
    :param row: the row returned by pymysql execute query
    """
    fields = list(message.DESCRIPTOR.fields)
    m = message()
    for field in fields:
        db_column = "c" + str(field.number)
        if db_column in row:
            setattr(m, field.name, row[db_column])
    return m

