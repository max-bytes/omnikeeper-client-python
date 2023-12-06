from gql import gql
import graphql
from graphql import GraphQLType
from gql.dsl import DSLQuery, DSLVariableDefinitions, DSLSchema, dsl_gql
from dateutil import parser
import datetime
import omnikeeper_client as okc
from typing import List, Dict, Any

def _is_relation_field(type: GraphQLType) -> bool:
    """
    Checks if field is a relation. A typical relation field looks like this:
    GraphQLList <GraphQLObjectType 'TEWrapper_tsa_cmdb__interface'>> or
    GraphQLList <GraphQLObjectType 'RelatedCIType'>
    Parameters
    ----------
    type : GraphQLType
        The type of the field
    Returns
    -------
    bool
        True if field is a relation, False otherwise
    """
    if not graphql.type.is_list_type(type):
        return False
    list_type = graphql.type.assert_list_type(type)
    if not graphql.type.is_object_type(list_type.of_type): # TODO: is this enough?
        return False
    return True

def _is_non_trait_hinted_relation_field(type: GraphQLType) -> bool:
    """
    Checks if field of a non-trait hinted is a realtion
    Parameters
    ----------
    type : GraphQLType
        The GraphQLType to check
    Returns
    -------
    bool
        True if the type is a non-trait hinted relation field, False otherwise
    """
    if not graphql.type.is_list_type(type):
        return False
    list_type = graphql.type.assert_list_type(type)
    if not graphql.type.is_object_type(list_type.of_type):
        return False
    if list_type.of_type.name != 'RelatedCIType':
        return False
    return True

def _get_escaped_trait_name(name: str) -> str:
    """
    Creates the escaped trait name
    Parameters
    ----------
    name : str
        the trait name
    Returns
    -------
    str
        the escaped trait name
    """
    return str.replace(name, '.', '__')

def _get_prefixed_trait_name(name: str) -> str:
    """
    Creates the prefixed trait name with m prefix
    Parameters
    ----------
    name : str
        the trait name
    Returns
    -------
    str
        the prefixed trait name with m prefix
    """
    if name.startswith("_"):
        return f"m{name}"
    return name

def get_latest_trait_change(ok_api_client: okc.OkApiClient, trait_name: str, layers: [str]) -> datetime.datetime:
    """
    Returns the timestamp of the latest change for the provided trait

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
    timestamp : datetime
        timestamp of the latest trait data change
    """

    client = ok_api_client._get_graphql_client()
    with client as session:
        ds = DSLSchema(client.schema)

        escaped_trait_name = _get_escaped_trait_name(trait_name)
        prefixed_escaped_trait_name = _get_prefixed_trait_name(escaped_trait_name)
        tetType = getattr(ds.TraitEntitiesType, prefixed_escaped_trait_name)
        dsl_root_type = getattr(ds, f"TERoot_{escaped_trait_name}")
        var = DSLVariableDefinitions()
        raw_query = DSLQuery(
                    ds.GraphQLQueryRoot.traitEntities.args(layers=var.layers).select(
                        tetType.select(
                            dsl_root_type.latestChangeAll.select(
                                ds.ChangesetType.timestamp
                            )
                        )
                    )
                )
        raw_query.variable_definitions = var
        query = dsl_gql(raw_query)

        result = session.execute(query, variable_values={"layers": layers})

        timestamp_str = result['traitEntities'][prefixed_escaped_trait_name]['latestChangeAll']['timestamp']
        timestamp = parser.parse(timestamp_str)
        return timestamp
 
def _get_all_traitentities(ok_api_client: okc.OkApiClient, trait_name: str, layers: [str]) -> List[Dict[str,Any]]:
    """
    Internal method used to fetch all traitentites

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
    List[Dict[str,Any]]
        result containing all traitentites
    """
    
    client = ok_api_client._get_graphql_client()
    with client as session:
        ds = DSLSchema(client.schema)

        escaped_trait_name = _get_escaped_trait_name(trait_name)
        prefixed_escaped_trait_name = _get_prefixed_trait_name(escaped_trait_name)

        tetType = getattr(ds.TraitEntitiesType, prefixed_escaped_trait_name)
        dsl_type = getattr(ds, f"TE_{escaped_trait_name}")
        dsl_root_type = getattr(ds, f"TERoot_{escaped_trait_name}")
        dsl_wrapper_type = getattr(ds, f"TEWrapper_{escaped_trait_name}")
        entity_fields = list(map(lambda t: getattr(dsl_type, t[0]), filter(lambda t: not _is_relation_field(t[1].type), dsl_type._type.fields.items())))

        var = DSLVariableDefinitions()
        raw_query = DSLQuery(
                    ds.GraphQLQueryRoot.traitEntities.args(layers=var.layers).select(
                        tetType.select(
                            dsl_root_type.all.select(
                                dsl_wrapper_type.ciid,
                                dsl_wrapper_type.entity.select(*entity_fields)
                            )
                        )
                    )
                )
        raw_query.variable_definitions = var
        query = dsl_gql(raw_query)

        result = session.execute(query, variable_values={"layers": layers})

        data_list = result['traitEntities'][prefixed_escaped_trait_name]['all']
        for data in data_list:
            data.update(data.pop('entity'))

        return data_list
    
