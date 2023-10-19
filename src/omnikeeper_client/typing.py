from typing import (
    List,
    Dict,
    Any,
)

import json

ATTRIBUTETYPE_TEXT = "TEXT"
ATTRIBUTETYPE_MULTILINE_TEXT = "MULTILINE_TEXT"
ATTRIBUTETYPE_INTEGER = "INTEGER"
ATTRIBUTETYPE_DOUBLE = "DOUBLE"
ATTRIBUTETYPE_BOOLEAN = "BOOLEAN"
ATTRIBUTETYPE_JSON = "JSON"

_TYPEMAP_FROM_MERGEDATTRIBUTE = {
    ATTRIBUTETYPE_TEXT: str,
    ATTRIBUTETYPE_MULTILINE_TEXT: str,
    ATTRIBUTETYPE_INTEGER: int,
    ATTRIBUTETYPE_DOUBLE: float,
    ATTRIBUTETYPE_BOOLEAN: bool,
    ATTRIBUTETYPE_JSON: Dict,
}

_TYPECONVERSIONMAP_FROM_MERGEDATTRIBUTE = {
    ATTRIBUTETYPE_TEXT: str,
    ATTRIBUTETYPE_MULTILINE_TEXT: str,
    ATTRIBUTETYPE_INTEGER: int,
    ATTRIBUTETYPE_DOUBLE: float,
    ATTRIBUTETYPE_BOOLEAN: bool,
    ATTRIBUTETYPE_JSON: json.loads,
}

def attributevalue_to_pythonvalue(attribute_value: Dict[str, Any]) -> Any:
    """converts a single merged attribute value to a native python value of equivalent type
    
    Parameters
    ----------
    
    attribute_value : Dict[str, Any]
        attribute to convert, expects dict containing {"type": ... , "isArray": ... , "values": ... }

    Returns
    -------
    Any
        attributevalue converted to native python type
    """
    type = attribute_value['type']
    values = attribute_value['values']

    if type in _TYPECONVERSIONMAP_FROM_MERGEDATTRIBUTE:
        if attribute_value['isArray']:
            return [_TYPECONVERSIONMAP_FROM_MERGEDATTRIBUTE[type](v) for v in values]
        else:
            return _TYPECONVERSIONMAP_FROM_MERGEDATTRIBUTE[type](values[0])

    else:
        raise NotImplementedError(f"type conversion for merged attribute type {type} not implemented")

def attributes_to_dict(attributes: List[Dict[str, Any]]) -> Dict[str, Any]:
    """converts a mergedAttributes list to native python attribute dictionary

    Parameters
    ----------
    attributes: List[Dict[str, Any]] list of attributes

    Returns
    -------
        Dict[str, Any]: attribute key, value dict
    """
    return {inner['attribute']['name']: attributevalue_to_pythonvalue(inner['attribute']['value']) for inner in attributes}
