# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: filter_service/text_filter.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='filter_service/text_filter.proto',
  package='filter_transport',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n filter_service/text_filter.proto\x12\x10\x66ilter_transport\"A\n\x17SingleTextFilterRequest\x12\x14\n\x0cinput_string\x18\x01 \x01(\t\x12\x10\n\x08\x63\x61sefold\x18\x02 \x01(\x08\"1\n\x18SingleTextFilterResponse\x12\x15\n\rpassed_filter\x18\x01 \x01(\x08\",\n\x13MultiFilterResponse\x12\x15\n\rpassed_inputs\x18\x01 \x03(\t\"\xba\x02\n\x14WebpageFilterRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x11\n\x04port\x18\x02 \x01(\rH\x00\x88\x01\x01\x12\x44\n\x07headers\x18\x03 \x03(\x0b\x32\x33.filter_transport.WebpageFilterRequest.HeadersEntry\x12\x42\n\x06params\x18\x04 \x03(\x0b\x32\x32.filter_transport.WebpageFilterRequest.ParamsEntry\x12\x10\n\x08\x63\x61sefold\x18\x05 \x01(\x08\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a-\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x07\n\x05_port2\xba\x03\n\x11TextFilterService\x12g\n\x0cSingleFilter\x12).filter_transport.SingleTextFilterRequest\x1a*.filter_transport.SingleTextFilterResponse\"\x00\x12\x63\n\x0bMultiFilter\x12).filter_transport.SingleTextFilterRequest\x1a%.filter_transport.MultiFilterResponse\"\x00(\x01\x12p\n\x11MultiFilterStream\x12).filter_transport.SingleTextFilterRequest\x1a*.filter_transport.SingleTextFilterResponse\"\x00(\x01\x30\x01\x12\x65\n\rWebpageFilter\x12&.filter_transport.WebpageFilterRequest\x1a*.filter_transport.SingleTextFilterResponse\"\x00\x62\x06proto3'
)




_SINGLETEXTFILTERREQUEST = _descriptor.Descriptor(
  name='SingleTextFilterRequest',
  full_name='filter_transport.SingleTextFilterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='input_string', full_name='filter_transport.SingleTextFilterRequest.input_string', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='casefold', full_name='filter_transport.SingleTextFilterRequest.casefold', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=54,
  serialized_end=119,
)


_SINGLETEXTFILTERRESPONSE = _descriptor.Descriptor(
  name='SingleTextFilterResponse',
  full_name='filter_transport.SingleTextFilterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='passed_filter', full_name='filter_transport.SingleTextFilterResponse.passed_filter', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=121,
  serialized_end=170,
)


_MULTIFILTERRESPONSE = _descriptor.Descriptor(
  name='MultiFilterResponse',
  full_name='filter_transport.MultiFilterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='passed_inputs', full_name='filter_transport.MultiFilterResponse.passed_inputs', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=172,
  serialized_end=216,
)


_WEBPAGEFILTERREQUEST_HEADERSENTRY = _descriptor.Descriptor(
  name='HeadersEntry',
  full_name='filter_transport.WebpageFilterRequest.HeadersEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='filter_transport.WebpageFilterRequest.HeadersEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='filter_transport.WebpageFilterRequest.HeadersEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=431,
  serialized_end=477,
)

_WEBPAGEFILTERREQUEST_PARAMSENTRY = _descriptor.Descriptor(
  name='ParamsEntry',
  full_name='filter_transport.WebpageFilterRequest.ParamsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='filter_transport.WebpageFilterRequest.ParamsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='filter_transport.WebpageFilterRequest.ParamsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=479,
  serialized_end=524,
)

_WEBPAGEFILTERREQUEST = _descriptor.Descriptor(
  name='WebpageFilterRequest',
  full_name='filter_transport.WebpageFilterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='url', full_name='filter_transport.WebpageFilterRequest.url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port', full_name='filter_transport.WebpageFilterRequest.port', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='headers', full_name='filter_transport.WebpageFilterRequest.headers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='params', full_name='filter_transport.WebpageFilterRequest.params', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='casefold', full_name='filter_transport.WebpageFilterRequest.casefold', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_WEBPAGEFILTERREQUEST_HEADERSENTRY, _WEBPAGEFILTERREQUEST_PARAMSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_port', full_name='filter_transport.WebpageFilterRequest._port',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=219,
  serialized_end=533,
)

_WEBPAGEFILTERREQUEST_HEADERSENTRY.containing_type = _WEBPAGEFILTERREQUEST
_WEBPAGEFILTERREQUEST_PARAMSENTRY.containing_type = _WEBPAGEFILTERREQUEST
_WEBPAGEFILTERREQUEST.fields_by_name['headers'].message_type = _WEBPAGEFILTERREQUEST_HEADERSENTRY
_WEBPAGEFILTERREQUEST.fields_by_name['params'].message_type = _WEBPAGEFILTERREQUEST_PARAMSENTRY
_WEBPAGEFILTERREQUEST.oneofs_by_name['_port'].fields.append(
  _WEBPAGEFILTERREQUEST.fields_by_name['port'])