def _bulk_replace_trait_entities_by_filter(ok_api_client: okc.OkApiClient, trait_name: str, input: List[Dict[str,Any]], id_attributes: [str], id_relations: [str], write_layer: str, read_layers: [str] = None, filter: object = {}) -> bool:
    """
    Internal method used to replace all traitentites in a layer, it can use a filter when updating the trait entities,
    this will also delete all old trait entities, if there are any

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_name : str
        the name of the trait to query the data

    input : List[Dict[str,Any]]
        Trait entities as list of dictionaries

    id_attributes : [str]
        attributes to be considered as trait IDs
    
    id_relations : [str]
        ids to be considered as trait relations IDs

    write_layer : str
        the name of the layer in which the data should be added

    read_layers : [str]
        A list with names of the layers in which the omnikeeper will look if trait entities already exist

    filter : object
        a filter object can be used, default {}, example for filter object: {type: {exact: "Validator"}, context: {exact: "test"}, group: {exact: "test"} }

    Returns
    -------
    bool 
        True if the update is successful, False otherwise
    """
    
    escaped_trait_name = _get_escaped_trait_name(trait_name)
    prefixed_escaped_trait_name = _get_prefixed_trait_name(escaped_trait_name)

    query = gql(f"""
        mutation($readLayers: [String]!, $writeLayer: String!, $idAttributes: [String!]!, $idRelations: [String!]!, $filter: TE_filter_Input_{escaped_trait_name}!, $input: [TE_Upsert_Input_{escaped_trait_name}]!) {{
        bulkReplaceByFilter_{prefixed_escaped_trait_name}(
            layers: $readLayers
            writeLayer: $writeLayer
            filter: $filter
            input: $input
            idAttributes: $idAttributes
            idRelations: $idRelations
        ) {{
            success
        }}
        }}
        """)
        
    if read_layers is None:
        read_layers = [write_layer]

    result = ok_api_client.execute_graphql(query, variables=dict(
        writeLayer=write_layer, 
        readLayers=read_layers, 
        idAttributes=id_attributes,
        idRelations=id_relations,
        filter=filter,
        input=input
        ))

    return result[f"bulkReplaceByFilter_{prefixed_escaped_trait_name}"]["success"]

def _bulk_replace_trait_entities(ok_api_client: okc.OkApiClient, trait_name: str, input: List[Dict[str,Any]], write_layer: str, read_layers: [str] = None) -> bool:
    """
    Internal method that sets all trait entities, this will also delete all old trait entities, if there are any

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_name : str
        the name of the trait to query the data

    input : List[Dict[str,Any]]
        The cis items which will be added to the layer

    write_layer : str
        the name of the layer in which the data should be added

    read_layers : [str]
        A list with names of the layers in which the omnikeeper will look if the cis already exists

    Returns
    -------
    bool 
        True if the update is successful, False otherwise
    """
    escaped_trait_name = _get_escaped_trait_name(trait_name)
    prefixed_escaped_trait_name = _get_prefixed_trait_name(escaped_trait_name)

    query = gql(f"""
        mutation($readLayers: [String]!, $writeLayer: String!, $input: [TE_CIID_And_Upsert_Attributes_Only_Input_{escaped_trait_name}]!) {{
        bulkReplace_{prefixed_escaped_trait_name}(
            layers: $readLayers
            writeLayer: $writeLayer
            input: $input
        ) {{
            success
        }}
        }}
        """)
        
    final_input = [{"ciid": d["ciid"], "attributes": {k: v for k, v in d.items() if k != "ciid"}} for d in input]
        
    if read_layers is None:
        read_layers = [write_layer]
    result = ok_api_client.execute_graphql(query, variables=dict(
        writeLayer=write_layer, 
        readLayers=read_layers, 
        input=final_input
        ))

    return result[f"bulkReplace_{prefixed_escaped_trait_name}"]["success"]

def bulk_replace_trait_entities_by_filter_list(ok_api_client: okc.OkApiClient, trait_name: str, input: List[Dict[str,Any]], id_attributes: [str], id_relations: [str], write_layer: str, read_layers: [str] = None, filter: object = {}) -> bool:
    """
    Replaces all traitentites in a layer, it can use a filter when updating the trait entities,
    this will also delete all old trait entities, if there are any

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_name : str
        the name of the trait to query the data

    input : List[Dict[str,Any]]
        Trait entities as list of dictionaries

    id_attributes : [str]
        attributes to be considered as trait IDs
    
    id_relations : [str]
        ids to be considered as trait relations IDs

    write_layer : str
        the name of the layer in which the data should be added

    read_layers : [str]
        A list with names of the layers in which the omnikeeper will look if trait entities already exist

    filter : object
        a filter object can be used, default {}, example for filter object: {type: {exact: "Validator"}, context: {exact: "test"}, group: {exact: "test"} }

    Returns
    -------
    bool 
        True if the update is successful, False otherwise
    """
    result = _bulk_replace_trait_entities_by_filter(ok_api_client, trait_name, input, id_attributes, id_relations, write_layer, read_layers, filter)
    return result

def bulk_replace_trait_entities_list(ok_api_client: okc.OkApiClient, trait_name: str, input: List[Dict[str,Any]], write_layer: str, read_layers: [str] = None) -> bool:
    """
    Sets all trait entities, this will also delete all old trait entities, if there are any

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_name : str
        the name of the trait to query the data

    input : List[Dict[str,Any]]
        The cis items which will be added to the layer

    write_layer : str
        the name of the layer in which the data should be added

    read_layers : [str]
        A list with names of the layers in which the omnikeeper will look if the cis already exists

    Returns
    -------
    bool 
        True if the update is successful, False otherwise
    """
    result = _bulk_replace_trait_entities(ok_api_client, trait_name, input, write_layer, read_layers)
    return result

def get_all_traitentities_list(ok_api_client: okc.OkApiClient, trait_name: str, layers: [str]) -> List[Dict[str,Any]]:
    """
    Returns all traitentites

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
    List[Dict[str,Any]]
        result containing all traitentites
    """
    
    trait_entities = _get_all_traitentities(ok_api_client, trait_name, layers)
    return trait_entities