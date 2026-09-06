import json
from client import AgentUserCoreferenceEntityResolver

def main():
    resolver = AgentUserCoreferenceEntityResolver()
    resolver.register_entity("ENT_091", "Apollo CRM Pipeline", "project")
    
    utterance = "Can you deploy it to production right now?"
    result = resolver.resolve_references(utterance)
    print("Resolved Utterance:", json.dumps(result, indent=2))
    assert result["substitutions_count"] == 1
    assert "Apollo CRM Pipeline" in result["resolved_utterance"]
    print("Coreference entity resolver verification: PASS")

if __name__ == "__main__":
    main()
