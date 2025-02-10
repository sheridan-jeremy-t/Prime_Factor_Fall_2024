import pytest
from prime import generate_prime_factors

def test_not_integer():
    with pytest.raises(ValueError):
        generate_prime_factors("Hello")

