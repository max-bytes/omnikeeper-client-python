import omnikeeper_client as okc
from .traitentities import (
    _get_all_traitentities,
    _bulk_replace_trait_entities
)
from pydantic import BaseModel, TypeAdapter, PlainSerializer
from typing_extensions import Annotated
import uuid
from typing import (
    List,
    TypeVar
)

SerializableUUID = Annotated[uuid.UUID, PlainSerializer(lambda x: str(x), return_type=str)]

# experimental ok trait hints
class AttributeName:
    def __init__(self, name: str):
        self.name = name
class AttributeOptional:
    def __init__(self, optional: bool = True):
        self.optional = optional
class TypeHint:
    def __init__(self, type: str, is_array: bool = False):
        self.type = type
        self.is_array = is_array


T = TypeVar("T", bound=BaseModel)

def get_all_traitentities_pydantic(ok_api_client: okc.OkApiClient, trait_name: str, ta: TypeAdapter, layers: List[str]) -> List[T]:
    """
    Returns all traitentites as pydantic objects 

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_name : str
        the name of the trait to query the data

    ta : TypeAdapter
        a pydantic Type Adapter for the type List[T] where T is the model's type

    layers : List[str]
        list containing layer_ids to search

    Returns
    -------
    List[T]
        list of pydantic model objects
    """

    data = _get_all_traitentities(ok_api_client, trait_id=trait_name, layers=layers)
    m = ta.validate_python(data, strict=False) # NOTE: consider using strict mode! But UUID matching requires non-strict without further changes
    return m


def bulk_replace_trait_entities_pydantic(ok_api_client: okc.OkApiClient, trait_name: str, input: List[T], write_layer: str, read_layers: List[str] = None) -> bool:
    """
    Sets all traitentities, the input is a list of pydantic model objects, this will also delete all old trait entities, if there are any

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_name : str
        the name of the trait to query the data

    input : List[T]
        traitentities as a list of pydantic model objects, must contain ciid field

    write_layer : str
        the id of the layer in which the data should be added

    read_layers : [str]
        A list with ids of the layers in which the omnikeeper will look if the cis already exists

    Returns
    -------
    bool 
        True if the update is successful, False otherwise
    """

    input_as_dict = (item.model_dump() for item in input)
    result = _bulk_replace_trait_entities(ok_api_client, trait_name, input_as_dict, write_layer, read_layers)
    return result
