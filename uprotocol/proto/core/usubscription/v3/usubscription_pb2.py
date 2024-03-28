# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: core/usubscription/v3/usubscription.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import uprotocol.proto.ustatus_pb2 as ustatus__pb2
import uprotocol.proto.uri_pb2 as uri__pb2
import uprotocol.proto.uprotocol_options_pb2 as uprotocol__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)core/usubscription/v3/usubscription.proto\x12\x1fuprotocol.core.usubscription.v3\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\rustatus.proto\x1a\turi.proto\x1a\x17uprotocol_options.proto\"\x9c\x01\n\x13SubscribeAttributes\x12*\n\x06\x65xpire\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12%\n\x07\x64\x65tails\x18\x02 \x03(\x0b\x32\x14.google.protobuf.Any\x12\x1d\n\x10sample_period_ms\x18\x03 \x01(\rH\x00\x88\x01\x01\x42\x13\n\x11_sample_period_ms\"X\n\x0eSubscriberInfo\x12\x1f\n\x03uri\x18\x01 \x01(\x0b\x32\x12.uprotocol.v1.UUri\x12%\n\x07\x64\x65tails\x18\x02 \x03(\x0b\x32\x14.google.protobuf.Any\"\xed\x01\n\x12SubscriptionStatus\x12H\n\x05state\x18\x01 \x01(\x0e\x32\x39.uprotocol.core.usubscription.v3.SubscriptionStatus.State\x12!\n\x04\x63ode\x18\x02 \x01(\x0e\x32\x13.uprotocol.v1.UCode\x12\x0f\n\x07message\x18\x03 \x01(\t\"Y\n\x05State\x12\x10\n\x0cUNSUBSCRIBED\x10\x00\x12\x15\n\x11SUBSCRIBE_PENDING\x10\x01\x12\x0e\n\nSUBSCRIBED\x10\x02\x12\x17\n\x13UNSUBSCRIBE_PENDING\x10\x03\"\xd2\x01\n\x13\x45ventDeliveryConfig\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12X\n\nattributes\x18\x03 \x03(\x0b\x32\x44.uprotocol.core.usubscription.v3.EventDeliveryConfig.AttributesEntry\x1aG\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\"\xc7\x01\n\x13SubscriptionRequest\x12!\n\x05topic\x18\x01 \x01(\x0b\x32\x12.uprotocol.v1.UUri\x12\x43\n\nsubscriber\x18\x02 \x01(\x0b\x32/.uprotocol.core.usubscription.v3.SubscriberInfo\x12H\n\nattributes\x18\x03 \x01(\x0b\x32\x34.uprotocol.core.usubscription.v3.SubscribeAttributes\"\xc4\x01\n\x14SubscriptionResponse\x12\x43\n\x06status\x18\x01 \x01(\x0b\x32\x33.uprotocol.core.usubscription.v3.SubscriptionStatus\x12\x44\n\x06\x63onfig\x18\x02 \x01(\x0b\x32\x34.uprotocol.core.usubscription.v3.EventDeliveryConfig\x12!\n\x05topic\x18\x03 \x01(\x0b\x32\x12.uprotocol.v1.UUri\"|\n\x12UnsubscribeRequest\x12!\n\x05topic\x18\x01 \x01(\x0b\x32\x12.uprotocol.v1.UUri\x12\x43\n\nsubscriber\x18\x02 \x01(\x0b\x32/.uprotocol.core.usubscription.v3.SubscriberInfo\"\\\n\x17\x46\x65tchSubscribersRequest\x12!\n\x05topic\x18\x01 \x01(\x0b\x32\x12.uprotocol.v1.UUri\x12\x13\n\x06offset\x18\x02 \x01(\rH\x00\x88\x01\x01\x42\t\n\x07_offset\"\xbb\x01\n\x18\x46\x65tchSubscribersResponse\x12\x44\n\x0bsubscribers\x18\x01 \x03(\x0b\x32/.uprotocol.core.usubscription.v3.SubscriberInfo\x12\x1d\n\x10has_more_records\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12%\n\x06status\x18\x03 \x01(\x0b\x32\x15.uprotocol.v1.UStatusB\x13\n\x11_has_more_records\"\xcb\x02\n\x0cSubscription\x12!\n\x05topic\x18\x01 \x01(\x0b\x32\x12.uprotocol.v1.UUri\x12\x43\n\nsubscriber\x18\x02 \x01(\x0b\x32/.uprotocol.core.usubscription.v3.SubscriberInfo\x12\x43\n\x06status\x18\x03 \x01(\x0b\x32\x33.uprotocol.core.usubscription.v3.SubscriptionStatus\x12H\n\nattributes\x18\x04 \x01(\x0b\x32\x34.uprotocol.core.usubscription.v3.SubscribeAttributes\x12\x44\n\x06\x63onfig\x18\x05 \x01(\x0b\x32\x34.uprotocol.core.usubscription.v3.EventDeliveryConfig\"\xb2\x01\n\x19\x46\x65tchSubscriptionsRequest\x12#\n\x05topic\x18\x01 \x01(\x0b\x32\x12.uprotocol.v1.UUriH\x00\x12\x45\n\nsubscriber\x18\x02 \x01(\x0b\x32/.uprotocol.core.usubscription.v3.SubscriberInfoH\x00\x12\x13\n\x06offset\x18\x03 \x01(\rH\x01\x88\x01\x01\x42\t\n\x07requestB\t\n\x07_offset\"\xbd\x01\n\x1a\x46\x65tchSubscriptionsResponse\x12\x44\n\rsubscriptions\x18\x01 \x03(\x0b\x32-.uprotocol.core.usubscription.v3.Subscription\x12\x1d\n\x10has_more_records\x18\x02 \x01(\x08H\x00\x88\x01\x01\x12%\n\x06status\x18\x03 \x01(\x0b\x32\x15.uprotocol.v1.UStatusB\x13\n\x11_has_more_records\"~\n\x14NotificationsRequest\x12!\n\x05topic\x18\x01 \x01(\x0b\x32\x12.uprotocol.v1.UUri\x12\x43\n\nsubscriber\x18\x02 \x01(\x0b\x32/.uprotocol.core.usubscription.v3.SubscriberInfo\"7\n\x12\x43reateTopicRequest\x12!\n\x05topic\x18\x01 \x01(\x0b\x32\x12.uprotocol.v1.UUri\":\n\x15\x44\x65precateTopicRequest\x12!\n\x05topic\x18\x01 \x01(\x0b\x32\x12.uprotocol.v1.UUri\"\x9f\x02\n\x06Update\x12!\n\x05topic\x18\x01 \x01(\x0b\x32\x12.uprotocol.v1.UUri\x12\x43\n\nsubscriber\x18\x02 \x01(\x0b\x32/.uprotocol.core.usubscription.v3.SubscriberInfo\x12\x43\n\x06status\x18\x03 \x01(\x0b\x32\x33.uprotocol.core.usubscription.v3.SubscriptionStatus\x12H\n\nattributes\x18\x04 \x01(\x0b\x32\x34.uprotocol.core.usubscription.v3.SubscribeAttributes\"\x1e\n\tResources\x12\x11\n\rsubscriptions\x10\x00\"\x1d\n\x0bPassiveMode\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\"\xd6\x02\n\x0cResetRequest\x12I\n\x06reason\x18\x01 \x01(\x0b\x32\x34.uprotocol.core.usubscription.v3.ResetRequest.ReasonH\x00\x88\x01\x01\x12/\n\x06\x62\x65\x66ore\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x01\x88\x01\x01\x1a\xb3\x01\n\x06Reason\x12G\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x39.uprotocol.core.usubscription.v3.ResetRequest.Reason.Code\x12\x14\n\x07message\x18\x02 \x01(\tH\x00\x88\x01\x01\">\n\x04\x43ode\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\x11\n\rFACTORY_RESET\x10\x01\x12\x12\n\x0e\x43ORRUPTED_DATA\x10\x02\x42\n\n\x08_messageB\t\n\x07_reasonB\t\n\x07_before2\xdd\x08\n\ruSubscription\x12~\n\tSubscribe\x12\x34.uprotocol.core.usubscription.v3.SubscriptionRequest\x1a\x35.uprotocol.core.usubscription.v3.SubscriptionResponse\"\x04\x80\x80\x19\x01\x12_\n\x0bUnsubscribe\x12\x33.uprotocol.core.usubscription.v3.UnsubscribeRequest\x1a\x15.uprotocol.v1.UStatus\"\x04\x80\x80\x19\x02\x12\x93\x01\n\x12\x46\x65tchSubscriptions\x12:.uprotocol.core.usubscription.v3.FetchSubscriptionsRequest\x1a;.uprotocol.core.usubscription.v3.FetchSubscriptionsResponse\"\x04\x80\x80\x19\x03\x12_\n\x0b\x43reateTopic\x12\x33.uprotocol.core.usubscription.v3.CreateTopicRequest\x1a\x15.uprotocol.v1.UStatus\"\x04\x80\x80\x19\x04\x12\x65\n\x0e\x44\x65precateTopic\x12\x36.uprotocol.core.usubscription.v3.DeprecateTopicRequest\x1a\x15.uprotocol.v1.UStatus\"\x04\x80\x80\x19\x05\x12n\n\x18RegisterForNotifications\x12\x35.uprotocol.core.usubscription.v3.NotificationsRequest\x1a\x15.uprotocol.v1.UStatus\"\x04\x80\x80\x19\x06\x12p\n\x1aUnregisterForNotifications\x12\x35.uprotocol.core.usubscription.v3.NotificationsRequest\x1a\x15.uprotocol.v1.UStatus\"\x04\x80\x80\x19\x07\x12\x8d\x01\n\x10\x46\x65tchSubscribers\x12\x38.uprotocol.core.usubscription.v3.FetchSubscribersRequest\x1a\x39.uprotocol.core.usubscription.v3.FetchSubscribersResponse\"\x04\x80\x80\x19\x08\x12S\n\x05Reset\x12-.uprotocol.core.usubscription.v3.ResetRequest\x1a\x15.uprotocol.v1.UStatus\"\x04\x80\x80\x19\t\x1a\x46\xe2\xf9\x18\x12\x63ore.usubscription\xe8\xf9\x18\x03\xf0\xf9\x18\x00\xf8\xf9\x18\x00\x92\xfa\x18 \x08\x80\x80\x02\x12\x12SubscriptionChange\x1a\x06UpdateBC\n+org.eclipse.uprotocol.core.usubscription.v3B\x12USubscriptionProtoP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'core.usubscription.v3.usubscription_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n+org.eclipse.uprotocol.core.usubscription.v3B\022USubscriptionProtoP\001'
  _EVENTDELIVERYCONFIG_ATTRIBUTESENTRY._options = None
  _EVENTDELIVERYCONFIG_ATTRIBUTESENTRY._serialized_options = b'8\001'
  _USUBSCRIPTION._options = None
  _USUBSCRIPTION._serialized_options = b'\342\371\030\022core.usubscription\350\371\030\003\360\371\030\000\370\371\030\000\222\372\030 \010\200\200\002\022\022SubscriptionChange\032\006Update'
  _USUBSCRIPTION.methods_by_name['Subscribe']._options = None
  _USUBSCRIPTION.methods_by_name['Subscribe']._serialized_options = b'\200\200\031\001'
  _USUBSCRIPTION.methods_by_name['Unsubscribe']._options = None
  _USUBSCRIPTION.methods_by_name['Unsubscribe']._serialized_options = b'\200\200\031\002'
  _USUBSCRIPTION.methods_by_name['FetchSubscriptions']._options = None
  _USUBSCRIPTION.methods_by_name['FetchSubscriptions']._serialized_options = b'\200\200\031\003'
  _USUBSCRIPTION.methods_by_name['CreateTopic']._options = None
  _USUBSCRIPTION.methods_by_name['CreateTopic']._serialized_options = b'\200\200\031\004'
  _USUBSCRIPTION.methods_by_name['DeprecateTopic']._options = None
  _USUBSCRIPTION.methods_by_name['DeprecateTopic']._serialized_options = b'\200\200\031\005'
  _USUBSCRIPTION.methods_by_name['RegisterForNotifications']._options = None
  _USUBSCRIPTION.methods_by_name['RegisterForNotifications']._serialized_options = b'\200\200\031\006'
  _USUBSCRIPTION.methods_by_name['UnregisterForNotifications']._options = None
  _USUBSCRIPTION.methods_by_name['UnregisterForNotifications']._serialized_options = b'\200\200\031\007'
  _USUBSCRIPTION.methods_by_name['FetchSubscribers']._options = None
  _USUBSCRIPTION.methods_by_name['FetchSubscribers']._serialized_options = b'\200\200\031\010'
  _USUBSCRIPTION.methods_by_name['Reset']._options = None
  _USUBSCRIPTION.methods_by_name['Reset']._serialized_options = b'\200\200\031\t'
  _SUBSCRIBEATTRIBUTES._serialized_start=190
  _SUBSCRIBEATTRIBUTES._serialized_end=346
  _SUBSCRIBERINFO._serialized_start=348
  _SUBSCRIBERINFO._serialized_end=436
  _SUBSCRIPTIONSTATUS._serialized_start=439
  _SUBSCRIPTIONSTATUS._serialized_end=676
  _SUBSCRIPTIONSTATUS_STATE._serialized_start=587
  _SUBSCRIPTIONSTATUS_STATE._serialized_end=676
  _EVENTDELIVERYCONFIG._serialized_start=679
  _EVENTDELIVERYCONFIG._serialized_end=889
  _EVENTDELIVERYCONFIG_ATTRIBUTESENTRY._serialized_start=818
  _EVENTDELIVERYCONFIG_ATTRIBUTESENTRY._serialized_end=889
  _SUBSCRIPTIONREQUEST._serialized_start=892
  _SUBSCRIPTIONREQUEST._serialized_end=1091
  _SUBSCRIPTIONRESPONSE._serialized_start=1094
  _SUBSCRIPTIONRESPONSE._serialized_end=1290
  _UNSUBSCRIBEREQUEST._serialized_start=1292
  _UNSUBSCRIBEREQUEST._serialized_end=1416
  _FETCHSUBSCRIBERSREQUEST._serialized_start=1418
  _FETCHSUBSCRIBERSREQUEST._serialized_end=1510
  _FETCHSUBSCRIBERSRESPONSE._serialized_start=1513
  _FETCHSUBSCRIBERSRESPONSE._serialized_end=1700
  _SUBSCRIPTION._serialized_start=1703
  _SUBSCRIPTION._serialized_end=2034
  _FETCHSUBSCRIPTIONSREQUEST._serialized_start=2037
  _FETCHSUBSCRIPTIONSREQUEST._serialized_end=2215
  _FETCHSUBSCRIPTIONSRESPONSE._serialized_start=2218
  _FETCHSUBSCRIPTIONSRESPONSE._serialized_end=2407
  _NOTIFICATIONSREQUEST._serialized_start=2409
  _NOTIFICATIONSREQUEST._serialized_end=2535
  _CREATETOPICREQUEST._serialized_start=2537
  _CREATETOPICREQUEST._serialized_end=2592
  _DEPRECATETOPICREQUEST._serialized_start=2594
  _DEPRECATETOPICREQUEST._serialized_end=2652
  _UPDATE._serialized_start=2655
  _UPDATE._serialized_end=2942
  _UPDATE_RESOURCES._serialized_start=2912
  _UPDATE_RESOURCES._serialized_end=2942
  _PASSIVEMODE._serialized_start=2944
  _PASSIVEMODE._serialized_end=2973
  _RESETREQUEST._serialized_start=2976
  _RESETREQUEST._serialized_end=3318
  _RESETREQUEST_REASON._serialized_start=3117
  _RESETREQUEST_REASON._serialized_end=3296
  _RESETREQUEST_REASON_CODE._serialized_start=3222
  _RESETREQUEST_REASON_CODE._serialized_end=3284
  _USUBSCRIPTION._serialized_start=3321
  _USUBSCRIPTION._serialized_end=4438
# @@protoc_insertion_point(module_scope)
