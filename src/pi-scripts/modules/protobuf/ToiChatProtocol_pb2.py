# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ToiChatProtocol.proto

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
  name='ToiChatProtocol.proto',
  package='ToiChatProtocol',
  serialized_pb=_b('\n\x15ToiChatProtocol.proto\x12\x0fToiChatProtocol\"\x87\x01\n\x0eToiChatMessage\x12\x31\n\ndnsMessage\x18\x01 \x01(\x0b\x32\x1b.ToiChatProtocol.DnsMessageH\x00\x12\x33\n\x0b\x63hatMessage\x18\x02 \x01(\x0b\x32\x1c.ToiChatProtocol.ChatMessageH\x00\x42\r\n\x0bmessageType\"\x8c\x02\n\nDnsMessage\x12\x0f\n\x07\x63ommand\x18\x01 \x02(\t\x12\x12\n\nclientName\x18\x02 \x02(\t\x12\x10\n\x08\x63lientId\x18\x03 \x02(\t\x12\x11\n\tdateAdded\x18\x04 \x02(\t\x12\x19\n\x0b\x64\x65scription\x18\x05 \x01(\t:\x04NONE\x12\x37\n\x07\x63lients\x18\x06 \x03(\x0b\x32&.ToiChatProtocol.DnsMessage.DNSClients\x1a`\n\nDNSClients\x12\x12\n\nclientName\x18\x01 \x02(\t\x12\x10\n\x08\x63lientId\x18\x02 \x02(\t\x12\x11\n\tdateAdded\x18\x03 \x02(\t\x12\x19\n\x0b\x64\x65scription\x18\x04 \x01(\t:\x04NONE\"\x19\n\x0b\x43hatMessage\x12\n\n\x02id\x18\x01 \x02(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_TOICHATMESSAGE = _descriptor.Descriptor(
  name='ToiChatMessage',
  full_name='ToiChatProtocol.ToiChatMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dnsMessage', full_name='ToiChatProtocol.ToiChatMessage.dnsMessage', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chatMessage', full_name='ToiChatProtocol.ToiChatMessage.chatMessage', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  oneofs=[
    _descriptor.OneofDescriptor(
      name='messageType', full_name='ToiChatProtocol.ToiChatMessage.messageType',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=43,
  serialized_end=178,
)


_DNSMESSAGE_DNSCLIENTS = _descriptor.Descriptor(
  name='DNSClients',
  full_name='ToiChatProtocol.DnsMessage.DNSClients',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='clientName', full_name='ToiChatProtocol.DnsMessage.DNSClients.clientName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='ToiChatProtocol.DnsMessage.DNSClients.clientId', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dateAdded', full_name='ToiChatProtocol.DnsMessage.DNSClients.dateAdded', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='ToiChatProtocol.DnsMessage.DNSClients.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("NONE").decode('utf-8'),
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
  oneofs=[
  ],
  serialized_start=353,
  serialized_end=449,
)

_DNSMESSAGE = _descriptor.Descriptor(
  name='DnsMessage',
  full_name='ToiChatProtocol.DnsMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command', full_name='ToiChatProtocol.DnsMessage.command', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clientName', full_name='ToiChatProtocol.DnsMessage.clientName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clientId', full_name='ToiChatProtocol.DnsMessage.clientId', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dateAdded', full_name='ToiChatProtocol.DnsMessage.dateAdded', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='ToiChatProtocol.DnsMessage.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("NONE").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clients', full_name='ToiChatProtocol.DnsMessage.clients', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_DNSMESSAGE_DNSCLIENTS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=449,
)


_CHATMESSAGE = _descriptor.Descriptor(
  name='ChatMessage',
  full_name='ToiChatProtocol.ChatMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ToiChatProtocol.ChatMessage.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  oneofs=[
  ],
  serialized_start=451,
  serialized_end=476,
)

_TOICHATMESSAGE.fields_by_name['dnsMessage'].message_type = _DNSMESSAGE
_TOICHATMESSAGE.fields_by_name['chatMessage'].message_type = _CHATMESSAGE
_TOICHATMESSAGE.oneofs_by_name['messageType'].fields.append(
  _TOICHATMESSAGE.fields_by_name['dnsMessage'])
_TOICHATMESSAGE.fields_by_name['dnsMessage'].containing_oneof = _TOICHATMESSAGE.oneofs_by_name['messageType']
_TOICHATMESSAGE.oneofs_by_name['messageType'].fields.append(
  _TOICHATMESSAGE.fields_by_name['chatMessage'])
_TOICHATMESSAGE.fields_by_name['chatMessage'].containing_oneof = _TOICHATMESSAGE.oneofs_by_name['messageType']
_DNSMESSAGE_DNSCLIENTS.containing_type = _DNSMESSAGE
_DNSMESSAGE.fields_by_name['clients'].message_type = _DNSMESSAGE_DNSCLIENTS
DESCRIPTOR.message_types_by_name['ToiChatMessage'] = _TOICHATMESSAGE
DESCRIPTOR.message_types_by_name['DnsMessage'] = _DNSMESSAGE
DESCRIPTOR.message_types_by_name['ChatMessage'] = _CHATMESSAGE

ToiChatMessage = _reflection.GeneratedProtocolMessageType('ToiChatMessage', (_message.Message,), dict(
  DESCRIPTOR = _TOICHATMESSAGE,
  __module__ = 'ToiChatProtocol_pb2'
  # @@protoc_insertion_point(class_scope:ToiChatProtocol.ToiChatMessage)
  ))
_sym_db.RegisterMessage(ToiChatMessage)

DnsMessage = _reflection.GeneratedProtocolMessageType('DnsMessage', (_message.Message,), dict(

  DNSClients = _reflection.GeneratedProtocolMessageType('DNSClients', (_message.Message,), dict(
    DESCRIPTOR = _DNSMESSAGE_DNSCLIENTS,
    __module__ = 'ToiChatProtocol_pb2'
    # @@protoc_insertion_point(class_scope:ToiChatProtocol.DnsMessage.DNSClients)
    ))
  ,
  DESCRIPTOR = _DNSMESSAGE,
  __module__ = 'ToiChatProtocol_pb2'
  # @@protoc_insertion_point(class_scope:ToiChatProtocol.DnsMessage)
  ))
_sym_db.RegisterMessage(DnsMessage)
_sym_db.RegisterMessage(DnsMessage.DNSClients)

ChatMessage = _reflection.GeneratedProtocolMessageType('ChatMessage', (_message.Message,), dict(
  DESCRIPTOR = _CHATMESSAGE,
  __module__ = 'ToiChatProtocol_pb2'
  # @@protoc_insertion_point(class_scope:ToiChatProtocol.ChatMessage)
  ))
_sym_db.RegisterMessage(ChatMessage)


# @@protoc_insertion_point(module_scope)
