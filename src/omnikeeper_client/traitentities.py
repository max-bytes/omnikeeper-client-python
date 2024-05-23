from gql import gql
import graphql
from graphql import GraphQLType
from gql.dsl import DSLQuery, DSLVariableDefinitions, DSLSchema, dsl_gql
from dateutil import parser
import datetime
import omnikeeper_client as okc
from typing import List, Dict, Any, Self
import uuid
from typing import (
    List,
)


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

def _get_escaped_trait_id(name: str) -> str:
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

def _get_prefixed_trait_id(name: str) -> str:
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

def get_latest_trait_change(ok_api_client: okc.OkApiClient, trait_id: str, layers: List[str]) -> datetime.datetime:
    """
    Returns the timestamp of the latest change for the provided trait

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_id : str
        the id of the trait to query the data

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

        escaped_trait_id = _get_escaped_trait_id(trait_id)
        prefixed_escaped_trait_id = _get_prefixed_trait_id(escaped_trait_id)
        tetType = getattr(ds.TraitEntitiesType, prefixed_escaped_trait_id)
        dsl_root_type = getattr(ds, f"TERoot_{escaped_trait_id}")
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

        timestamp_str = result['traitEntities'][prefixed_escaped_trait_id]['latestChangeAll']['timestamp']
        timestamp = parser.parse(timestamp_str)
        return timestamp
 
def _get_all_traitentities(ok_api_client: okc.OkApiClient, trait_id: str, layers: List[str]) -> List[Dict[str,Any]]:
    """
    Internal method used to fetch all traitentites

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_id : str
        the id of the trait to query the data

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

        escaped_trait_id = _get_escaped_trait_id(trait_id)
        prefixed_escaped_trait_id = _get_prefixed_trait_id(escaped_trait_id)

        tetType = getattr(ds.TraitEntitiesType, prefixed_escaped_trait_id)
        dsl_type = getattr(ds, f"TE_{escaped_trait_id}")
        dsl_root_type = getattr(ds, f"TERoot_{escaped_trait_id}")
        dsl_wrapper_type = getattr(ds, f"TEWrapper_{escaped_trait_id}")
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

        data_list = result['traitEntities'][prefixed_escaped_trait_id]['all']
        for data in data_list:
            data.update(data.pop('entity'))

        def unescape_trait_attribute_name(name: str) -> str:
            return name.replace("__", ".")
        final_output = [{unescape_trait_attribute_name(k): v for k, v in d.items()} for d in data_list]
        
        return final_output
    
  
def get_all_traitentities(ok_api_client: okc.OkApiClient, trait_id: str, layers: List[str]) -> List[Dict[str,Any]]:
    """
    Returns all traitentites

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_id : str
        the id of the trait to query the data

    layers : [str]
        list containing layer_ids to search

    Returns
    -------
    List[Dict[str,Any]]
        result containing all traitentites
    """
    
    trait_entities = _get_all_traitentities(ok_api_client, trait_id, layers)
    return trait_entities

def get_all_traitentity_relations(ok_api_client: okc.OkApiClient, trait_id: str, traitrelation_id: str, layers: List[str]) -> List[Dict[str,Any]]:
    """
    Returns the trait relations for all trait entities of a particular trait

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_id : str
        the id of the trait to query the data

    layers : [str]
        list containing layer_ids to search

    Returns
    -------
    List[Dict[str,Any]]
        result all data for a specific trait in a list format
    """

    client = ok_api_client._get_graphql_client()
    with client as session:
        ds = DSLSchema(client.schema)

        escaped_trait_id = _get_escaped_trait_id(trait_id)
        prefixed_escaped_trait_id = _get_prefixed_trait_id(escaped_trait_id)

        tetType = getattr(ds.TraitEntitiesType, prefixed_escaped_trait_id)
        dsl_type = getattr(ds, f"TE_{escaped_trait_id}")
        dsl_root_type = getattr(ds, f"TERoot_{escaped_trait_id}")
        dsl_wrapper_type = getattr(ds, f"TEWrapper_{escaped_trait_id}")

        entity_fields = list(map(lambda t: getattr(dsl_type, t[0]).select(ds.RelatedCIType.relatedCIID), filter(lambda t: t[0] == traitrelation_id and _is_non_trait_hinted_relation_field(t[1].type), dsl_type._type.fields.items())))

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

        result_list = []
        for entity in result['traitEntities'][prefixed_escaped_trait_id]['all']:
            related_ciids = [related_entity['relatedCIID'] for related_entity in entity['entity'][traitrelation_id]]
            result_dict = {
                "base_ciid": entity['ciid'],
                "related_ciids": related_ciids,
            }
            result_list.append(result_dict)

        return result_list
    
