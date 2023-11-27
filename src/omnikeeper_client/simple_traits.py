from gql import Client, gql
import pandas as pd
import graphql
from graphql import GraphQLType
from gql.dsl import DSLQuery, DSLVariableDefinitions, DSLSchema, dsl_gql
from dateutil import parser
import datetime
from deprecated import deprecated

@deprecated(category=FutureWarning, reason="please use omnikeeper_client.* public functions instead, if really needed, use  OkApiClient()._is_relation_field()")
def is_relation_field(type: GraphQLType) -> bool:
    # a typical relation field looks like this:
    # GraphQLList <GraphQLObjectType 'TEWrapper_tsa_cmdb__interface'>>
    # or
    # GraphQLList <GraphQLObjectType 'RelatedCIType'>
    if not graphql.type.is_list_type(type):
        return False
    list_type = graphql.type.assert_list_type(type)
    if not graphql.type.is_object_type(list_type.of_type): # TODO: is this enough?
        return False
    return True

@deprecated(category=FutureWarning, reason="please use omnikeeper_client.* public functions instead, if really needed, use  OkApiClient()._is_non_trait_hinted_relation_field()")
def is_non_trait_hinted_relation_field(type: GraphQLType) -> bool:
    if not graphql.type.is_list_type(type):
        return False
    list_type = graphql.type.assert_list_type(type)
    if not graphql.type.is_object_type(list_type.of_type):
        return False
    if list_type.of_type.name != 'RelatedCIType':
        return False
    return True

@deprecated(category=FutureWarning, reason="please use omnikeeper_client.* public functions instead, if really needed, use  OkApiClient()._get_escaped_trait_name()")
def get_escaped_trait_name(name: str) -> str:
    return str.replace(name, '.', '__')

@deprecated(category=FutureWarning, reason="please use omnikeeper_client.* public functions instead, if really needed, use  OkApiClient()._get_prefixed_trait_name()")
def get_prefixed_trait_name(name: str) -> str:
    if name.startswith("_"):
        return f"m{name}"
    return name

@deprecated(category=FutureWarning, reason="please use omnikeeper_client public function get_latest_trait_change() instead")
def get_latest_change_for_all(client: Client, trait_name: str, layers: [str]) -> datetime.datetime:
    with client as session:
        ds = DSLSchema(client.schema)

        escaped_trait_name = get_escaped_trait_name(trait_name)
        prefixed_escaped_trait_name = get_prefixed_trait_name(escaped_trait_name)

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

@deprecated(category=FutureWarning, reason="please use omnikeeper_client.* public functions instead, use get_all_traitentities_list() if you want to work with list, use get_all_traitentities_dataframe() if you want to work with dataframes")
def get_all(client: Client, trait_name: str, layers: [str], keep_ciid_as_column: bool = False) -> pd.DataFrame:
    with client as session:
        ds = DSLSchema(client.schema)

        escaped_trait_name = get_escaped_trait_name(trait_name)
        prefixed_escaped_trait_name = get_prefixed_trait_name(escaped_trait_name)

        tetType = getattr(ds.TraitEntitiesType, prefixed_escaped_trait_name)
        dsl_type = getattr(ds, f"TE_{escaped_trait_name}")
        dsl_root_type = getattr(ds, f"TERoot_{escaped_trait_name}")
        dsl_wrapper_type = getattr(ds, f"TEWrapper_{escaped_trait_name}")
        entity_fields = list(map(lambda t: getattr(dsl_type, t[0]), filter(lambda t: not is_relation_field(t[1].type), dsl_type._type.fields.items())))

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

        data_frame = (
            pd.json_normalize(result['traitEntities'][prefixed_escaped_trait_name]['all'])
                .set_index('ciid', drop=not keep_ciid_as_column)
        )
        data_frame.columns = data_frame.columns.str.removeprefix('entity.')

        return data_frame

@deprecated(category=FutureWarning, reason="please use omnikeeper_client public function get_trait_relation() instead")
def get_relation(client: Client, trait_name: str, relation_name: str, layers: [str], keep_ciid_as_column: bool = False) -> pd.DataFrame:
    with client as session:
        ds = DSLSchema(client.schema)

        escaped_trait_name = get_escaped_trait_name(trait_name)
        prefixed_escaped_trait_name = get_prefixed_trait_name(escaped_trait_name)

        tetType = getattr(ds.TraitEntitiesType, prefixed_escaped_trait_name)
        dsl_type = getattr(ds, f"TE_{escaped_trait_name}")
        dsl_root_type = getattr(ds, f"TERoot_{escaped_trait_name}")
        dsl_wrapper_type = getattr(ds, f"TEWrapper_{escaped_trait_name}")
        entity_fields = list(map(lambda t: getattr(dsl_type, t[0]).select(ds.RelatedCIType.relatedCIID), filter(lambda t: t[0] == relation_name and is_non_trait_hinted_relation_field(t[1].type), dsl_type._type.fields.items())))

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

        data_frame = (
            pd.json_normalize(result['traitEntities'][prefixed_escaped_trait_name]['all'])
                .rename(columns={"ciid": "base_ciid", f'entity.{relation_name}': "related_ciids"})
                .set_index('base_ciid', drop=not keep_ciid_as_column)
        )
        data_frame['related_ciids'] = data_frame['related_ciids'].apply(lambda x: list(map(lambda i: i['relatedCIID'], x)))

        return data_frame
    
@deprecated(category=FutureWarning, reason="please use omnikeeper_client.* public functions instead, use bulk_replace_trait_entities_list() if you want to work with list, use bulk_replace_trait_entities_dataframe() if you want to work with dataframes")
def set_all(client: Client, trait_name: str, input: pd.DataFrame, write_layer: str, read_layers: [str] = None) -> bool:
    escaped_trait_name = get_escaped_trait_name(trait_name)
    prefixed_escaped_trait_name = get_prefixed_trait_name(escaped_trait_name)

    with client as session:
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
        
        final_input = list(map(lambda kv: {"ciid": kv[0], "attributes": kv[1]}, input.to_dict('index').items()))
        
        if read_layers is None:
            read_layers = [write_layer]
        result = session.execute(query, variable_values=dict(
            writeLayer=write_layer, 
            readLayers=read_layers, 
            input=final_input
            ))
        return result[f"bulkReplace_{prefixed_escaped_trait_name}"]["success"]

@deprecated(category=FutureWarning, reason="please use omnikeeper_client.* public functions instead, use bulk_replace_trait_entities_by_filter_list() if you want to work with list, use bulk_replace_trait_entities_by_filter_dataframe() if you want to work with dataframes")
def bulk_replace(client: Client, trait_name: str, input: pd.DataFrame, id_attributes: [str], id_relations: [str], write_layer: str, read_layers: [str] = None, filter: object = {}) -> bool:
    escaped_trait_name = get_escaped_trait_name(trait_name)
    prefixed_escaped_trait_name = get_prefixed_trait_name(escaped_trait_name)

    with client as session:
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
        
        final_input = input.to_dict('records')
        
        if read_layers is None:
            read_layers = [write_layer]
        result = session.execute(query, variable_values=dict(
            writeLayer=write_layer, 
            readLayers=read_layers, 
            idAttributes=id_attributes,
            idRelations=id_relations,
            filter=filter,
            input=final_input
            ))
        return result[f"bulkReplaceByFilter_{prefixed_escaped_trait_name}"]["success"]
