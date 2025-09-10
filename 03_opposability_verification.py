#!/usr/bin/env python3
"""
Example 3: Opposability Verification
Demonstrates the calculation and verification of the opposability score Ω.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.types import LegalSemantics

def calculate_opposability(interpretation: LegalSemantics) -> float:
    """
    Calculates the overall opposability score Ω as the minimum of its components.
    This implements the formula: Ω = min(Ε, Γ, V)
    """
    components = interpretation.opposability_components
    return min(components['explainability'], 
               components['contestability'], 
               components['verifiability'])

def verify_opposability(interpretation: LegalSemantics, threshold: float = 0.60) -> bool:
    """
    Verifies if an interpretation meets the minimum opposability bound.
    """
    omega = calculate_opposability(interpretation)
    return omega >= threshold

def main():
    print("=== Example 3: Opposability Verification ===\n")
    
    # Create a mock legal interpretation with opposability components
    interpretation = LegalSemantics(
        field_element=987654,
        verdict="Liable for Breach of Contract",
        contextual_meaning="The party failed to meet the agreed-upon deliverables...",
        interpretation_confidence=0.85,
        applicable_laws=["UCC §2-314", "Restatement (Second) of Contracts §235"],
        opposability_components={
            'explainability': 0.75,   # Good explanation
            'contestability': 0.90,   # Strong contestation pathways
            'verifiability': 0.99     # STARK proof is valid
        }
    )
    
    # Calculate and verify
    omega_score = calculate_opposability(interpretation)
    is_valid = verify_opposability(interpretation)
    
    print(f"Interpretation: '{interpretation.verdict}'")
    print(f"Opposability Components: {interpretation.opposability_components}")
    print(f"Overall Opposability Score Ω: {omega_score:.3f}")
    print(f"Meets Minimum Bound (Ω ≥ 0.60)? {is_valid}")
    
    # Demonstrate a failure case
    interpretation.opposability_components['explainability'] = 0.55
    omega_score = calculate_opposability(interpretation)
    is_valid = verify_opposability(interpretation)
    
    print(f"\n--- After Explainability Challenge ---")
    print(f"Opposability Components: {interpretation.opposability_components}")
    print(f"Overall Opposability Score Ω: {omega_score:.3f}")
    print(f"Meets Minimum Bound (Ω ≥ 0.60)? {is_valid}")

if __name__ == "__main__":
    main()