"""
prime.py -- Write the application code here
"""
def generate_prime_factors(n):
    """the general function"""
    if not isinstance(n, int):
        raise ValueError("Not an integer")
    # if n == 1:
    #     return []
    # if n == 2:
    #     return [2]
    # if n == 3:
    #     return [3]
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2
    if n > 1:
        factors.append(n)
    return factors
