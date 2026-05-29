"""
============================================================
Knowledge Graph using Python
============================================================

This program demonstrates a simple Knowledge Graph.

A Knowledge Graph represents:
1. Entities
2. Relationships
3. Connections between concepts

The graph stores relationships between:
- Student
- Artificial Intelligence
- Computer Science
"""

# ─────────────────────────────────────────────
# KNOWLEDGE GRAPH
# ─────────────────────────────────────────────

knowledge_graph = {

    "Student": {
        "studies": "Artificial Intelligence"
    },

    "Artificial Intelligence": {
        "belongs_to": "Computer Science"
    },

    "Computer Science": {
        "includes": "Programming"
    }
}

# ─────────────────────────────────────────────
# DISPLAY KNOWLEDGE GRAPH
# ─────────────────────────────────────────────

print("================================================")
print("KNOWLEDGE GRAPH")
print("================================================")

for entity, relations in knowledge_graph.items():

    for relation, target in relations.items():

        print(entity, "----", relation, "---->", target)
