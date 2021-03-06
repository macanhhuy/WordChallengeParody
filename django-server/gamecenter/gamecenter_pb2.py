# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='gamecenter.proto',
  package='pbauth',
  serialized_pb='\n\x10gamecenter.proto\x12\x06pbauth\"\x99\x01\n\x12GameCenterResponse\x12.\n\x05rooms\x18\x01 \x03(\x0b\x32\x1f.pbauth.GameCenterResponse.Room\x1aS\n\x04Room\x12\x0e\n\x06roomId\x18\x01 \x02(\x05\x12\x10\n\x08roomName\x18\x02 \x02(\t\x12\x15\n\rnumberOfUsers\x18\x03 \x02(\x05\x12\x12\n\ntotalSeats\x18\x04 \x02(\x05\"\x99\x01\n\x04User\x12\x0e\n\x06userId\x18\x01 \x02(\x05\x12\x10\n\x08userName\x18\x02 \x02(\t\x12/\n\nuserStatus\x18\x03 \x02(\x0e\x32\x1b.pbauth.User.UserStatusType\">\n\x0eUserStatusType\x12\n\n\x06JOINED\x10\x00\x12\r\n\tCONFIRMED\x10\x01\x12\x08\n\x04PLAY\x10\x02\x12\x07\n\x03\x45ND\x10\x03\"\xd2\x01\n\x12RoomStatusResponse\x12=\n\nroomStatus\x18\x01 \x02(\x0e\x32).pbauth.RoomStatusResponse.RoomStatusType\x12\x1b\n\x05users\x18\x02 \x03(\x0b\x32\x0c.pbauth.User\"`\n\x0eRoomStatusType\x12\x10\n\x0cJOIN_SUCCESS\x10\x00\x12\x14\n\x10ROOM_UNAVAILABLE\x10\x01\x12\x14\n\x10SEAT_UNAVAILABLE\x10\x02\x12\x10\n\x0cUSER_INVALID\x10\x03\"A\n\x11GameStatusRequest\x12\x0e\n\x06userId\x18\x01 \x02(\x05\x12\x0e\n\x06points\x18\x02 \x02(\x05\x12\x0c\n\x04time\x18\x03 \x02(\x05\"\xd7\x01\n\x12GameStatusResponse\x12=\n\nstatusList\x18\x04 \x03(\x0b\x32).pbauth.GameStatusResponse.UserGameStatus\x1a\x81\x01\n\x0eUserGameStatus\x12\x0e\n\x06userId\x18\x01 \x02(\x05\x12/\n\nuserStatus\x18\x02 \x02(\x0e\x32\x1b.pbauth.User.UserStatusType\x12\x0e\n\x06points\x18\x03 \x02(\x05\x12\x0c\n\x04time\x18\x04 \x02(\x05\x12\x10\n\x08userName\x18\x05 \x01(\t')



_USER_USERSTATUSTYPE = descriptor.EnumDescriptor(
  name='UserStatusType',
  full_name='pbauth.User.UserStatusType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='JOINED', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CONFIRMED', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='PLAY', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='END', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=276,
  serialized_end=338,
)

_ROOMSTATUSRESPONSE_ROOMSTATUSTYPE = descriptor.EnumDescriptor(
  name='RoomStatusType',
  full_name='pbauth.RoomStatusResponse.RoomStatusType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='JOIN_SUCCESS', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='ROOM_UNAVAILABLE', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SEAT_UNAVAILABLE', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='USER_INVALID', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=455,
  serialized_end=551,
)


_GAMECENTERRESPONSE_ROOM = descriptor.Descriptor(
  name='Room',
  full_name='pbauth.GameCenterResponse.Room',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='roomId', full_name='pbauth.GameCenterResponse.Room.roomId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='roomName', full_name='pbauth.GameCenterResponse.Room.roomName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='numberOfUsers', full_name='pbauth.GameCenterResponse.Room.numberOfUsers', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='totalSeats', full_name='pbauth.GameCenterResponse.Room.totalSeats', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=99,
  serialized_end=182,
)

_GAMECENTERRESPONSE = descriptor.Descriptor(
  name='GameCenterResponse',
  full_name='pbauth.GameCenterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='rooms', full_name='pbauth.GameCenterResponse.rooms', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GAMECENTERRESPONSE_ROOM, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=29,
  serialized_end=182,
)


_USER = descriptor.Descriptor(
  name='User',
  full_name='pbauth.User',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='userId', full_name='pbauth.User.userId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='userName', full_name='pbauth.User.userName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='userStatus', full_name='pbauth.User.userStatus', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _USER_USERSTATUSTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=185,
  serialized_end=338,
)


