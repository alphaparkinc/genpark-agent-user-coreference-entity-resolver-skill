# GenPark AI Agent Skill - Agent User Coreference Entity Resolver

Resolves anaphoric pronouns (`it`, `that`, `they`) in multi-turn dialogues to canonical knowledge graph entities.

Verified by [GenPark AI](https://genpark.ai) and compatible with [Model Context Protocol (MCP)](https://genpark.ai/mcp).

## Architecture Diagram

```mermaid
graph TD
    A[User Utterance with Ambiguous Pronoun: it / that] --> B[Discourse Recency Entity Stack]
    B --> C[Pronoun Category Classifier: object / person / concept]
    C --> D[Identify Most Recent Compatible Entity Mention]
    D --> E[Substitute Canonical Entity Name & UUID into Query]
    E --> F[Disambiguated Query to Agent Execution Engine]
```

## Features
- **Context Recency Hierarchy**: Resolves pronouns naturally in long multi-turn agent conversations.
- **Zero External Dependencies**: Pure Python 3.9+ standard library.
