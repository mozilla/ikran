# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='common.proto',
  package='userfeedback',
  serialized_pb='\n\x0c\x63ommon.proto\x12\x0cuserfeedback\"\xcd\x01\n\nCommonData\x12\x0f\n\x07gaia_id\x18\x01 \x01(\x06\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1e\n\x16\x64\x65scription_translated\x18\x04 \x01(\t\x12\'\n\x1bsource_description_language\x18\x05 \x01(\t:\x02\x65n\x12\x1a\n\x0bui_language\x18\x06 \x01(\t:\x05\x65n_US\x12\x12\n\nuser_email\x18\x03 \x01(\t\x12 \n\x18unique_report_identifier\x18\x07 \x01(\tB\x02H\x03')




_COMMONDATA = descriptor.Descriptor(
  name='CommonData',
  full_name='userfeedback.CommonData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='gaia_id', full_name='userfeedback.CommonData.gaia_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='description', full_name='userfeedback.CommonData.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='description_translated', full_name='userfeedback.CommonData.description_translated', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='source_description_language', full_name='userfeedback.CommonData.source_description_language', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("en", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='ui_language', full_name='userfeedback.CommonData.ui_language', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=unicode("en_US", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='user_email', full_name='userfeedback.CommonData.user_email', index=5,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='unique_report_identifier', full_name='userfeedback.CommonData.unique_report_identifier', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=31,
  serialized_end=236,
)

DESCRIPTOR.message_types_by_name['CommonData'] = _COMMONDATA

class CommonData(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _COMMONDATA
  
  # @@protoc_insertion_point(class_scope:userfeedback.CommonData)

# @@protoc_insertion_point(module_scope)