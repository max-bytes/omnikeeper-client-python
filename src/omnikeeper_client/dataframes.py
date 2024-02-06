import omnikeeper_client as okc
import pandas as pd
from .traitentities import (
    _get_all_traitentities,
    _bulk_replace_trait_entities_by_filter,
    _bulk_replace_trait_entities,
)

def get_all_traitentities_dataframe(ok_api_client: okc.OkApiClient, trait_name: str, layers: [str], keep_ciid_as_column: bool = False) -> pd.DataFrame:
    """
    Returns all traitentites as pandas dataframe 

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_name : str
        the name of the trait to query the data

    layers : [str]
        list containing layer_ids to search

    Returns
    -------
    pd.DataFrame
        result containing all traitentites in pandas dataframe format
    """

    data_list = _get_all_traitentities(ok_api_client, trait_id=trait_name, layers=layers)
    data_df = pd.DataFrame(data_list)
    data_df.set_index('ciid', inplace=True, drop=not keep_ciid_as_column)

    return data_df

def bulk_replace_trait_entities_by_filter_dataframe(ok_api_client: okc.OkApiClient, trait_name: str, input: pd.DataFrame, id_attributes: [str], id_relations: [str], write_layer: str, read_layers: [str] = None, filter: object = {}) -> bool:
    """
    Replaces all traitentites in a layer input data is a dataframe, it can use a filter when updating the traitentities,
    this will also delete all old trait entities, if there are any

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_name : str
        the name of the trait to query the data

    input : pd.DataFrame
        Trait entities in dataframe format

    id_attributes : [str]
        attributes to be considered as trait IDs
    
    id_relations : [str]
        ids to be considered as trait relations IDs

    write_layer : str
        the id of the layer in which the data should be added

    read_layers : [str]
        A list with ids of the layers in which the omnikeeper will look if the cis already exists

    filter : object
        a filter object can be used, default {}, example for filter object: {type: {exact: "Validator"}, context: {exact: "test"}, group: {exact: "test"} }

    Returns
    -------
    bool 
        True if the update is successful, False otherwise
    """

    input_as_dict = input.to_dict('records')
    result = _bulk_replace_trait_entities_by_filter(ok_api_client, trait_name, input_as_dict, id_attributes, id_relations, write_layer, read_layers, filter)
    return result

def bulk_replace_trait_entities_dataframe(ok_api_client: okc.OkApiClient, trait_name: str, input: pd.DataFrame, write_layer: str, read_layers: [str] = None) -> bool:
    """
    Sets all traitentities, the input is a pd.DataFrame, this will also delete all old trait entities, if there are any

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_name : str
        the name of the trait to query the data

    input : pd.DataFrame
        traitentities in dataframe format

    write_layer : str
        the id of the layer in which the data should be added

    read_layers : [str]
        A list with ids of the layers in which the omnikeeper will look if the cis already exists

    Returns
    -------
    bool 
        True if the update is successful, False otherwise
    """

    if 'ciid' not in input.columns:
        input = input.reset_index(drop=False).rename(columns={'index': 'ciid'})
    input_as_dict = input.to_dict('records')

    result = _bulk_replace_trait_entities(ok_api_client, trait_name, input_as_dict, write_layer, read_layers)
    return result