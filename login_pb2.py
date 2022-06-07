# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: login.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='login.proto',
  package='messages',
  syntax='proto3',
  serialized_options=_b('\n-br.com.blk.marketdata.apigrpc.protos.messagesZ-blk.com.br/marketdata/apigrpc/protos/messages\252\002&Blk.MarketData.APIgRPC.Protos.Messages'),
  serialized_pb=_b('\n\x0blogin.proto\x12\x08messages\"+\n\x05Login\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"0\n\x0b\x41\x63\x63\x65ssToken\x12\r\n\x05token\x18\x01 \x01(\t\x12\x12\n\ntoken_type\x18\x02 \x01(\tB\x87\x01\n-br.com.blk.marketdata.apigrpc.protos.messagesZ-blk.com.br/marketdata/apigrpc/protos/messages\xaa\x02&Blk.MarketData.APIgRPC.Protos.Messagesb\x06proto3')
)




_LOGIN = _descriptor.Descriptor(
  name='Login',
  full_name='messages.Login',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='messages.Login.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='messages.Login.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=68,
)


_ACCESSTOKEN = _descriptor.Descriptor(
  name='AccessToken',
  full_name='messages.AccessToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='messages.AccessToken.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token_type', full_name='messages.AccessToken.token_type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=118,
)

DESCRIPTOR.message_types_by_name['Login'] = _LOGIN
DESCRIPTOR.message_types_by_name['AccessToken'] = _ACCESSTOKEN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Login = _reflection.GeneratedProtocolMessageType('Login', (_message.Message,), dict(
  DESCRIPTOR = _LOGIN,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:messages.Login)
  ))
_sym_db.RegisterMessage(Login)

AccessToken = _reflection.GeneratedProtocolMessageType('AccessToken', (_message.Message,), dict(
  DESCRIPTOR = _ACCESSTOKEN,
  __module__ = 'login_pb2'
  # @@protoc_insertion_point(class_scope:messages.AccessToken)
  ))
_sym_db.RegisterMessage(AccessToken)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
