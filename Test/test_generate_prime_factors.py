import pytest
from prime import generate_prime_factors
#step 1 ValueError if not integer
def test_not_integer():
    with pytest.raises(ValueError):
        generate_prime_factors("Hello")
#step 2 return empty list if n == 1
def test_empty_list_if_one_called():
    assert generate_prime_factors(1) == []
#step 3 return [2] if 2 is called
def test_if_two_called():
    assert generate_prime_factors(2) == [2]
#step 4 return [3] if 3 is called
def test_if_three_called():
    assert generate_prime_factors(3) == [3]
