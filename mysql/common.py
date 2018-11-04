
def get_table_name(message):
    return message.DESCRIPTOR.full_name.replace(".", "_").lower()


def to_dict(message, obj):
    fields = list(message.DESCRIPTOR.fields)
    dict = {}
    for field in fields:
        val = getattr(obj, field.name)
        if isinstance(val, str):
            val = "\"{0}\"".format(val)
        dict[field.name] = val
    return dict