_ROOMSTATUSRESPONSE = descriptor.Descriptor(
  name='RoomStatusResponse',
  full_name='pbauth.RoomStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='roomStatus', full_name='pbauth.RoomStatusResponse.roomStatus', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='users', full_name='pbauth.RoomStatusResponse.users', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ROOMSTATUSRESPONSE_ROOMSTATUSTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=341,
  serialized_end=551,
)


_GAMESTATUSREQUEST = descriptor.Descriptor(
  name='GameStatusRequest',
  full_name='pbauth.GameStatusRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='userId', full_name='pbauth.GameStatusRequest.userId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='points', full_name='pbauth.GameStatusRequest.points', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time', full_name='pbauth.GameStatusRequest.time', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
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
  serialized_start=553,
  serialized_end=618,
)


_GAMESTATUSRESPONSE_USERGAMESTATUS = descriptor.Descriptor(
  name='UserGameStatus',
  full_name='pbauth.GameStatusResponse.UserGameStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='userId', full_name='pbauth.GameStatusResponse.UserGameStatus.userId', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='userStatus', full_name='pbauth.GameStatusResponse.UserGameStatus.userStatus', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='points', full_name='pbauth.GameStatusResponse.UserGameStatus.points', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='time', full_name='pbauth.GameStatusResponse.UserGameStatus.time', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='userName', full_name='pbauth.GameStatusResponse.UserGameStatus.userName', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=707,
  serialized_end=836,
)

_GAMESTATUSRESPONSE = descriptor.Descriptor(
  name='GameStatusResponse',
  full_name='pbauth.GameStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='statusList', full_name='pbauth.GameStatusResponse.statusList', index=0,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GAMESTATUSRESPONSE_USERGAMESTATUS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=621,
  serialized_end=836,
)

_GAMECENTERRESPONSE_ROOM.containing_type = _GAMECENTERRESPONSE;
_GAMECENTERRESPONSE.fields_by_name['rooms'].message_type = _GAMECENTERRESPONSE_ROOM
_USER.fields_by_name['userStatus'].enum_type = _USER_USERSTATUSTYPE
_USER_USERSTATUSTYPE.containing_type = _USER;
_ROOMSTATUSRESPONSE.fields_by_name['roomStatus'].enum_type = _ROOMSTATUSRESPONSE_ROOMSTATUSTYPE
_ROOMSTATUSRESPONSE.fields_by_name['users'].message_type = _USER
_ROOMSTATUSRESPONSE_ROOMSTATUSTYPE.containing_type = _ROOMSTATUSRESPONSE;
_GAMESTATUSRESPONSE_USERGAMESTATUS.fields_by_name['userStatus'].enum_type = _USER_USERSTATUSTYPE
_GAMESTATUSRESPONSE_USERGAMESTATUS.containing_type = _GAMESTATUSRESPONSE;
_GAMESTATUSRESPONSE.fields_by_name['statusList'].message_type = _GAMESTATUSRESPONSE_USERGAMESTATUS
DESCRIPTOR.message_types_by_name['GameCenterResponse'] = _GAMECENTERRESPONSE
DESCRIPTOR.message_types_by_name['User'] = _USER
DESCRIPTOR.message_types_by_name['RoomStatusResponse'] = _ROOMSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['GameStatusRequest'] = _GAMESTATUSREQUEST
DESCRIPTOR.message_types_by_name['GameStatusResponse'] = _GAMESTATUSRESPONSE

class GameCenterResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class Room(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _GAMECENTERRESPONSE_ROOM
    
    # @@protoc_insertion_point(class_scope:pbauth.GameCenterResponse.Room)
  DESCRIPTOR = _GAMECENTERRESPONSE
  
  # @@protoc_insertion_point(class_scope:pbauth.GameCenterResponse)

class User(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _USER
  
  # @@protoc_insertion_point(class_scope:pbauth.User)

class RoomStatusResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ROOMSTATUSRESPONSE
  
  # @@protoc_insertion_point(class_scope:pbauth.RoomStatusResponse)

class GameStatusRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GAMESTATUSREQUEST
  
  # @@protoc_insertion_point(class_scope:pbauth.GameStatusRequest)

class GameStatusResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  
  class UserGameStatus(message.Message):
    __metaclass__ = reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _GAMESTATUSRESPONSE_USERGAMESTATUS
    
    # @@protoc_insertion_point(class_scope:pbauth.GameStatusResponse.UserGameStatus)
  DESCRIPTOR = _GAMESTATUSRESPONSE
  
  # @@protoc_insertion_point(class_scope:pbauth.GameStatusResponse)

# @@protoc_insertion_point(module_scope)