def set_traitentity_relations(ok_api_client: okc.OkApiClient, trait_id: str, traitrelation_id: str, base_ciid: uuid.UUID | str, related_ciids: List[uuid.UUID | str], write_layer: str, read_layers: List[str] = None) -> bool:
    """
    Sets a particular trait relation of a particular trait for a single CI
    Adds new traitrelations and deletes all traitrelations not in the provided list

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_id : str
        the id of the trait

    traitrelation_id: str
        the id of the trait's traitrelation
        
    base_ciid: uuid.UUID | str
        the base ciid
        
    related_ciids: List[uuid.UUID | str]
        the list of related ciids

    write_layer : str
        the id of the layer in which the data should be added

    read_layers : [str]
        A list with ids of the layers in which the omnikeeper will look if trait entities already exist

    Returns
    -------
    List[Dict[str,Any]]
        result all data for a specific trait in a list format
    """
        
    prefixed_escaped_trait_id = _get_prefixed_trait_id(_get_escaped_trait_id(trait_id))
    escaped_traitrelation_id = _get_escaped_trait_id(traitrelation_id)
    query = gql(f"""
        mutation($readLayers: [String]!, $writeLayer: String!, $baseCIID: Guid!, $relatedCIIDs: [Guid!]!) {{
        setRelationsByCIID_{prefixed_escaped_trait_id}_{escaped_traitrelation_id}(
            layers: $readLayers
            writeLayer: $writeLayer
            baseCIID: $baseCIID
            relatedCIIDs: $relatedCIIDs
        ) {{
            ciid
        }}
        }}
        """)
        
    if read_layers is None:
        read_layers = [write_layer]

    ok_api_client.execute_graphql(query, variables=dict(
        writeLayer=write_layer, 
        readLayers=read_layers, 
        baseCIID=base_ciid,
        relatedCIIDs=related_ciids
        ))

    return True

