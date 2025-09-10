

#This file is used to define common test fixtures that can be shared across multiple test files.

import pytest
from src.core.fields import FiniteField
from src.types import SHParameters, RelationalContext

# Define a small prime field for fast testing
TEST_PRIME = 10007

@pytest.fixture
def test_field():
    """Provides a finite field instance for testing."""
    return FiniteField(TEST_PRIME)

@pytest.fixture
def test_params(test_field):
    """Provides a default SHParameters instance for testing."""
    # Find a non-residue for the test field
    # For test field of 10007, a known non-residue is 5 (can be verified)
    test_alpha = 5
    return SHParameters(
        field_size=TEST_PRIME,
        alpha=test_alpha,
        iterations=5,  # Small number for speed
        security_param=32
    )

@pytest.fixture
def test_context():
    """Provides a simple RelationalContext for testing."""
    return RelationalContext(
        relationship_type="test",
        context_type="test",
        jurisdiction="test",
        legal_framework="test",
        verdict_space=["Verdict_A", "Verdict_B", "Verdict_C"]
    )