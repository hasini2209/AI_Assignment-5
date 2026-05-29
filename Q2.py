"""
============================================================
AI-Based Travel Planner
============================================================

This program implements a simple AI Travel Planner.

The system recommends travel destinations
based on:
1. Budget
2. Food Preference
3. Number of Days
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
# AI TRAVEL PLANNER FUNCTION
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
# USER INPUT
# ─────────────────────────────────────────────

print("================================================")
print("AI TRAVEL PLANNER")
print("================================================")

budget = input("Enter Budget (low/medium/high): ")

result = recommend_destination(budget)

if result:

    place, food, days, cost = result

    print("\nRecommended Destination :", place)
    print("Suggested Food          :", food)
    print("Trip Duration           :", days, "days")
    print("Estimated Cost          : ₹", cost)

else:

    print("No destination found.")
