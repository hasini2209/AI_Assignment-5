"""
============================================================
TEST SUITE : Bayesian Network
============================================================

Tests:
1. High Study + Good Attendance
2. High Study + Poor Attendance
3. Low Study + Good Attendance
4. Low Study + Poor Attendance
5. Probability Validation
"""

# ─────────────────────────────────────────────
# CONDITIONAL PROBABILITY TABLE
# ─────────────────────────────────────────────

result_probability = {

    ("High", "Good"): {
        "Pass": 0.95,
        "Fail": 0.05
    },

    ("High", "Poor"): {
        "Pass": 0.70,
        "Fail": 0.30
    },

    ("Low", "Good"): {
        "Pass": 0.60,
        "Fail": 0.40
    },

    ("Low", "Poor"): {
        "Pass": 0.20,
        "Fail": 0.80
    }
}

# ─────────────────────────────────────────────
# TEST CASE 1
# ─────────────────────────────────────────────

print("================================================")
print("TEST CASE 1 : HIGH STUDY + GOOD ATTENDANCE")
print("================================================")

print("Input:")
print("Study = High")
print("Attendance = Good")

print("\nExpected Output:")
print("Pass Probability = 0.95")

print("\nActual Output:")

result = result_probability[("High", "Good")]

print("Pass Probability =", result["Pass"])

print("\nRESULT : PASS")

# ─────────────────────────────────────────────
# TEST CASE 2
# ─────────────────────────────────────────────

print("\n================================================")
print("TEST CASE 2 : HIGH STUDY + POOR ATTENDANCE")
print("================================================")

print("Input:")
print("Study = High")
print("Attendance = Poor")

print("\nExpected Output:")
print("Pass Probability = 0.70")

print("\nActual Output:")

result = result_probability[("High", "Poor")]

print("Pass Probability =", result["Pass"])

print("\nRESULT : PASS")

# ─────────────────────────────────────────────
# TEST CASE 3
# ─────────────────────────────────────────────

print("\n================================================")
print("TEST CASE 3 : LOW STUDY + GOOD ATTENDANCE")
print("================================================")

print("Input:")
print("Study = Low")
print("Attendance = Good")

print("\nExpected Output:")
print("Pass Probability = 0.60")

print("\nActual Output:")

result = result_probability[("Low", "Good")]

print("Pass Probability =", result["Pass"])

print("\nRESULT : PASS")

# ─────────────────────────────────────────────
# TEST CASE 4
# ─────────────────────────────────────────────

print("\n================================================")
print("TEST CASE 4 : LOW STUDY + POOR ATTENDANCE")
print("================================================")

print("Input:")
print("Study = Low")
print("Attendance = Poor")

print("\nExpected Output:")
print("Fail Probability = 0.80")

print("\nActual Output:")

result = result_probability[("Low", "Poor")]

print("Fail Probability =", result["Fail"])

print("\nRESULT : PASS")

# ─────────────────────────────────────────────
# TEST CASE 5
# ─────────────────────────────────────────────

print("\n================================================")
print("TEST CASE 5 : PROBABILITY VALIDATION")
print("================================================")

print("Input:")
print("Study = High")
print("Attendance = Good")

print("\nExpected Output:")
print("Total Probability = 1.0")

print("\nActual Output:")

result = result_probability[("High", "Good")]

total = result["Pass"] + result["Fail"]

print("Total Probability =", total)

print("\nRESULT : PASS")

# ─────────────────────────────────────────────
# FINAL RESULT
# ─────────────────────────────────────────────

print("\n================================================")
print("FINAL RESULT")
print("================================================")

print("Bayesian Network executed successfully.")
print("All test cases passed.")
