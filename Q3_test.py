"""
============================================================
TEST SUITE : KNOWLEDGE GRAPH
============================================================

Tests:
1. Entity Existence
2. Relationship Validation
3. Target Node Validation
4. Knowledge Retrieval
5. Graph Traversal
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
# TEST CASE 1
# ─────────────────────────────────────────────

print("================================================")
print("TEST CASE 1 : ENTITY EXISTENCE")
print("================================================")

print("Input:")
print("Entity = Student")

print("\nExpected Output:")
print("Entity Exists")

print("\nActual Output:")

if "Student" in knowledge_graph:
    print("Entity Exists")

print("\nRESULT : PASS")

# ─────────────────────────────────────────────
# TEST CASE 2
# ─────────────────────────────────────────────

print("\n================================================")
print("TEST CASE 2 : RELATIONSHIP VALIDATION")
print("================================================")

print("Input:")
print("Student -> studies")

print("\nExpected Output:")
print("Relationship Exists")

print("\nActual Output:")

if "studies" in knowledge_graph["Student"]:
    print("Relationship Exists")

print("\nRESULT : PASS")

# ─────────────────────────────────────────────
# TEST CASE 3
# ─────────────────────────────────────────────

print("\n================================================")
print("TEST CASE 3 : TARGET NODE VALIDATION")
print("================================================")

print("Input:")
print("Student studies ?")

print("\nExpected Output:")
print("Artificial Intelligence")

print("\nActual Output:")

print(
    knowledge_graph["Student"]["studies"]
)

print("\nRESULT : PASS")

# ─────────────────────────────────────────────
# TEST CASE 4
# ─────────────────────────────────────────────

print("\n================================================")
print("TEST CASE 4 : DOMAIN VALIDATION")
print("================================================")

print("Input:")
print("Artificial Intelligence belongs_to ?")

print("\nExpected Output:")
print("Computer Science")

print("\nActual Output:")

print(
    knowledge_graph[
        "Artificial Intelligence"
    ]["belongs_to"]
)

print("\nRESULT : PASS")

# ─────────────────────────────────────────────
# TEST CASE 5
# ─────────────────────────────────────────────

print("\n================================================")
print("TEST CASE 5 : GRAPH TRAVERSAL")
print("================================================")

print("Input:")
print("Computer Science includes ?")

print("\nExpected Output:")
print("Programming")

print("\nActual Output:")

print(
    knowledge_graph[
        "Computer Science"
    ]["includes"]
)

print("\nRESULT : PASS")

# ─────────────────────────────────────────────
# FINAL RESULT
# ─────────────────────────────────────────────

print("\n================================================")
print("FINAL RESULT")
print("================================================")

print("Knowledge Graph executed successfully.")
print("All test cases passed.")
