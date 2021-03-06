# coding: utf-8

"""
    Landscape omnikeeper REST API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from okclient.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class AttributeValueDTO(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @classmethod
    @property
    def type(cls) -> typing.Type['AttributeValueType']:
        return AttributeValueType
    isArray = BoolSchema
    
    
    class values(
        ListSchema
    ):
        _items = StrSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        type: typing.Union['AttributeValueType', Unset] = unset,
        isArray: typing.Union[isArray, Unset] = unset,
        values: typing.Union[values, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'AttributeValueDTO':
        return super().__new__(
            cls,
            *args,
            type=type,
            isArray=isArray,
            values=values,
            _configuration=_configuration,
            **kwargs,
        )

from okclient.model.attribute_value_type import AttributeValueType
