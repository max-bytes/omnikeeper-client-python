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


class IEdmEntityContainer(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    
    class elements(
        _SchemaTypeChecker(typing.Union[tuple, none_type, ]),
        ListBase,
        NoneBase,
        Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[list, tuple, None, ],
            _configuration: typing.Optional[Configuration] = None,
        ) -> 'elements':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )

    @classmethod
    @property
    def schemaElementKind(cls) -> typing.Type['EdmSchemaElementKind']:
        return EdmSchemaElementKind
    
    
    class namespace(
        _SchemaTypeChecker(typing.Union[none_type, str, ]),
        StrBase,
        NoneBase,
        Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[str, None, ],
            _configuration: typing.Optional[Configuration] = None,
        ) -> 'namespace':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
            )
    
    
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
        elements: typing.Union[elements, Unset] = unset,
        schemaElementKind: typing.Union['EdmSchemaElementKind', Unset] = unset,
        namespace: typing.Union[namespace, Unset] = unset,
        name: typing.Union[name, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'IEdmEntityContainer':
        return super().__new__(
            cls,
            *args,
            elements=elements,
            schemaElementKind=schemaElementKind,
            namespace=namespace,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )

from okclient.model.edm_schema_element_kind import EdmSchemaElementKind
from okclient.model.i_edm_entity_container_element import IEdmEntityContainerElement
