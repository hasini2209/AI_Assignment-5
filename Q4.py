"""
============================================================
Bayesian Network using Python
============================================================

This program demonstrates a simple Bayesian Network.

The network predicts student performance
based on:
1. Study Hours
2. Attendance

The program calculates:
- Probability of Pass
- Probability of Fail
"""

# ─────────────────────────────────────────────
# PROBABILITY VALUES
# ─────────────────────────────────────────────

study_probability = {
    "High": 0.7,
    "Low": 0.3
}

attendance_probability = {
    "Good": 0.8,
    "Poor": 0.2
}

# Conditional Probability Table

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
# USER INPUT
# ─────────────────────────────────────────────

print("================================================")
print("BAYESIAN NETWORK")
print("================================================")

study = input("Enter Study Level (High/Low): ")

attendance = input("Enter Attendance (Good/Poor): ")

# ─────────────────────────────────────────────
# INFERENCE
# ─────────────────────────────────────────────

result = result_probability[(study, attendance)]

print("\nProbability of Pass :", result["Pass"])

print("Probability of Fail :", result["Fail"])
