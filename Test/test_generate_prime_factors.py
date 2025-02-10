import pytest
from prime import generate_prime_factors
#step 1 ValueError if not integer
def test_not_integer():
    with pytest.raises(ValueError):
        generate_prime_factors("Hello")
#step 2 return empty list if n == 1
def test_empty_list_if_one_called():
    assert generate_prime_factors(1) == 1