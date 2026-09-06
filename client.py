import re
from typing import Dict, Any, List, Optional

class AgentUserCoreferenceEntityResolver:
    """
    Maintains dialogue discourse entities in recency stack to resolve anaphoric pronouns
    ('it', 'they', 'him', 'that project') to canonical entity identifiers.
    """
    PRONOUN_CATEGORIES = {
        "it": "object",
        "that": "object",
        "this": "object",
        "he": "person_male",
        "she": "person_female",
        "they": "plural_or_neutral"
    }

    def __init__(self):
        self.discourse_entities: List[Dict[str, Any]] = []

    def register_entity(self, entity_id: str, canonical_name: str, entity_type: str):
        self.discourse_entities.insert(0, {
            "id": entity_id,
            "name": canonical_name,
            "type": entity_type
        })

    def resolve_references(self, utterance: str) -> Dict[str, Any]:
        words = utterance.split()
        resolved_utterance = utterance
        substitutions = []

        for w in words:
            clean_w = w.lower().strip(",.?!:;'\"")
            if clean_w in self.PRONOUN_CATEGORIES:
                target_type = self.PRONOUN_CATEGORIES[clean_w]
                
                # Search recency stack
                for ent in self.discourse_entities:
                    if target_type == "object" or ent["type"] in ["project", "service", "device", "concept"]:
                        pattern = re.compile(rf"\b{re.escape(w)}\b")
                        resolved_utterance = pattern.sub(f"{ent['name']} ({ent['id']})", resolved_utterance, count=1)
                        substitutions.append({"pronoun": w, "resolved_to": ent["name"], "entity_id": ent["id"]})
                        break

        return {
            "original_utterance": utterance,
            "resolved_utterance": resolved_utterance,
            "substitutions_count": len(substitutions),
            "substitutions": substitutions
        }
