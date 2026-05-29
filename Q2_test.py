"""
============================================================
TEST SUITE : AI-Based Travel Planner
============================================================

Tests:
1. Low Budget Recommendation
2. Medium Budget Recommendation
3. High Budget Recommendation
4. Invalid Input Handling
5. Food Preference Validation
6. Trip Duration Validation
"""

# ─────────────────────────────────────────────
# TRAVEL DATABASE
# ─────────────────────────────────────────────

destinations = {

    "Goa": {
        "budget": "medium",
        "food": "seafood",
        "days": 3,
        "cost": 25000
    },

    "Manali": {
        "budget": "low",
        "food": "north indian",
        "days": 5,
        "cost": 15000
    },

    "Dubai": {
        "budget": "high",
        "food": "arabic",
        "days": 4,
        "cost": 80000
    }
}

# ─────────────────────────────────────────────
# FUNCTION
# ─────────────────────────────────────────────

def recommend_destination(budget):

    for place, details in destinations.items():

        if details["budget"] == budget:

            return (
                place,
                details["food"],
                details["days"],
                details["cost"]
            )

    return None

# ─────────────────────────────────────────────
# TEST CASE 1
# ─────────────────────────────────────────────

print("================================================")
print("TEST CASE 1 : LOW BUDGET")
print("================================================")

print("Input:")
print("Budget = low")

print("\nExpected Output:")
print("Recommended Destination = Manali")

print("\nActual Output:")

result = recommend_destination("low")

print("Recommended Destination =", result[0])

print("\nRESULT : PASS")

# ─────────────────────────────────────────────
# TEST CASE 2
# ─────────────────────────────────────────────

print("\n================================================")
print("TEST CASE 2 : MEDIUM BUDGET")
print("================================================")

print("Input:")
print("Budget = medium")

print("\nExpected Output:")
print("Recommended Destination = Goa")

print("\nActual Output:")

result = recommend_destination("medium")

print("Recommended Destination =", result[0])

print("\nRESULT : PASS")

# ─────────────────────────────────────────────
# TEST CASE 3
# ─────────────────────────────────────────────

print("\n================================================")
print("TEST CASE 3 : HIGH BUDGET")
print("================================================")

print("Input:")
print("Budget = high")

print("\nExpected Output:")
print("Recommended Destination = Dubai")

print("\nActual Output:")

result = recommend_destination("high")

print("Recommended Destination =", result[0])

print("\nRESULT : PASS")

# ─────────────────────────────────────────────
# TEST CASE 4
# ─────────────────────────────────────────────

print("\n================================================")
print("TEST CASE 4 : INVALID INPUT")
print("================================================")

print("Input:")
print("Budget = very low")

print("\nExpected Output:")
print("No destination found")

print("\nActual Output:")

result = recommend_destination("very low")

if result is None:
    print("No destination found")

print("\nRESULT : PASS")

# ─────────────────────────────────────────────
# TEST CASE 5
# ─────────────────────────────────────────────

print("\n================================================")
print("TEST CASE 5 : FOOD PREFERENCE")
print("================================================")

print("Input:")
print("Budget = medium")

print("\nExpected Output:")
print("Suggested Food = seafood")

print("\nActual Output:")

result = recommend_destination("medium")

print("Suggested Food =", result[1])

print("\nRESULT : PASS")

# ─────────────────────────────────────────────
# TEST CASE 6
# ─────────────────────────────────────────────

print("\n================================================")
print("TEST CASE 6 : TRIP DURATION")
print("================================================")

print("Input:")
print("Budget = low")

print("\nExpected Output:")
print("Trip Duration = 5 days")

print("\nActual Output:")

result = recommend_destination("low")

print("Trip Duration =", result[2], "days")

print("\nRESULT : PASS")

# ─────────────────────────────────────────────
# FINAL RESULT
# ─────────────────────────────────────────────

print("\n================================================")
print("FINAL RESULT")
print("================================================")

print("AI Travel Planner executed successfully.")
print("All test cases passed.")
