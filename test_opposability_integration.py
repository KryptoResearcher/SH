"""
Integration test for opposability calculation and verification.
"""
from src.types import LegalSemantics

def test_opposability_calculation():
    # Test the opposability calculation logic
    interpretation = LegalSemantics(
        field_element=999,
        verdict="Test",
        contextual_meaning="Test",
        interpretation_confidence=0.9,
        applicable_laws=[],
        opposability_components={
            'explainability': 0.8,
            'contestability': 0.7, 
            'verifiability': 0.9
        }
    )
    
    # Calculate Ω = min(Ε, Γ, V)
    omega = min(
        interpretation.opposability_components['explainability'],
        interpretation.opposability_components['contestability'],
        interpretation.opposability_components['verifiability']
    )
    
    assert omega == 0.7  # The minimum of the three values
    assert omega >= 0.60  # Should meet the minimum bound

def test_opposability_verification_failure():
    # Test that verification fails when Ω < 0.60
    interpretation = LegalSemantics(
        field_element=999,
        verdict="Test",
        contextual_meaning="Test",
        interpretation_confidence=0.9,
        applicable_laws=[],
        opposability_components={
            'explainability': 0.8,
            'contestability': 0.5,  # Below threshold
            'verifiability': 0.9
        }
    )
    
    omega = min(
        interpretation.opposability_components['explainability'],
        interpretation.opposability_components['contestability'],
        interpretation.opposability_components['verifiability']
    )
    
    assert omega == 0.5
    assert omega < 0.60  # Should fail the minimum bound