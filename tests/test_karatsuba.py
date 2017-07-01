"""Tests for stanford_algorithms.karatsuba."""
import pytest
from stanford_algorithms import karatsuba


def test_karatsuba():
    """Test for the info function."""
    assert karatsuba.karatsuba(1024, 1024) == 1048576
