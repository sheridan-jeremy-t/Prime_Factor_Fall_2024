"""Testing file for Generate Prime Factors"""

import pytest
from prime import generate_prime_factors
#step 1 ValueError if not integer
def test_not_integer():
    """test to see if input was an integer if not return ValueError"""
    with pytest.raises(ValueError):
        generate_prime_factors("Hello")
#step 2 return empty list if n == 1
def test_input():
    """main function for assert"""
    assert generate_prime_factors(1)
#step 3 return [2] if 2 is called
    assert generate_prime_factors(2) == [2]
#step 4 return [3] if 3 is called
    assert generate_prime_factors(3) == [3]
#step 5 return [2,2] if 4 is called
    assert generate_prime_factors(4) == [2,2]
#step 6 return [2,3] if 6 is called
    assert generate_prime_factors(6) == [2,3]
#step 7 return [2,2,2] if 8 is called
    assert generate_prime_factors(8) == [2,2,2]
#step 8 return [3,3] if 9 is called
    assert generate_prime_factors(9) == [3,3]
