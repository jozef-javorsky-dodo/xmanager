# Copyright 2017 The Bazel Authors. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pyformat: disable
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# pylint: skip-file
# source: src/main/protobuf/option_filters.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&src/main/protobuf/option_filters.proto\x12\x07options*\xea\x02\n\x0fOptionEffectTag\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05NO_OP\x10\x01\x12\x1b\n\x17LOSES_INCREMENTAL_STATE\x10\x02\x12\x12\n\x0e\x43HANGES_INPUTS\x10\x03\x12\x13\n\x0f\x41\x46\x46\x45\x43TS_OUTPUTS\x10\x04\x12\x18\n\x14\x42UILD_FILE_SEMANTICS\x10\x05\x12 \n\x1c\x42\x41ZEL_INTERNAL_CONFIGURATION\x10\x06\x12\x18\n\x14LOADING_AND_ANALYSIS\x10\x07\x12\r\n\tEXECUTION\x10\x08\x12\'\n#HOST_MACHINE_RESOURCE_OPTIMIZATIONS\x10\t\x12\x15\n\x11\x45\x41GERNESS_TO_EXIT\x10\n\x12\x14\n\x10\x42\x41ZEL_MONITORING\x10\x0b\x12\x13\n\x0fTERMINAL_OUTPUT\x10\x0c\x12\x18\n\x14\x41\x43TION_COMMAND_LINES\x10\r\x12\x0f\n\x0bTEST_RUNNER\x10\x0e*\xb2\x01\n\x11OptionMetadataTag\x12\x10\n\x0c\x45XPERIMENTAL\x10\x00\x12\x17\n\x13INCOMPATIBLE_CHANGE\x10\x01\x12\x0e\n\nDEPRECATED\x10\x02\x12\n\n\x06HIDDEN\x10\x03\x12\x0c\n\x08INTERNAL\x10\x04\x12\x1b\n\x17\x45XPLICIT_IN_OUTPUT_PATH\x10\x06\"\x04\x08\x05\x10\x05*%TRIGGERED_BY_ALL_INCOMPATIBLE_CHANGESB*\n(com.google.devtools.common.options.protob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'src.main.protobuf.option_filters_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(com.google.devtools.common.options.proto'
  _OPTIONEFFECTTAG._serialized_start=52
  _OPTIONEFFECTTAG._serialized_end=414
  _OPTIONMETADATATAG._serialized_start=417
  _OPTIONMETADATATAG._serialized_end=595
# @@protoc_insertion_point(module_scope)