def bulk_replace_traitentity_relations(ok_api_client: okc.OkApiClient, trait_id: str, traitrelation_id: str, input: List[Dict[str, Any]], relevant_ciids: List[str], write_layer: str, read_layers: List[str] = None) -> bool:
    """
    Bulk replaces a particular trait relation of a particular trait for ALL trait entities of that trait
    Adds new traitrelations and deletes all relevant traitrelations not in the provided list

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_id : str
        the id of the trait

    traitrelation_id: str
        the id of the trait's traitrelation
        
    input: List[Dict[str, Any]]
        a list of dicts, the dicts in the following form: { "baseCIID" = <ciid>, "relatedCIIDs" = [<ciid>, <ciid>, ...] }

    relevant_ciids: List[str]
        a list of CIIDs, that specifies which CIs are actually relevant for this operation. This is necessary to let omnikeeper know which CIs it should consider for this operation
        CIs not in the list of relevant_ciids are not changed
        depending on your usecase..
        ...you may want to set relevant_ciids equal to the list of baseCIIDs in input
        ...or you may want to keep track of the relevant_ciids yourself, because you got an initial list from get_all_traitentity_relations()

    write_layer : str
        the id of the layer in which the data should be added

    read_layers : [str]
        A list with ids of the layers in which the omnikeeper will look if trait entities already exist

    Returns
    -------
    bool 
        True if the update is successful, False otherwise
    """

    prefixed_escaped_trait_id = _get_prefixed_trait_id(_get_escaped_trait_id(trait_id))
    escaped_traitrelation_id = _get_escaped_trait_id(traitrelation_id)
    query = gql(f"""
        mutation($readLayers: [String]!, $writeLayer: String!, $input: [TE_Upsert_Relations_Only_Input]!, $relevantCIIDs: [Guid]!) {{
        bulkReplaceRelations_{prefixed_escaped_trait_id}_{escaped_traitrelation_id}(
            layers: $readLayers
            writeLayer: $writeLayer
            input: $input
            relevantCIIDs: $relevantCIIDs
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
        input=input,
        relevantCIIDs=relevant_ciids
        ))

    return result[f"bulkReplaceRelations_{prefixed_escaped_trait_id}_{escaped_traitrelation_id}"]["success"]
  
def _bulk_replace_trait_entities_by_filter(ok_api_client: okc.OkApiClient, trait_id: str, input: List[Dict[str,Any]], id_attributes: List[str], id_relations: List[str], write_layer: str, read_layers: List[str] = None, filter: object = {}) -> bool:
    """
    Internal method used to replace all traitentites in a layer, it can use a filter when updating the trait entities,
    this will also delete all old trait entities, if there are any

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_id : str
        the id of the trait to query the data

    input : List[Dict[str,Any]]
        Trait entities as list of dictionaries

    id_attributes : [str]
        attributes to be considered as trait IDs
    
    id_relations : [str]
        ids to be considered as trait relations IDs

    write_layer : str
        the id of the layer in which the data should be added

    read_layers : [str]
        A list with ids of the layers in which the omnikeeper will look if trait entities already exist

    filter : object
        a filter object can be used, default {}, example for filter object: {type: {exact: "Validator"}, context: {exact: "test"}, group: {exact: "test"} }

    Returns
    -------
    bool 
        True if the update is successful, False otherwise
    """
    
    escaped_trait_id = _get_escaped_trait_id(trait_id)
    prefixed_escaped_trait_id = _get_prefixed_trait_id(escaped_trait_id)
    query = gql(f"""
        mutation($readLayers: [String]!, $writeLayer: String!, $idAttributes: [String!]!, $idRelations: [String!]!, $filter: TE_filter_Input_{escaped_trait_id}!, $input: [TE_Upsert_Input_{escaped_trait_id}]!) {{
        bulkReplaceByFilter_{prefixed_escaped_trait_id}(
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

    return result[f"bulkReplaceByFilter_{prefixed_escaped_trait_id}"]["success"]

def _bulk_replace_trait_entities(ok_api_client: okc.OkApiClient, trait_id: str, input: List[Dict[str,Any]], write_layer: str, read_layers: List[str] = None) -> bool:
    """
    Internal method that sets all trait entities, this will also delete all old trait entities, if there are any

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_id : str
        the id of the trait to query the data

    input : List[Dict[str,Any]]
        The cis items which will be inserted, needs to be of the form:
        [{"ciid": "836DA01F-9ABD-4D9D-80C7-02AF85C822A8", "attribute1": "foo", "attribute2": 2},
         {"ciid": "936DA01F-9ABD-4D9D-80C7-02AF85C822A8", "attribute1": "bar", "attribute2": 3}]

    write_layer : str
        the id of the layer in which the data should be added

    read_layers : [str]
        A list with ids of the layers in which the omnikeeper will look if the cis already exists

    Returns
    -------
    bool 
        True if the update is successful, False otherwise
    """
    escaped_trait_id = _get_escaped_trait_id(trait_id)
    prefixed_escaped_trait_id = _get_prefixed_trait_id(escaped_trait_id)

    query = gql(f"""
        mutation($readLayers: [String]!, $writeLayer: String!, $input: [TE_CIID_And_Upsert_Attributes_Only_Input_{escaped_trait_id}]!) {{
        bulkReplace_{prefixed_escaped_trait_id}(
            layers: $readLayers
            writeLayer: $writeLayer
            input: $input
        ) {{
            success
        }}
        }}
        """)

    def escape_trait_attribute_name(name: str) -> str:
        return name.replace(".", "__")
    final_input = [{"ciid": d["ciid"], "attributes": {escape_trait_attribute_name(k): v for k, v in d.items() if k != "ciid"}} for d in input]
        
    if read_layers is None:
        read_layers = [write_layer]
    result = ok_api_client.execute_graphql(query, variables=dict(
        writeLayer=write_layer, 
        readLayers=read_layers, 
        input=final_input
        ))

    return result[f"bulkReplace_{prefixed_escaped_trait_id}"]["success"]

# TODO: support use of uuid.UUID for ciids
def bulk_replace_trait_entities_by_filter(ok_api_client: okc.OkApiClient, trait_id: str, input: List[Dict[str,Any]], id_attributes: List[str], id_relations: List[str], write_layer: str, read_layers: List[str] = None, filter: object = {}) -> bool:
    """
    Replaces all traitentites in a layer, it can use a filter when updating the trait entities,
    this will also delete all old trait entities, if there are any

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_id : str
        the id of the trait to query the data

    input : List[Dict[str,Any]]
        The cis items which will be inserted, needs to be of the form:
        [{"ciid": "836DA01F-9ABD-4D9D-80C7-02AF85C822A8", "attribute1": "foo", "attribute2": 2},
         {"ciid": "936DA01F-9ABD-4D9D-80C7-02AF85C822A8", "attribute1": "bar", "attribute2": 3}]

    id_attributes : [str]
        attributes to be considered as trait IDs
    
    id_relations : [str]
        ids to be considered as trait relations IDs

    write_layer : str
        the id of the layer in which the data should be added

    read_layers : [str]
        A list with ids of the layers in which the omnikeeper will look if trait entities already exist

    filter : object
        a filter object can be used, default {}, example for filter object: {type: {exact: "Validator"}, context: {exact: "test"}, group: {exact: "test"} }

    Returns
    -------
    bool 
        True if the update is successful, False otherwise
    """
    result = _bulk_replace_trait_entities_by_filter(ok_api_client, trait_id, input, id_attributes, id_relations, write_layer, read_layers, filter)
    return result

# TODO: support use of uuid.UUID for ciids
def bulk_replace_trait_entities(ok_api_client: okc.OkApiClient, trait_id: str, input: List[Dict[str,Any]], write_layer: str, read_layers: List[str] = None) -> bool:
    """
    Sets all trait entities, this will also delete all old trait entities, if there are any

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_id : str
        the id of the trait to query the data

    input : List[Dict[str,Any]]
        The cis items which will be inserted, needs to be of the form:
        [{"ciid": "836DA01F-9ABD-4D9D-80C7-02AF85C822A8", "attribute1": "foo", "attribute2": 2},
         {"ciid": "936DA01F-9ABD-4D9D-80C7-02AF85C822A8", "attribute1": "bar", "attribute2": 3}]

    write_layer : str
        the id of the layer in which the data should be added

    read_layers : [str]
        A list with ids of the layers in which the omnikeeper will look if the cis already exists

    Returns
    -------
    bool 
        True if the update is successful, False otherwise
    """
    result = _bulk_replace_trait_entities(ok_api_client, trait_id, input, write_layer, read_layers)
    return result

OKEntityItem = Dict[str, Any]

class OKEntityList:
    def __init__(self, ok_list: List[OKEntityItem]):
        self.ok_list = ok_list
        self.ciid_lookup_table = {str(v['ciid']): index for index, v in enumerate(ok_list)}

    def update_or_add_via_ciid(self, new_item: OKEntityItem, ciid: str, duplicate_strategy: str = 'update') -> int:
        index = self.ciid_lookup_table.get(ciid, None)
        if index is not None:
            # ci exists in the data already -> update
            existing = self.ok_list[index]

            old_update_count = existing.get('__update_count', 0)

            if old_update_count >= 1 and duplicate_strategy is not None:
                if duplicate_strategy == "skip":
                    return -1
                else: # default: update
                    existing.update(new_item)
            else:
                existing.update(new_item)
                
            existing['__update_count'] = old_update_count + 1

            return index
        else:
            # ci does not exist yet -> add
            new_item['ciid'] = ciid
            new_item['__update_count'] = 1
            self.ok_list.append(new_item)
            self.ciid_lookup_table[ciid] = len(self.ok_list) - 1
            return index
    
    def get_final_list(self) -> List[OKEntityItem]:
        return [{k: v for k, v in d.items() if k != '__update_count'} for d in self.ok_list if '__update_count' in d]


class OKRelationList:
    def __init__(self, ok_list: List[Dict[str, Any]]):
        self.ok_list = ok_list
        self.lookup_table = {str(v['base_ciid']): index for index, v in enumerate(ok_list)}
        self.keeps = set() # set of tuples [(base_ciid, related_ciid)], which tracks what relations we must "keep"

    def add_or_update(self, base_ciid: str, related_ciids: List[str], merge_strategy_related_ciids: str = 'replace'):
        related_ciids_non_duplicates = list(set(related_ciids)) # NOTE: list(set(...)) ensures uniqueness
        index = self.lookup_table.get(base_ciid, None)
        if index is not None:
            # give caller the choice on how to merge related_ciids
            if merge_strategy_related_ciids == 'replace':
                # simply replace existing related_ciids dictionary with new dictionary
                self.ok_list[index].update({'related_ciids': related_ciids_non_duplicates})
                self.keeps.update([(base_ciid, related_ciid) for related_ciid in related_ciids_non_duplicates])
            elif merge_strategy_related_ciids == 'merge':
                exsting_related_ciids = self.ok_list[index]['related_ciids']
                final_related_ciids = list(set(exsting_related_ciids + related_ciids_non_duplicates)) # NOTE: list(set(...)) ensures uniqueness
                self.ok_list[index].update({'related_ciids': final_related_ciids})
                self.keeps.update([(base_ciid, related_ciid) for related_ciid in related_ciids_non_duplicates])
            else:
                raise Exception(f"Unknown value for merge_strategy_related_ciids: {merge_strategy_related_ciids}")
        else:
            self.ok_list.append({'base_ciid': base_ciid, 'related_ciids': related_ciids_non_duplicates})
            self.keeps.update([(base_ciid, related_ciid) for related_ciid in related_ciids_non_duplicates])
            self.lookup_table[base_ciid] = len(self.ok_list) - 1

    def build_inverse_list(self) -> Self:
        tmp = dict()
        for d in self.ok_list:
            for r in d['related_ciids']:
                existing = tmp.get(r, None)
                if existing is None:
                    tmp[r] = [d['base_ciid']]
                else:
                    existing.append(d['base_ciid'])
        
        final_list = [{'base_ciid': k, 'related_ciids': v} for k, v in tmp.items()]
        return OKRelationList(final_list)

    def get_related_ciids(self, base_ciid: str, keep_only: bool, default = []) -> List[str]:
        index = self.lookup_table.get(base_ciid, None)
        if index is None:
            return default
        
        related_ciids = self.ok_list[index]["related_ciids"]
        if keep_only:
            return [related_ciid for related_ciid in related_ciids if (base_ciid, related_ciid) in self.keeps]
        else:
            return related_ciids
    
    def get_relevant_ciids(self) -> List[str]:
        return [d['base_ciid'] for d in self.ok_list]
    
    def get_final_list(self) -> List[Dict[str, Any]]:
        final = []
        for item in self.ok_list:
            final_related_ciids = [related_ciid for related_ciid in item['related_ciids'] if (item['base_ciid'], related_ciid) in self.keeps]
            if len(final_related_ciids) > 0:
                # HACK, TODO: rework client library to not have to rewrite keys
                # final.append({'base_ciid': item['base_ciid'], 'related_ciids': final_related_ciids})
                final.append({'baseCIID': item['base_ciid'], 'relatedCIIDs': final_related_ciids})

        return final