_WEBPAGEFILTERREQUEST.fields_by_name['port'].containing_oneof = _WEBPAGEFILTERREQUEST.oneofs_by_name['_port']
DESCRIPTOR.message_types_by_name['SingleTextFilterRequest'] = _SINGLETEXTFILTERREQUEST
DESCRIPTOR.message_types_by_name['SingleTextFilterResponse'] = _SINGLETEXTFILTERRESPONSE
DESCRIPTOR.message_types_by_name['MultiFilterResponse'] = _MULTIFILTERRESPONSE
DESCRIPTOR.message_types_by_name['WebpageFilterRequest'] = _WEBPAGEFILTERREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SingleTextFilterRequest = _reflection.GeneratedProtocolMessageType('SingleTextFilterRequest', (_message.Message,), {
  'DESCRIPTOR' : _SINGLETEXTFILTERREQUEST,
  '__module__' : 'filter_service.text_filter_pb2'
  # @@protoc_insertion_point(class_scope:filter_transport.SingleTextFilterRequest)
  })
_sym_db.RegisterMessage(SingleTextFilterRequest)

SingleTextFilterResponse = _reflection.GeneratedProtocolMessageType('SingleTextFilterResponse', (_message.Message,), {
  'DESCRIPTOR' : _SINGLETEXTFILTERRESPONSE,
  '__module__' : 'filter_service.text_filter_pb2'
  # @@protoc_insertion_point(class_scope:filter_transport.SingleTextFilterResponse)
  })
_sym_db.RegisterMessage(SingleTextFilterResponse)

MultiFilterResponse = _reflection.GeneratedProtocolMessageType('MultiFilterResponse', (_message.Message,), {
  'DESCRIPTOR' : _MULTIFILTERRESPONSE,
  '__module__' : 'filter_service.text_filter_pb2'
  # @@protoc_insertion_point(class_scope:filter_transport.MultiFilterResponse)
  })
_sym_db.RegisterMessage(MultiFilterResponse)

WebpageFilterRequest = _reflection.GeneratedProtocolMessageType('WebpageFilterRequest', (_message.Message,), {

  'HeadersEntry' : _reflection.GeneratedProtocolMessageType('HeadersEntry', (_message.Message,), {
    'DESCRIPTOR' : _WEBPAGEFILTERREQUEST_HEADERSENTRY,
    '__module__' : 'filter_service.text_filter_pb2'
    # @@protoc_insertion_point(class_scope:filter_transport.WebpageFilterRequest.HeadersEntry)
    })
  ,

  'ParamsEntry' : _reflection.GeneratedProtocolMessageType('ParamsEntry', (_message.Message,), {
    'DESCRIPTOR' : _WEBPAGEFILTERREQUEST_PARAMSENTRY,
    '__module__' : 'filter_service.text_filter_pb2'
    # @@protoc_insertion_point(class_scope:filter_transport.WebpageFilterRequest.ParamsEntry)
    })
  ,
  'DESCRIPTOR' : _WEBPAGEFILTERREQUEST,
  '__module__' : 'filter_service.text_filter_pb2'
  # @@protoc_insertion_point(class_scope:filter_transport.WebpageFilterRequest)
  })
_sym_db.RegisterMessage(WebpageFilterRequest)
_sym_db.RegisterMessage(WebpageFilterRequest.HeadersEntry)
_sym_db.RegisterMessage(WebpageFilterRequest.ParamsEntry)


_WEBPAGEFILTERREQUEST_HEADERSENTRY._options = None
_WEBPAGEFILTERREQUEST_PARAMSENTRY._options = None

_TEXTFILTERSERVICE = _descriptor.ServiceDescriptor(
  name='TextFilterService',
  full_name='filter_transport.TextFilterService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=536,
  serialized_end=978,
  methods=[
  _descriptor.MethodDescriptor(
    name='SingleFilter',
    full_name='filter_transport.TextFilterService.SingleFilter',
    index=0,
    containing_service=None,
    input_type=_SINGLETEXTFILTERREQUEST,
    output_type=_SINGLETEXTFILTERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MultiFilter',
    full_name='filter_transport.TextFilterService.MultiFilter',
    index=1,
    containing_service=None,
    input_type=_SINGLETEXTFILTERREQUEST,
    output_type=_MULTIFILTERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MultiFilterStream',
    full_name='filter_transport.TextFilterService.MultiFilterStream',
    index=2,
    containing_service=None,
    input_type=_SINGLETEXTFILTERREQUEST,
    output_type=_SINGLETEXTFILTERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='WebpageFilter',
    full_name='filter_transport.TextFilterService.WebpageFilter',
    index=3,
    containing_service=None,
    input_type=_WEBPAGEFILTERREQUEST,
    output_type=_SINGLETEXTFILTERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEXTFILTERSERVICE)

DESCRIPTOR.services_by_name['TextFilterService'] = _TEXTFILTERSERVICE

# @@protoc_insertion_point(module_scope)
