# python-foundation-stability.py

"""
Mandala Foundation Stability Checker
Analyzes the four Embodied Foundations (Nourishment, Cleansing, Restoration, Movement)
to determine if a system is stable enough for strategic planning (VSM System 4).
Requires all foundations to meet a stability threshold of 2.
"""

def check_foundation_stability(nourishment: int, cleansing: int, restoration: int, movement: int) -> dict:
    """
    Checks the stability of the four Embodied Foundations.

    Args:
        nourishment: N_score (0-3)
        cleansing: C_score (0-3)
        restoration: R_score (0-3)
        movement: M_score (0-3)

    Returns:
        A dictionary containing the overall status and a list of areas requiring focus.
    """
    
    foundations = {
        "Nourishment": nourishment,
        "Cleansing": cleansing,
        "Restoration": restoration,
        "Movement": movement
    }
    
    UNSTABLE_THRESHOLD = 2
    unstable_foundations = []

    for name, score in foundations.items():
        if score < UNSTABLE_THRESHOLD:
            unstable_foundations.append(f"{name} (Score: {score})")
            
    is_stable = not unstable_foundations
    
    if is_stable:
        status_message = "All Foundations are stable (≥2). Proceed with VSM System 4 Strategic Planning."
    else:
        status_message = (
            "Foundations are unstable. HALT strategic planning."
            "Focus exclusively on stabilization for the listed foundations."
        )

    return {
        "status": "Stable" if is_stable else "Unstable",
        "message": status_message,
        "unstable_areas": unstable_foundations,
        "scores": foundations
    }

# --- Example Usage ---
# Scenario 1: Unstable Foundation (Low Nourishment)
result_unstable = check_foundation_stability(
    nourishment=1, 
    cleansing=3, 
    restoration=2, 
    movement=3
)
print("--- Unstable Result ---")
print(result_unstable)

# Scenario 2: Stable Foundations
result_stable = check_foundation_stability(
    nourishment=2, 
    cleansing=3, 
    restoration=2, 
    movement=2
)
print("\n--- Stable Result ---")
print(result_stable)
