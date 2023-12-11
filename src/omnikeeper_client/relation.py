
from gql.dsl import DSLQuery, DSLVariableDefinitions, DSLSchema, dsl_gql
import omnikeeper_client as okc
from typing import List, Dict, Any
from .traitentities import (
    _get_escaped_trait_name,
    _get_prefixed_trait_name,
    _is_non_trait_hinted_relation_field,
    get_all_traitentities_list,
)

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