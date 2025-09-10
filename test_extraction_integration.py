"""
Integration test for the complete SH extraction process.
"""
from src.core.aiip import compute_iteration_trace
from src.legal.mapping import semantic_map
from src.types import LegalSemantics

def test_complete_extraction(test_field, test_params, test_context):
    # Test the complete flow from input to LegalSemantics
    input_data = 1234
    
    # 1. Compute cryptographic trace
    trace = compute_iteration_trace(input_data, test_params.alpha, test_params.iterations, test_field)
    
    # 2. Apply semantic mapping
    final_verdict = semantic_map(trace[-1], test_context.verdict_space, test_params.field_size)
    
    # 3. Create LegalSemantics object
    interpretation = LegalSemantics(
        field_element=trace[-1],
        verdict=final_verdict,
        contextual_meaning=f"Test interpretation for {final_verdict}",
        interpretation_confidence=0.95,
        applicable_laws=["Test_Law_1"],
        opposability_components={'explainability': 0.8, 'contestability': 0.9, 'verifiability': 1.0}
    )
    
    # Verify the result
    assert interpretation.verdict in test_context.verdict_space
    assert interpretation.interpretation_confidence > 0
    assert len(interpretation.applicable_laws) > 0