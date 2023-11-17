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
    is_relation = False
    if graphql.type.is_list_type(type):
        is_relation = True
    list_type = graphql.type.assert_list_type(type)
    if graphql.type.is_object_type(list_type.of_type): # TODO: is this enough?
        is_relation = True
    return is_relation

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
    is_relation = False
    if graphql.type.is_list_type(type):
        is_relation = True
    list_type = graphql.type.assert_list_type(type)
    if graphql.type.is_object_type(list_type.of_type):
        is_relation = True
    if list_type.of_type.name == 'RelatedCIType':
        is_relation = True
    return is_relation

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
    # TODO we should find a way how to get the schema when using the new okc.OkApiClient
    # ds = DSLSchema(client.schema)

    # NOTE check this
    ds = DSLSchema(ok_api_client.get_schema())

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
    result = ok_api_client.execute_graphql(query, variables={"layers": layers})
    timestamp_str = result['traitEntities'][prefixed_escaped_trait_name]['latestChangeAll']['timestamp']
    timestamp = parser.parse(timestamp_str)
    return timestamp
 
def get_all_traitentities(ok_api_client: okc.OkApiClient, trait_name: str, layers: [str], keep_ciid_as_column: bool = False) -> List[Dict[str,Any]]:
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

    keep_ciid_as_column : bool
        True if ciid should be returned in result, False otherwise

    Returns
    -------
    List[Dict[str,Any]]
        result containing all traitentites
    """
    
    # ds = DSLSchema(client.schema)
    ds = DSLSchema(ok_api_client.get_schema())

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

    result = ok_api_client.execute_graphql(query, variables={"layers": layers})

    data_list = result['traitEntities'][prefixed_escaped_trait_name]['all']
    for data in data_list:
        data.update(data.pop('entity'))

    return data_list

def get_trait_relation(ok_api_client: okc.OkApiClient, trait_name: str, relation_name: str, layers: [str], keep_ciid_as_column: bool = False) -> List[Dict[str,Any]]:
    """
    Returns the specified relation for a trait

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_name : str
        the name of the trait to query the data

    layers : [str]
        list containing layer_ids to search

    keep_ciid_as_column : bool
        True if ciid should be returned in result, False otherwise

    Returns
    -------
    List[Dict[str,Any]]
        result all data for a specific trait in a list format
    """

    # ds = DSLSchema(client.schema)
    ds = DSLSchema(ok_api_client.get_schema())

    escaped_trait_name = _get_escaped_trait_name(trait_name)
    prefixed_escaped_trait_name = _get_prefixed_trait_name(escaped_trait_name)

    tetType = getattr(ds.TraitEntitiesType, prefixed_escaped_trait_name)
    dsl_type = getattr(ds, f"TE_{escaped_trait_name}")
    dsl_root_type = getattr(ds, f"TERoot_{escaped_trait_name}")
    dsl_wrapper_type = getattr(ds, f"TEWrapper_{escaped_trait_name}")
    entity_fields = list(map(lambda t: getattr(dsl_type, t[0]).select(ds.RelatedCIType.relatedCIID), filter(lambda t: t[0] == relation_name and _is_non_trait_hinted_relation_field(t[1].type), dsl_type._type.fields.items())))

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

    result = ok_api_client.execute_graphql(query, variables={"layers": layers})

    # data_frame = (
    #     pd.json_normalize(result['traitEntities'][prefixed_escaped_trait_name]['all'])
    #         .rename(columns={"ciid": "base_ciid", f'entity.{relation_name}': "related_ciids"})
    #         .set_index('base_ciid', drop=not keep_ciid_as_column)
    # )
    # data_frame['related_ciids'] = data_frame['related_ciids'].apply(lambda x: list(map(lambda i: i['relatedCIID'], x)))

    result_list = []
    for entity in result['traitEntities'][prefixed_escaped_trait_name]['all']:
        related_ciids = [related_entity['relatedCIID'] for related_entity in entity]
        result_dict = {
            "base_ciid": entity['ciid'],
            "related_ciids": related_ciids,
        }
        result_list.append(result_dict)

    return result_list

# NOTE renamed to bulk_replace_trait_cis based on what the function dos and the similarity with the bulk_replace_trait_cis_by_filter function below
def bulk_replace_trait_entities(ok_api_client: okc.OkApiClient, trait_name: str, input: List[Dict[str,Any]], write_layer: str, read_layers: [str] = None) -> bool:
    """
    Sets all traitentities, this will also delete all old trait entities, if there are any

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
        
    # final_input = list(map(lambda kv: {"ciid": kv[0], "attributes": kv[1]}, input.to_dict('index').items()))
        
    if read_layers is None:
        read_layers = [write_layer]
    result = ok_api_client.execute_graphql(query, variables=dict(
        writeLayer=write_layer, 
        readLayers=read_layers, 
        input=input
        ))

    return result[f"bulkReplace_{prefixed_escaped_trait_name}"]["success"]

def bulk_replace_trait_entities_by_filter(ok_api_client: okc.OkApiClient, trait_name: str, input: List[Dict[str,Any]], id_attributes: [str], id_relations: [str], write_layer: str, read_layers: [str] = None, filter: object = {}) -> bool:
    """
    Replaces all traitentites in a layer, it can use a filter when updating the traitentities,
    this will also delete all old trait entities, if there are any

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_name : str
        the name of the trait to query the data

    input : List[Dict[str,Any]]
        The cis items which will be added to the layer

    id_attributes : [str]
        TODO add description
    
    id_relations : [str]
        TODO add description

    write_layer : str
        the name of the layer in which the data should be added

    read_layers : [str]
        A list with names of the layers in which the omnikeeper will look if the cis already exists

    filter : object
        TODO add description

    Returns
    -------
    bool 
        True if the update is successful, False otherwise
    """
    
    escaped_trait_name = _get_escaped_trait_name(trait_name)
    prefixed_escaped_trait_name = _get_prefixed_trait_name(escaped_trait_name)

    # example for filter object: {type: {exact: "Validator"}, context: {exact: "test"}, group: {exact: "test"} }
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
        
    # final_input = input.to_dict('records')
    
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
