from gql import Client
import pandas as pd
import graphql
from graphql import GraphQLType
from gql.dsl import DSLQuery, DSLVariableDefinitions, DSLSchema, dsl_gql

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


def is_non_trait_hinted_relation_field(type: GraphQLType) -> bool:
    if not graphql.type.is_list_type(type):
        return False
    list_type = graphql.type.assert_list_type(type)
    if not graphql.type.is_object_type(list_type.of_type):
        return False
    if list_type.of_type.name != 'RelatedCIType':
        return False
    return True

def get_all(client: Client, trait_name: str, layers: [str], keep_ciid_as_column: bool = False) -> pd.DataFrame:
    with client as session:
        ds = DSLSchema(client.schema)

        escaped_trait_name = str.replace(trait_name, '.', '__')
        prefixed_escaped_trait_name = escaped_trait_name
        if prefixed_escaped_trait_name.startswith("_"):
            prefixed_escaped_trait_name = f"m{prefixed_escaped_trait_name}"

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
                .rename(columns=lambda n: n.removeprefix("entity."))
        )
        return data_frame

def get_relation(client: Client, trait_name: str, relation_name: str, layers: [str], keep_ciid_as_column: bool = False) -> pd.DataFrame:
    with client as session:
        ds = DSLSchema(client.schema)

        escaped_trait_name = str.replace(trait_name, '.', '__')
        prefixed_escaped_trait_name = escaped_trait_name
        if prefixed_escaped_trait_name.startswith("_"):
            prefixed_escaped_trait_name = f"m{prefixed_escaped_trait_name}"

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