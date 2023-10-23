from typing import (
    List,
    Dict,
    Any,
    Optional,
)

import json
import uuid

ATTRIBUTETYPE_TEXT = "TEXT"
ATTRIBUTETYPE_MULTILINE_TEXT = "MULTILINE_TEXT"
ATTRIBUTETYPE_INTEGER = "INTEGER"
ATTRIBUTETYPE_DOUBLE = "DOUBLE"
ATTRIBUTETYPE_BOOLEAN = "BOOLEAN"
ATTRIBUTETYPE_JSON = "JSON"

_TYPECONVERSIONMAP_FROM_MERGEDATTRIBUTE = {
    ATTRIBUTETYPE_TEXT: str,
    ATTRIBUTETYPE_MULTILINE_TEXT: str,
    ATTRIBUTETYPE_INTEGER: int,
    ATTRIBUTETYPE_DOUBLE: float,
    ATTRIBUTETYPE_BOOLEAN: bool,
    ATTRIBUTETYPE_JSON: json.loads,
}

# TODO add more convert functions other TEXT and integer, remove lambda and write str directly if wanted
_TYPECONVERSIONMAP_TO_MERGEDATTRIBUTE = {
    ATTRIBUTETYPE_TEXT: lambda x: str(x),
    ATTRIBUTETYPE_MULTILINE_TEXT: lambda x: str(x),
    ATTRIBUTETYPE_INTEGER: lambda x: str(x),
    ATTRIBUTETYPE_DOUBLE: lambda x: str(x),
    ATTRIBUTETYPE_BOOLEAN: bool,
    ATTRIBUTETYPE_JSON: json.dumps,
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
    attributes: List[Dict[str, Any]] 
        list of attributes

    Returns
    -------
    Dict[str, Any]
        attribute key, value dict
    """
    return {attribute['attribute']['name']: attributevalue_to_pythonvalue(attribute['attribute']['value']) for attribute in attributes}

def _detect_single_attributetype(value : Any) -> str:
    """tries to transform any given legacy value to attribute type if unsure TEXT type is returned
    
    Parameters
    ----------
    value : Any
        the value to be inspected

    Returns
    -------
    str
        the corresponding ATTRIBUTETYPE
    """

    # print (type(value))

    # a simple plan
    simple_types = {
        int : ATTRIBUTETYPE_INTEGER,
        float : ATTRIBUTETYPE_DOUBLE,
        bool : ATTRIBUTETYPE_BOOLEAN,
        dict : ATTRIBUTETYPE_JSON,
        list : ATTRIBUTETYPE_JSON, # this is need for List of List
    }
    if type(value) in simple_types:
        return simple_types[type(value)]
    
    # string is a bit more complex as we look out for multiline signs
    if type(value) == str:
        if "\n" in value:
            return ATTRIBUTETYPE_MULTILINE_TEXT
        if "\r" in value:
            return ATTRIBUTETYPE_MULTILINE_TEXT
        
        return ATTRIBUTETYPE_TEXT
    
    return ATTRIBUTETYPE_TEXT

def dict_to_attributes(ciid : uuid.UUID, native_attribute_dict : Dict[str, Any], type_hints : Dict[str, str] = {}, type_hints_isarray : Dict[str, bool] = {}) -> List[Dict[str, Any]]:
    """converts a native python attribute dictionary to a omnikeeper mergedAttributes list
    
    Parameters
    ----------
    ciid : uuid.UUID
        ciid to write attributes for 

    native_attribute_dict : Dict[str, Any] 
        attribute key, value dict  

    type_hints : Dict[str, str]
        an optional hint map to override types and not use autodetect

    type_hints_isarray : Dict[str, bool]
        an optional hint map to override isArray and not use autodetect        

    Returns
    -------
    List[Dict[str, Any]]
        list of attributes
    """

    attributes = []

    for k, v in native_attribute_dict.items():
        # detect list/array
        if k in type_hints_isarray:
            is_array = type_hints_isarray[k]
        else:
            is_array = (type(v) == list)

        # detect type
        if k in type_hints:
            attr_type = type_hints[k]
        else:
            if is_array:
                if len(v) > 0:
                    attr_type = _detect_single_attributetype(v[0])
                else:
                    # we don not know it without a hint or at least one item
                    attr_type = ATTRIBUTETYPE_TEXT

            else:
                attr_type = _detect_single_attributetype(v)

        if is_array:
            attr_values = [_TYPECONVERSIONMAP_TO_MERGEDATTRIBUTE[attr_type](item) for item in v]
        else:
            attr_values = [_TYPECONVERSIONMAP_TO_MERGEDATTRIBUTE[attr_type](v)]

        attributes.append({
            "ci": str(ciid),
            "name": k,
            "value": {
                "type": attr_type,
                "isArray": is_array,
                "values": attr_values,
            }
        })

    return attributes
