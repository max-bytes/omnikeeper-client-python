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


class EdmExpressionKind(
    _SchemaEnumMaker(
        enum_value_to_name={
            "None": "NONE",
            "BinaryConstant": "BINARYCONSTANT",
            "BooleanConstant": "BOOLEANCONSTANT",
            "DateTimeOffsetConstant": "DATETIMEOFFSETCONSTANT",
            "DecimalConstant": "DECIMALCONSTANT",
            "FloatingConstant": "FLOATINGCONSTANT",
            "GuidConstant": "GUIDCONSTANT",
            "IntegerConstant": "INTEGERCONSTANT",
            "StringConstant": "STRINGCONSTANT",
            "DurationConstant": "DURATIONCONSTANT",
            "Null": "NULL",
            "Record": "RECORD",
            "Collection": "COLLECTION",
            "Path": "PATH",
            "If": "IF",
            "Cast": "CAST",
            "IsType": "ISTYPE",
            "FunctionApplication": "FUNCTIONAPPLICATION",
            "LabeledExpressionReference": "LABELEDEXPRESSIONREFERENCE",
            "Labeled": "LABELED",
            "PropertyPath": "PROPERTYPATH",
            "NavigationPropertyPath": "NAVIGATIONPROPERTYPATH",
            "DateConstant": "DATECONSTANT",
            "TimeOfDayConstant": "TIMEOFDAYCONSTANT",
            "EnumMember": "ENUMMEMBER",
            "AnnotationPath": "ANNOTATIONPATH",
        }
    ),
    StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @classmethod
    @property
    def NONE(cls):
        return cls("None")
    
    @classmethod
    @property
    def BINARYCONSTANT(cls):
        return cls("BinaryConstant")
    
    @classmethod
    @property
    def BOOLEANCONSTANT(cls):
        return cls("BooleanConstant")
    
    @classmethod
    @property
    def DATETIMEOFFSETCONSTANT(cls):
        return cls("DateTimeOffsetConstant")
    
    @classmethod
    @property
    def DECIMALCONSTANT(cls):
        return cls("DecimalConstant")
    
    @classmethod
    @property
    def FLOATINGCONSTANT(cls):
        return cls("FloatingConstant")
    
    @classmethod
    @property
    def GUIDCONSTANT(cls):
        return cls("GuidConstant")
    
    @classmethod
    @property
    def INTEGERCONSTANT(cls):
        return cls("IntegerConstant")
    
    @classmethod
    @property
    def STRINGCONSTANT(cls):
        return cls("StringConstant")
    
    @classmethod
    @property
    def DURATIONCONSTANT(cls):
        return cls("DurationConstant")
    
    @classmethod
    @property
    def NULL(cls):
        return cls("Null")
    
    @classmethod
    @property
    def RECORD(cls):
        return cls("Record")
    
    @classmethod
    @property
    def COLLECTION(cls):
        return cls("Collection")
    
    @classmethod
    @property
    def PATH(cls):
        return cls("Path")
    
    @classmethod
    @property
    def IF(cls):
        return cls("If")
    
    @classmethod
    @property
    def CAST(cls):
        return cls("Cast")
    
    @classmethod
    @property
    def ISTYPE(cls):
        return cls("IsType")
    
    @classmethod
    @property
    def FUNCTIONAPPLICATION(cls):
        return cls("FunctionApplication")
    
    @classmethod
    @property
    def LABELEDEXPRESSIONREFERENCE(cls):
        return cls("LabeledExpressionReference")
    
    @classmethod
    @property
    def LABELED(cls):
        return cls("Labeled")
    
    @classmethod
    @property
    def PROPERTYPATH(cls):
        return cls("PropertyPath")
    
    @classmethod
    @property
    def NAVIGATIONPROPERTYPATH(cls):
        return cls("NavigationPropertyPath")
    
    @classmethod
    @property
    def DATECONSTANT(cls):
        return cls("DateConstant")
    
    @classmethod
    @property
    def TIMEOFDAYCONSTANT(cls):
        return cls("TimeOfDayConstant")
    
    @classmethod
    @property
    def ENUMMEMBER(cls):
        return cls("EnumMember")
    
    @classmethod
    @property
    def ANNOTATIONPATH(cls):
        return cls("AnnotationPath")
