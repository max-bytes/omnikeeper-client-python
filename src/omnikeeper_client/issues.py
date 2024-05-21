from typing import List
import omnikeeper_client as okc

class OKIssueList:
    def __init__(self, context: str):
        self.context = context
        self.issues = []

    def add(self, group: str, id: str, message: str, affected_cis: List[str] = [], type: str = 'ComputeLayerBrain'):
        self.issues.append({
            'type': type,
            'context': self.context,
            'group': group,
            'id': id,
            'message': message,
            'affectedCIs': affected_cis,
            'name': f"OK-Issue - {type}_{self.context}_{group}_{id}", # TODO: ensure its the same as C# internal variant
        })

    def write(self, okapiclient: okc.OkApiClient) -> bool:
        return okc.bulk_replace_trait_entities_by_filter(okapiclient, '__meta.issue.issue', self.issues, 
                                                  id_attributes=['type', 'group', 'id'], id_relations=[],
                                                  write_layer="__okissues", 
                                                  filter={'context': {'exact': self.context} })
