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


class IEdmEntityContainerElement(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @classmethod
    @property
    def containerElementKind(cls) -> typing.Type['EdmContainerElementKind']:
        return EdmContainerElementKind

    @classmethod
    @property
    def container(cls) -> typing.Type['IEdmEntityContainer']:
        return IEdmEntityContainer
    
    
    class name(
        _SchemaTypeChecker(typing.Union[none_type, str, ]),
        StrBase,
        NoneBase,
        Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[str, None, ],
            _configuration: typing.Optional[Configuration] = None,
        ) -> 'name':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        containerElementKind: typing.Union['EdmContainerElementKind', Unset] = unset,
        container: typing.Union['IEdmEntityContainer', Unset] = unset,
        name: typing.Union[name, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'IEdmEntityContainerElement':
        return super().__new__(
            cls,
            *args,
            containerElementKind=containerElementKind,
            container=container,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )

from okclient.model.edm_container_element_kind import EdmContainerElementKind
from okclient.model.i_edm_entity_container import IEdmEntityContainer
