# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: subscription.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='subscription.proto',
  package='messages',
  syntax='proto3',
  serialized_options=_b('\n-br.com.blk.marketdata.apigrpc.protos.messagesZ-blk.com.br/marketdata/apigrpc/protos/messages\252\002&Blk.MarketData.APIgRPC.Protos.Messages'),
  serialized_pb=_b('\n\x12subscription.proto\x12\x08messages\"c\n\x12SubscriptionStatus\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x1f\n\x17number_of_subscriptions\x18\x02 \x01(\x05\x12\x1d\n\x15subscribed_securities\x18\x03 \x03(\tB\x87\x01\n-br.com.blk.marketdata.apigrpc.protos.messagesZ-blk.com.br/marketdata/apigrpc/protos/messages\xaa\x02&Blk.MarketData.APIgRPC.Protos.Messagesb\x06proto3')
)




_SUBSCRIPTIONSTATUS = _descriptor.Descriptor(
  name='SubscriptionStatus',
  full_name='messages.SubscriptionStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit', full_name='messages.SubscriptionStatus.limit', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number_of_subscriptions', full_name='messages.SubscriptionStatus.number_of_subscriptions', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscribed_securities', full_name='messages.SubscriptionStatus.subscribed_securities', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=32,
  serialized_end=131,
)

DESCRIPTOR.message_types_by_name['SubscriptionStatus'] = _SUBSCRIPTIONSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SubscriptionStatus = _reflection.GeneratedProtocolMessageType('SubscriptionStatus', (_message.Message,), dict(
  DESCRIPTOR = _SUBSCRIPTIONSTATUS,
  __module__ = 'subscription_pb2'
  # @@protoc_insertion_point(class_scope:messages.SubscriptionStatus)
  ))
_sym_db.RegisterMessage(SubscriptionStatus)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
