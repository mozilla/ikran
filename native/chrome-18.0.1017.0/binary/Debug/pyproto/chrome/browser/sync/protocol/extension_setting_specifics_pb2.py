# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import sync_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='extension_setting_specifics.proto',
  package='sync_pb',
  serialized_pb='\n!extension_setting_specifics.proto\x12\x07sync_pb\x1a\nsync.proto\"M\n\x19\x45xtensionSettingSpecifics\x12\x14\n\x0c\x65xtension_id\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t:Y\n\x11\x65xtension_setting\x12\x18.sync_pb.EntitySpecifics\x18\x9f\xef\x05 \x01(\x0b\x32\".sync_pb.ExtensionSettingSpecificsB\x04H\x03X\x01')


EXTENSION_SETTING_FIELD_NUMBER = 96159
extension_setting = descriptor.FieldDescriptor(
  name='extension_setting', full_name='sync_pb.extension_setting', index=0,
  number=96159, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_EXTENSIONSETTINGSPECIFICS = descriptor.Descriptor(
  name='ExtensionSettingSpecifics',
  full_name='sync_pb.ExtensionSettingSpecifics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='extension_id', full_name='sync_pb.ExtensionSettingSpecifics.extension_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='key', full_name='sync_pb.ExtensionSettingSpecifics.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='sync_pb.ExtensionSettingSpecifics.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=58,
  serialized_end=135,
)

DESCRIPTOR.message_types_by_name['ExtensionSettingSpecifics'] = _EXTENSIONSETTINGSPECIFICS

class ExtensionSettingSpecifics(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EXTENSIONSETTINGSPECIFICS
  
  # @@protoc_insertion_point(class_scope:sync_pb.ExtensionSettingSpecifics)

extension_setting.message_type = _EXTENSIONSETTINGSPECIFICS
sync_pb2.EntitySpecifics.RegisterExtension(extension_setting)
# @@protoc_insertion_point(module_scope)