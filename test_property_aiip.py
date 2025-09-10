"""
Property-based tests for AIIP properties using hypothesis.
"""
from hypothesis import given, strategies as st
from src.core.aiip import compute_iteration_trace

# Strategy for generating values in our test field
field_elements = st.integers(min_value=0, max_value=10006)  # For TEST_PRIME = 10007

@given(start=field_elements, n=st.integers(min_value=1, max_value=10))
def test_aiip_trace_length_property(test_field, test_params, start, n):
    # Property: Trace should always have length n+1
    trace = compute_iteration_trace(start, test_params.alpha, n, test_field)
    assert len(trace) == n + 1

@given(start=field_elements)
def test_aiip_determinism_property(test_field, test_params, start):
    # Property: Same input always produces same output (determinism)
    n = 5
    trace1 = compute_iteration_trace(start, test_params.alpha, n, test_field)
    trace2 = compute_iteration_trace(start, test_params.alpha, n, test_field)
    assert trace1 == trace2

@given(start=field_elements)
def test_aiip_range_property(test_field, test_params, start):
    # Property: All elements in the trace must be valid field elements [0, p-1]
    n = 5
    trace = compute_iteration_trace(start, test_params.alpha, n, test_field)
    for element in trace:
        assert 0 <= element < test_field.prime