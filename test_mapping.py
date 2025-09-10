"""
Unit tests for semantic mapping in src/legal/mapping.py.
"""
from src.legal.mapping import semantic_map

def test_semantic_map_bounds():
    # Test mapping at the lower and upper bounds of the field
    field_size = 100
    verdict_space = ["A", "B", "C"]
    
    # Element 0 should map to first verdict
    assert semantic_map(0, verdict_space, field_size) == "A"
    # Element 99 should map to last verdict
    assert semantic_map(99, verdict_space, field_size) == "C"

def test_semantic_map_distribution():
    # Test that the mapping is roughly uniform for a small example
    field_size = 12  # Divisible by verdict space size for clean test
    verdict_space = ["A", "B", "C"]  # 3 verdicts
    # Each verdict should get exactly 4 field elements: 12/3=4
    # Elements 0-3 -> A, 4-7 -> B, 8-11 -> C
    
    assert semantic_map(0, verdict_space, field_size) == "A"
    assert semantic_map(3, verdict_space, field_size) == "A"
    assert semantic_map(4, verdict_space, field_size) == "B"
    assert semantic_map(7, verdict_space, field_size) == "B"
    assert semantic_map(8, verdict_space, field_size) == "C"
    assert semantic_map(11, verdict_space, field_size) == "C"