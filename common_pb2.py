# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='messages',
  syntax='proto3',
  serialized_options=_b('\n-br.com.blk.marketdata.apigrpc.protos.messagesZ-blk.com.br/marketdata/apigrpc/protos/messages\252\002&Blk.MarketData.APIgRPC.Protos.Messages'),
  serialized_pb=_b('\n\x0c\x63ommon.proto\x12\x08messages\"D\n\x12SecuritySymbolOrId\x12\x10\n\x06symbol\x18\x01 \x01(\tH\x00\x12\x0c\n\x02id\x18\x02 \x01(\x03H\x00\x42\x0e\n\x0csymbol_or_id\"\x07\n\x05\x45mpty*A\n\x0eTradeAggressor\x12\x18\n\x14TRADE_AGGRESSOR_NONE\x10\x00\x12\t\n\x05\x42UYER\x10\x01\x12\n\n\x06SELLER\x10\x02\x42\x87\x01\n-br.com.blk.marketdata.apigrpc.protos.messagesZ-blk.com.br/marketdata/apigrpc/protos/messages\xaa\x02&Blk.MarketData.APIgRPC.Protos.Messagesb\x06proto3')
)

_TRADEAGGRESSOR = _descriptor.EnumDescriptor(
  name='TradeAggressor',
  full_name='messages.TradeAggressor',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TRADE_AGGRESSOR_NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUYER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SELLER', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=105,
  serialized_end=170,
)
_sym_db.RegisterEnumDescriptor(_TRADEAGGRESSOR)

TradeAggressor = enum_type_wrapper.EnumTypeWrapper(_TRADEAGGRESSOR)
TRADE_AGGRESSOR_NONE = 0
BUYER = 1
SELLER = 2



_SECURITYSYMBOLORID = _descriptor.Descriptor(
  name='SecuritySymbolOrId',
  full_name='messages.SecuritySymbolOrId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='messages.SecuritySymbolOrId.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='messages.SecuritySymbolOrId.id', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
    _descriptor.OneofDescriptor(
      name='symbol_or_id', full_name='messages.SecuritySymbolOrId.symbol_or_id',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=26,
  serialized_end=94,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='messages.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=96,
  serialized_end=103,
)

_SECURITYSYMBOLORID.oneofs_by_name['symbol_or_id'].fields.append(
  _SECURITYSYMBOLORID.fields_by_name['symbol'])
_SECURITYSYMBOLORID.fields_by_name['symbol'].containing_oneof = _SECURITYSYMBOLORID.oneofs_by_name['symbol_or_id']
_SECURITYSYMBOLORID.oneofs_by_name['symbol_or_id'].fields.append(
  _SECURITYSYMBOLORID.fields_by_name['id'])
_SECURITYSYMBOLORID.fields_by_name['id'].containing_oneof = _SECURITYSYMBOLORID.oneofs_by_name['symbol_or_id']
DESCRIPTOR.message_types_by_name['SecuritySymbolOrId'] = _SECURITYSYMBOLORID
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.enum_types_by_name['TradeAggressor'] = _TRADEAGGRESSOR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SecuritySymbolOrId = _reflection.GeneratedProtocolMessageType('SecuritySymbolOrId', (_message.Message,), dict(
  DESCRIPTOR = _SECURITYSYMBOLORID,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:messages.SecuritySymbolOrId)
  ))
_sym_db.RegisterMessage(SecuritySymbolOrId)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:messages.Empty)
  ))
_sym_db.RegisterMessage(Empty)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
