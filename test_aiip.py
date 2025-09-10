"""
Unit tests for AIIP iteration in src/core/aiip.py.
"""
from src.core.aiip import compute_iteration_trace

def test_aiip_trace_length(test_field, test_params):
    # Test that the trace has the correct length (n+1 elements)
    start = 5
    trace = compute_iteration_trace(start, test_params.alpha, test_params.iterations, test_field)
    assert len(trace) == test_params.iterations + 1  # [x₀, x₁, ..., xₙ]

def test_aiip_iteration_correctness(test_field, test_params):
    # Test the first iteration manually: x1 = (x0² + α) mod p
    start = 5
    trace = compute_iteration_trace(start, test_params.alpha, 1, test_field)
    expected_x1 = (start * start + test_params.alpha) % test_field.prime
    assert trace[1] == expected_x1

def test_aiip_determinism(test_field, test_params):
    # Test that the same input always produces the same output
    start = 1234
    trace1 = compute_iteration_trace(start, test_params.alpha, test_params.iterations, test_field)
    trace2 = compute_iteration_trace(start, test_params.alpha, test_params.iterations, test_field)
    assert trace1 == trace2