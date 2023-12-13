
from gql import gql
from gql.dsl import DSLQuery, DSLVariableDefinitions, DSLSchema, dsl_gql
from gql.transport.exceptions import (
    TransportQueryError,
)
import omnikeeper_client as okc
from typing import List, Dict, Any
from .traitentities import (
    _get_escaped_trait_name,
    _get_prefixed_trait_name,
    _is_non_trait_hinted_relation_field,
    get_all_traitentities_list,
)
import uuid

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

    client = ok_api_client._get_graphql_client()
    with client as session:
        ds = DSLSchema(client.schema)

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

        result = session.execute(query, variable_values={"layers": layers})

        # data_frame = (
        #     pd.json_normalize(result['traitEntities'][prefixed_escaped_trait_name]['all'])
        #         .rename(columns={"ciid": "base_ciid", f'entity.{relation_name}': "related_ciids"})
        #         .set_index('base_ciid', drop=not keep_ciid_as_column)
        # )
        # data_frame['related_ciids'] = data_frame['related_ciids'].apply(lambda x: list(map(lambda i: i['relatedCIID'], x)))

        result_list = []
        for entity in result['traitEntities'][prefixed_escaped_trait_name]['all']:
            # TODO check how related_ciids are mapped from result
            # related_ciids = [related_entity['relatedCIID'] for related_entity in entity]
            related_ciids = [related_entity['relatedCIID'] for related_entity in entity['entity'][relation_name]]
            result_dict = {
                "base_ciid": entity['ciid'],
                "related_ciids": related_ciids,
            }
            result_list.append(result_dict)

        return result_list

def add_trait_relations_by_ciid(ok_api_client: okc.OkApiClient, trait_name: str, predicate: str, base_ciid: uuid.UUID, related_ciids_to_add: List[uuid.UUID], write_layer: str, read_layers: [str] = None) -> bool:
    """
    adds trait relations for a specific ci, the relation should be defined when defining the trait as trait relation definition

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_name : str
        the name of the trait that defined the relation and cis fulfill this trait

    predicate : str
        predicate of relation, defined in trait relation definition

    base_ciid : uuid.UUID
        id of the ci for which relations are being added

    related_ciids_to_add : List[uuid.UUID]
        list with the ids of the related cis
    
    write_layer : str
        id of the layer to add the relations

    read_layers : [str]
        list containing layer_ids to search

    Returns
    -------
    bool
        True if execution was successful, False otherwise
    """

    client = ok_api_client._get_graphql_client()
    with client as session:
        ds = DSLSchema(client.schema)
        escaped_trait_name = _get_escaped_trait_name(trait_name)
        prefixed_escaped_trait_name = _get_prefixed_trait_name(escaped_trait_name)

        query = gql(f"""
            mutation($readLayers: [String]!, $writeLayer: String!, $baseCIID: Guid!, $relatedCIIDsToAdd: [Guid]!) {{
            addRelationsByCIID_{prefixed_escaped_trait_name}_{predicate}(
                layers: $readLayers
                writeLayer: $writeLayer
                baseCIID: $baseCIID
                relatedCIIDsToAdd: $relatedCIIDsToAdd
            ) {{
                ciid
            }}
            }}
            """)
        
        if read_layers is None:
            read_layers = [write_layer]

        try:
            result = ok_api_client.execute_graphql(query, variables=dict(
                writeLayer=write_layer, 
                readLayers=read_layers, 
                baseCIID=str(base_ciid),
                relatedCIIDsToAdd=[str(uuid) for uuid in related_ciids_to_add]
            ))
            
            if "ciid" in result[f"addRelationsByCIID_{prefixed_escaped_trait_name}_{predicate}"]:
                return True
            else: 
                print(result)
                return False
        except TransportQueryError as e:
            print(e)
            return False
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return False
