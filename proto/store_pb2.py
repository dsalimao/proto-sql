# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: store.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='store.proto',
  package='proto',
  syntax='proto3',
  serialized_pb=_b('\n\x0bstore.proto\x12\x05proto\"\xc1\x01\n\x05Store\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12*\n\nstore_type\x18\x04 \x01(\x0e\x32\x16.proto.Store.StoreType\x12\x0f\n\x07web_url\x18\x05 \x01(\t\"L\n\tStoreType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07GROCERY\x10\x01\x12\x0b\n\x07OUTDOOR\x10\x02\x12\r\n\tCOSMETICS\x10\x03\x12\t\n\x05\x43LOTH\x10\x04\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_STORE_STORETYPE = _descriptor.EnumDescriptor(
  name='StoreType',
  full_name='proto.Store.StoreType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROCERY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OUTDOOR', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COSMETICS', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOTH', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=140,
  serialized_end=216,
)
_sym_db.RegisterEnumDescriptor(_STORE_STORETYPE)


_STORE = _descriptor.Descriptor(
  name='Store',
  full_name='proto.Store',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='proto.Store.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.Store.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='proto.Store.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='store_type', full_name='proto.Store.store_type', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='web_url', full_name='proto.Store.web_url', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _STORE_STORETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=216,
)

_STORE.fields_by_name['store_type'].enum_type = _STORE_STORETYPE
_STORE_STORETYPE.containing_type = _STORE
DESCRIPTOR.message_types_by_name['Store'] = _STORE

Store = _reflection.GeneratedProtocolMessageType('Store', (_message.Message,), dict(
  DESCRIPTOR = _STORE,
  __module__ = 'store_pb2'
  # @@protoc_insertion_point(class_scope:proto.Store)
  ))
_sym_db.RegisterMessage(Store)


# @@protoc_insertion_point(module_scope)