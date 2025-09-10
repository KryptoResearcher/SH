"""
Property-based tests for semantic mapping properties.
"""
from hypothesis import given, strategies as st
from src.legal.mapping import semantic_map

# Strategies
field_elements = st.integers(min_value=0, max_value=999)
verdict_spaces = st.lists(st.text(min_size=1), min_size=1, max_size=10)

@given(element=field_elements, space=verdict_spaces)
def test_mapping_in_bounds(element, space):
    # Property: The mapping should always return a verdict from the space
    field_size = 1000
    verdict = semantic_map(element, space, field_size)
    assert verdict in space

@given(space=verdict_spaces)
def test_mapping_cover_entire_space(space):
    # Property: For a large enough field, all verdicts should be reachable
    # We use a field size much larger than the verdict space size
    field_size = 10000 * len(space)
    
    # This is a probabilistic test - we can't test all elements, but we can test many
    tested_verdicts = set()
    # Test at strategic points: the "boundaries" for each verdict
    for i in range(len(space)):
        element = (i * field_size) // len(space)
        verdict = semantic_map(element, space, field_size)
        tested_verdicts.add(verdict)
    
    # We should have encountered all verdicts
    assert tested_verdicts == set(space)