# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trades.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='trades.proto',
  package='messages',
  syntax='proto3',
  serialized_options=_b('\n-br.com.blk.marketdata.apigrpc.protos.messagesZ-blk.com.br/marketdata/apigrpc/protos/messages\252\002&Blk.MarketData.APIgRPC.Protos.Messages'),
  serialized_pb=_b('\n\x0ctrades.proto\x12\x08messages\x1a\x0c\x63ommon.proto\"\xd4\x02\n\x05Trade\x12\x0e\n\x06symbol\x18\x01 \x01(\t\x12\x11\n\tdate_time\x18\x02 \x01(\t\x12\x10\n\x08trade_id\x18\x03 \x01(\x03\x12\r\n\x05price\x18\x04 \x01(\x01\x12\x10\n\x08quantity\x18\x05 \x01(\x01\x12\x0e\n\x06volume\x18\x06 \x01(\x01\x12\x31\n\x0ftrade_aggressor\x18\x07 \x01(\x0e\x32\x18.messages.TradeAggressor\x12\x17\n\x0f\x62uyer_broker_id\x18\x08 \x01(\x03\x12\x18\n\x10seller_broker_id\x18\t \x01(\x03\x12\x0e\n\x06\x63hange\x18\n \x01(\x01\x12\x19\n\x11\x63hange_percentage\x18\x0b \x01(\x01\x12\x13\n\x0bis_canceled\x18\x0c \x01(\x08\x12\x12\n\nis_crossed\x18\r \x01(\x08\x12\x17\n\x0fis_after_market\x18\x0e \x01(\x08\x12\x12\n\nis_auction\x18\x0f \x01(\x08\"\'\n\x06Trades\x12\x1d\n\x04list\x18\x01 \x03(\x0b\x32\x0f.messages.Trade\"S\n\rTradesRequest\x12\x0e\n\x06length\x18\x01 \x01(\x05\x12\x32\n\x0csymbol_or_id\x18\x02 \x01(\x0b\x32\x1c.messages.SecuritySymbolOrIdB\x87\x01\n-br.com.blk.marketdata.apigrpc.protos.messagesZ-blk.com.br/marketdata/apigrpc/protos/messages\xaa\x02&Blk.MarketData.APIgRPC.Protos.Messagesb\x06proto3')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])




_TRADE = _descriptor.Descriptor(
  name='Trade',
  full_name='messages.Trade',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='symbol', full_name='messages.Trade.symbol', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_time', full_name='messages.Trade.date_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trade_id', full_name='messages.Trade.trade_id', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='messages.Trade.price', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='messages.Trade.quantity', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume', full_name='messages.Trade.volume', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='trade_aggressor', full_name='messages.Trade.trade_aggressor', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='buyer_broker_id', full_name='messages.Trade.buyer_broker_id', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seller_broker_id', full_name='messages.Trade.seller_broker_id', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='change', full_name='messages.Trade.change', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='change_percentage', full_name='messages.Trade.change_percentage', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_canceled', full_name='messages.Trade.is_canceled', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_crossed', full_name='messages.Trade.is_crossed', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_after_market', full_name='messages.Trade.is_after_market', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_auction', full_name='messages.Trade.is_auction', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=41,
  serialized_end=381,
)


_TRADES = _descriptor.Descriptor(
  name='Trades',
  full_name='messages.Trades',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='messages.Trades.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=383,
  serialized_end=422,
)


_TRADESREQUEST = _descriptor.Descriptor(
  name='TradesRequest',
  full_name='messages.TradesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='length', full_name='messages.TradesRequest.length', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol_or_id', full_name='messages.TradesRequest.symbol_or_id', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=424,
  serialized_end=507,
)

_TRADE.fields_by_name['trade_aggressor'].enum_type = common__pb2._TRADEAGGRESSOR
_TRADES.fields_by_name['list'].message_type = _TRADE
_TRADESREQUEST.fields_by_name['symbol_or_id'].message_type = common__pb2._SECURITYSYMBOLORID
DESCRIPTOR.message_types_by_name['Trade'] = _TRADE
DESCRIPTOR.message_types_by_name['Trades'] = _TRADES
DESCRIPTOR.message_types_by_name['TradesRequest'] = _TRADESREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Trade = _reflection.GeneratedProtocolMessageType('Trade', (_message.Message,), dict(
  DESCRIPTOR = _TRADE,
  __module__ = 'trades_pb2'
  # @@protoc_insertion_point(class_scope:messages.Trade)
  ))
_sym_db.RegisterMessage(Trade)

Trades = _reflection.GeneratedProtocolMessageType('Trades', (_message.Message,), dict(
  DESCRIPTOR = _TRADES,
  __module__ = 'trades_pb2'
  # @@protoc_insertion_point(class_scope:messages.Trades)
  ))
_sym_db.RegisterMessage(Trades)

TradesRequest = _reflection.GeneratedProtocolMessageType('TradesRequest', (_message.Message,), dict(
  DESCRIPTOR = _TRADESREQUEST,
  __module__ = 'trades_pb2'
  # @@protoc_insertion_point(class_scope:messages.TradesRequest)
  ))
_sym_db.RegisterMessage(TradesRequest)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)