"""
Unit tests for finite field arithmetic in src/core/fields.py.
"""
import pytest
from src.core.fields import FiniteField

def test_field_initialization():
    field = FiniteField(11)
    assert field.prime == 11

def test_field_addition(test_field):
    # Test basic addition: (a + b) mod p
    assert test_field.add(10, 20) == (10 + 20) % test_field.prime

def test_field_multiplication(test_field):
    # Test basic multiplication: (a * b) mod p
    assert test_field.mul(100, 50) == (100 * 50) % test_field.prime

def test_field_inverse(test_field):
    # Test that a * a⁻¹ ≡ 1 mod p
    a = 123
    a_inv = test_field.inv(a)
    assert test_field.mul(a, a_inv) == 1

def test_field_inverse_zero():
    # Test that trying to invert zero raises an error
    field = FiniteField(11)
    with pytest.raises(ValueError):
        field.inv(0)