import omnikeeper_client as okc
import omnikeeper_client.typing as okc_typing
import omnikeeper_client.util as okc_util
from gql import gql
from gql.transport.exceptions import (
    TransportQueryError,
)

# NOTE: these classes use camelCase members, so they can be easily encoded for GraphQL using okc_util.to_dict()
class TraitAttributeDefinition:
    def __init__(self, identifier: str, name: str, attribute_type: str = okc_typing.ATTRIBUTETYPE_TEXT, is_array: bool = False):
        self.identifier = identifier
        self.template = dict(
            name = name,
            type = attribute_type,
            isArray = is_array,
            isID = False, # NOTE: isID is deprecated anyway, so we don't support this
            valueConstraints = [] # TODO: support value constraints properly
        )

class TraitRelationDefinition:
    def __init__(self, identifier: str, predicate_id: str, direction_forward: bool, trait_hints: [str] = []):
        self.identifier = identifier
        self.template = dict(
            predicateID = predicate_id,
            directionForward = direction_forward,
            traitHints = trait_hints
        )

class TraitDefinition:
    def __init__(self, trait_id: str, required_attributes: [TraitAttributeDefinition], optional_attributes: [TraitAttributeDefinition] = [], optional_relations: [TraitRelationDefinition] = [], required_traits: [str] = []):
        self.id = trait_id
        self.requiredAttributes = required_attributes
        self.optionalAttributes = optional_attributes
        self.optionalRelations = optional_relations
        self.requiredTraits = required_traits

def upsert_trait(ok_api_client: okc.OkApiClient, trait_definition: TraitDefinition):
    """upsert a trait; create the trait if it does not exist, update it if it does

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_definition : TraitDefinition
        the trait's definition

    Returns
    -------
    bool
        True, if trait was upserted and is ready to use. False, if something fails
    """
        
    query = gql("""
    mutation ($trait_definition: UpsertRecursiveTraitInputType!) {
        manage_upsertRecursiveTrait(
            trait: $trait_definition
        ) {
            id
        }
    }""")
    
    marshalled_trait = okc_util.to_dict(trait_definition)
    try:
        ok_api_client.execute_graphql(query, variables=dict(
            trait_definition=marshalled_trait
        ))
    except TransportQueryError as e:
        return False

    return True



# TODO: should we change the return to a tri-state? deleted, not deleted, error?
def delete_trait(ok_api_client: okc.OkApiClient, trait_id: str):
    """deletes a trait

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_id : str
        the trait's ID

    Returns
    -------
    bool
        True, if trait was successfully deleted. False, if it did not exist in the first place, or if something failed
    """
        
    query = gql("""
    mutation ($trait_id: String!) {
        manage_removeRecursiveTrait(
            id: $trait_id
        )
    }""")
    
    try:
        ret = ok_api_client.execute_graphql(query, variables=dict(
            trait_id=trait_id
        ))
        return ret['manage_removeRecursiveTrait']
    except TransportQueryError as e:
        return False

# TODO: should we change the return to a tri-state? deleted, not deleted, error?
def check_trait(ok_api_client: okc.OkApiClient, trait_definition: TraitDefinition):
    """checks if a trait already exists with this exact definition

    Parameters
    ----------
    ok_api_client : OkApiClient
        The OkApiClient instance representing omnikeeper connection

    trait_definition : TraitDefinition
        the trait's definition

    Returns
    -------
    bool
        True, if trait exists exactly as defined; False if not, or in case of an error
    """
        
    query = gql("""
    query ($trait_definition: UpsertRecursiveTraitInputType!) {
        checkTrait(
            trait: $trait_definition
        )
    }""")
    
    marshalled_trait = okc_util.to_dict(trait_definition)
    try:
        ret = ok_api_client.execute_graphql(query, variables=dict(
            trait_definition=marshalled_trait
        ))
        return ret['checkTrait']
    except TransportQueryError as e:
        return False